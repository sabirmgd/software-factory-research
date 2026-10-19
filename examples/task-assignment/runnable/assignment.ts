import { GRANTS } from './contracts.js';
import type { AssignCommand, AssignResult, Audit, AuthenticatedActor, Fixture, Membership, Permission, Task } from './contracts.js';
type Success = Extract<AssignResult, {ok:true}>;
type Replay = { fingerprint: string; result: Success };
type State = Fixture & { audit: Audit[]; replays: Map<string, Replay> };

/**
 * A synchronous, in-memory teaching model. No real token validation, database,
 * transport, distributed concurrency, or release mechanism is implemented.
 */
export class TaskAssignments {
  #state: State;
  readonly #allowExplicitlySharedGuests: boolean;
  #failNextCommit = false;
  constructor(fixture: Fixture, options: {allowExplicitlySharedGuests?: boolean} = {}) {
    this.#state = {...structuredClone(fixture), audit: [], replays: new Map()};
    this.#allowExplicitlySharedGuests = options.allowExplicitlySharedGuests ?? false;
  }
  #membership(userId: string, workspaceId: string): Membership | undefined {
    return this.#state.memberships.find(m => m.userId === userId && m.workspaceId === workspaceId && m.active);
  }
  #canSee(task: Task, member: Membership): boolean {
    if (member.role === 'manager') return true;
    if (member.role === 'guest') return task.sharedWith.includes(member.userId);
    return task.visibility === 'workspace' || task.sharedWith.includes(member.userId);
  }
  assign(actor: AuthenticatedActor | null, command: AssignCommand): AssignResult {
    if (!actor || actor.authenticated !== true || !actor.id) return {ok:false, error:'unauthenticated'};
    const ids = [command?.workspaceId, command?.taskId, command?.assigneeId, command?.requestId];
    if (!command || ids.some(id => typeof id !== 'string' || id.trim() === '')
      || !Number.isSafeInteger(command.expectedRevision) || command.expectedRevision < 0) {
      return {ok:false, error:'invalid_command'};
    }
    // Current trusted membership, not an actor-supplied role, grants authority.
    const caller = this.#membership(actor.id, command.workspaceId);
    if (!caller || !(GRANTS[caller.role] as readonly Permission[]).includes('tasks:assign'))
      return {ok:false, error:'forbidden'};
    const task = this.#state.tasks.find(t => t.id === command.taskId && t.workspaceId === command.workspaceId);
    if (!task || !this.#canSee(task, caller)) return {ok:false, error:'not_found'};
    const key = JSON.stringify([command.workspaceId, actor.id, command.requestId]);
    const fingerprint = JSON.stringify([command.taskId, command.assigneeId, command.expectedRevision]);
    const prior = this.#state.replays.get(key);
    if (prior) {
      if (prior.fingerprint !== fingerprint) return {ok:false, error:'idempotency_conflict'};
      // This is a prior applied receipt, NOT a new assignment or current-state claim.
      return {...prior.result, replayed:true};
    }
    const target = this.#membership(command.assigneeId, command.workspaceId);
    if (!target || !this.#canSee(task, target)
      || (target.role === 'guest' && !this.#allowExplicitlySharedGuests))
      return {ok:false, error:'ineligible_assignee'};
    if (task.revision !== command.expectedRevision) return {ok:false, error:'revision_conflict'};
    const result: Success = {ok:true, taskId:task.id, assigneeId:target.userId, revision:task.revision+1, replayed:false};
    const next = structuredClone(this.#state);
    const changed = next.tasks.find(t => t.id === task.id && t.workspaceId === task.workspaceId)!;
    changed.assigneeId = target.userId; changed.revision = result.revision;
    next.audit.push({taskId:task.id, workspaceId:task.workspaceId, actorId:actor.id, assigneeId:target.userId, revision:result.revision});
    next.replays.set(key, {fingerprint, result:{...result}});
    if (this.#failNextCommit) {
      this.#failNextCommit = false;
      return {ok:false, error:'storage_unavailable'};
    }
    // A single replacement is atomic only within this synchronous model.
    this.#state = next;
    return result;
  }
  /** Test fixture helpers. These are NOT proposed production module APIs. */
  snapshot(): {tasks: Task[]; audit: Audit[]; replayCount: number} {
    return {tasks:structuredClone(this.#state.tasks), audit:structuredClone(this.#state.audit), replayCount:this.#state.replays.size};
  }
  setMembershipActive(userId: string, workspaceId: string, active: boolean): void {
    const member = this.#state.memberships.find(m => m.userId === userId && m.workspaceId === workspaceId);
    if (!member) throw new Error('Unknown fixture membership');
    member.active = active;
  }
  injectPreCommitFailure(): void { this.#failNextCommit = true; }
}
