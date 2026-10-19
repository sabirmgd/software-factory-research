# UC-001 — Assign responsibility without granting access

**Status:** illustrative product contract. **Outcome hypothesis:** coordinators can make responsibility clear with fewer clarification steps while preserving access boundaries. No customer outcome has been measured.

## Actor, trigger, and preconditions

An authenticated team coordinator with the `tasks:assign` capability chooses an assignee for an existing task. Their membership is active in the task's workspace. The target is an active eligible member who can already access the task. A product persona called coordinator does not automatically imply a security role; this example maps the capability to an illustrative manager role.

## Successful interaction

The coordinator opens a task they may access, selects an eligible person, and submits the assignment. The system confirms the new assignee and revision. Assignment and audit change together. The operation does not grant sharing rights or expose task contents to a new audience.

## Alternatives and failures

A stale edit asks the coordinator to refresh rather than overwriting newer work. An invalid target leaves the current assignment unchanged. A request without authority is denied. A resource outside the selected workspace is not exposed. A repeated successfully applied request returns its recorded result without creating another audit event, provided the caller is still authorized to receive that result.

## Invariants

I-01: no cross-workspace assignment. I-02: no assignment to an inactive or ineligible target. I-03: assignment does not create access. I-04: failed operations leave state unchanged. I-05: one applied command creates one audit event. I-06: the public operation, not each caller, owns assignment policy.

## Product questions resolved for this illustration

Assignment does not imply sharing. External collaborators are excluded from the initial version. Notifications are out of scope; the audit event does not imply that a message has been sent. Membership freshness at a real database commit remains a technical consistency decision, not something the in-memory model establishes.
