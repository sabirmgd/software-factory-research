# Bounded delegation contract

**Reusable template.** Use before autonomous work with material scope or side effects. For low-risk work, these fields can live in a short work item.

[Template guide](../README.md) · [Filled or worked reference](../../examples/task-assignment/delegation-contract.md)


## Objective
Approved result, relevant use case, current source revision, and explicit non-goals.

## Authority
Allowed files, modules, environments, commands, and external actions. Forbidden actions and protected policy/test areas. State whether package installation, network access, data access, commits, PR creation, merge, and deployment are authorized; these are different permissions.

## Constraints
Stable contracts and invariants. Required test and security policy. Dependencies that cannot be changed without review. Never infer approval from a proposed document.

## Evidence
Commands and checks required, how evidence is captured, and what is independently checked. Tests may be changed for legitimate reasons, but weakening accepted criteria requires explicit review.

## Budget and escalation
Time/action/attempt budget, stop conditions, and the accountable escalation recipient. Stop on consequential unknowns, new authority requirements, or repeated design friction. Autonomous work may pause; nonresponse is not approval.

## Completion and release
Define implementation-complete separately from merge-authorized, release-authorized, and outcome-evaluated. Record handoff and recovery ownership.
