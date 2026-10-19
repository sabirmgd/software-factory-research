import test from 'node:test';
import assert from 'node:assert/strict';
import {TaskAssignments} from './.build/assignment.js';
const actor = {id:'manager', authenticated:true};
const command = {workspaceId:'w1', taskId:'t1', assigneeId:'member', expectedRevision:0, requestId:'r1'};
function fixture() {
  return {
    tasks:[{id:'t1', workspaceId:'w1', assigneeId:null, revision:0, visibility:'workspace', sharedWith:[]},
      {id:'t2', workspaceId:'w2', assigneeId:null, revision:0, visibility:'workspace', sharedWith:[]}],
    memberships:[{userId:'manager', workspaceId:'w1', role:'manager', active:true},
      {userId:'member', workspaceId:'w1', role:'member', active:true},
      {userId:'other', workspaceId:'w2', role:'member', active:true},
      {userId:'guest', workspaceId:'w1', role:'guest', active:true}]
  };
}
function deniedWithoutMutation(model, who, cmd, expected) {
  const before=model.snapshot();
  assert.deepEqual(model.assign(who,cmd),{ok:false,error:expected});
  assert.deepEqual(model.snapshot(),before);
}
test('A01: eligible assignment updates state, revision and audit together',()=>{
  const m=new TaskAssignments(fixture());
  assert.deepEqual(m.assign(actor,command),{ok:true,taskId:'t1',assigneeId:'member',revision:1,replayed:false});
  assert.equal(m.snapshot().tasks[0].assigneeId,'member');
  assert.equal(m.snapshot().audit.length,1); assert.equal(m.snapshot().replayCount,1);
});
test('A02: unauthenticated request is denied without mutation',()=>deniedWithoutMutation(new TaskAssignments(fixture()),null,command,'unauthenticated'));
test('A03: forged client role does not replace trusted membership',()=>deniedWithoutMutation(new TaskAssignments(fixture()),{id:'member',authenticated:true,role:'manager'},command,'forbidden'));
test('A04: no workspace membership is denied',()=>deniedWithoutMutation(new TaskAssignments(fixture()),{id:'other',authenticated:true},command,'forbidden'));
test('A04: task in another workspace is not exposed',()=>deniedWithoutMutation(new TaskAssignments(fixture()),actor,{...command,taskId:'t2'},'not_found'));
test('A05: assignee outside workspace is ineligible',()=>deniedWithoutMutation(new TaskAssignments(fixture()),actor,{...command,assigneeId:'other'},'ineligible_assignee'));
test('A05: inactive assignee is ineligible',()=>{
  const m=new TaskAssignments(fixture());m.setMembershipActive('member','w1',false);
  deniedWithoutMutation(m,actor,command,'ineligible_assignee');
});
test('A06: revoked caller cannot assign',()=>{
  const m=new TaskAssignments(fixture());m.setMembershipActive('manager','w1',false);
  deniedWithoutMutation(m,actor,command,'forbidden');
});
test('A07: stale revision never overwrites current assignment',()=>deniedWithoutMutation(new TaskAssignments(fixture()),actor,{...command,expectedRevision:2},'revision_conflict'));
test('A08: replay returns prior receipt without duplicate audit or mutation',()=>{
  const m=new TaskAssignments(fixture());m.assign(actor,command);const before=m.snapshot();
  assert.deepEqual(m.assign(actor,command),{ok:true,taskId:'t1',assigneeId:'member',revision:1,replayed:true});
  assert.deepEqual(m.snapshot(),before);
});
test('A08: replay after caller revocation is denied',()=>{
  const m=new TaskAssignments(fixture());m.assign(actor,command);m.setMembershipActive('manager','w1',false);
  deniedWithoutMutation(m,actor,command,'forbidden');
});
test('A09: idempotency key reused for different content is rejected',()=>{
  const m=new TaskAssignments(fixture());m.assign(actor,command);
  deniedWithoutMutation(m,actor,{...command,expectedRevision:1},'idempotency_conflict');
});
test('A10: injected failure commits neither state, audit, nor replay; retry succeeds',()=>{
  const m=new TaskAssignments(fixture());m.injectPreCommitFailure();
  deniedWithoutMutation(m,actor,command,'storage_unavailable');
  assert.equal(m.assign(actor,command).ok,true);assert.equal(m.snapshot().audit.length,1);
});
test('A11: restricted task is not assigned to a member who lacks access',()=>{
  const f=fixture();f.tasks[0].visibility='restricted';const m=new TaskAssignments(f);
  deniedWithoutMutation(m,actor,command,'ineligible_assignee');
});
test('A11: explicitly shared restricted task is eligible',()=>{
  const f=fixture();f.tasks[0].visibility='restricted';f.tasks[0].sharedWith=['member'];
  assert.equal(new TaskAssignments(f).assign(actor,command).ok,true);
});
test('baseline excludes guests even when shared',()=>{
  const f=fixture();f.tasks[0].sharedWith=['guest'];
  deniedWithoutMutation(new TaskAssignments(f),actor,{...command,assigneeId:'guest'},'ineligible_assignee');
});
test('next-change profile permits explicitly shared guest without public API change',()=>{
  const f=fixture();f.tasks[0].sharedWith=['guest'];const m=new TaskAssignments(f,{allowExplicitlySharedGuests:true});
  assert.equal(m.assign(actor,{...command,assigneeId:'guest'}).ok,true);
  assert.deepEqual(m.snapshot().tasks[0].sharedWith,['guest']);
});
test('next-change profile does not silently share an unshared task',()=>{
  const m=new TaskAssignments(fixture(),{allowExplicitlySharedGuests:true});
  deniedWithoutMutation(m,actor,{...command,assigneeId:'guest'},'ineligible_assignee');
});
test('empty identifiers and invalid revision are rejected',()=>{
  const m=new TaskAssignments(fixture());
  for(const cmd of [{...command,requestId:''},{...command,expectedRevision:-1},{...command,expectedRevision:0.5}])
    deniedWithoutMutation(m,actor,cmd,'invalid_command');
});
test('snapshot is detached from the internal model',()=>{
  const m=new TaskAssignments(fixture()); const external=m.snapshot();external.tasks[0].revision=999;
  assert.equal(m.snapshot().tasks[0].revision,0);
});
