# PRD-001 — Make task responsibility explicit

**Status:** illustrative decision set. **Related use case:** [UC-001](use-case.md). **No real customer approval or outcome result is claimed.**

## Problem and success hypothesis

Coordinators need to establish who is responsible for a task without accidentally granting information access or overwriting another person's changes. We hypothesize that a clear assignment flow with explicit failure behavior will reduce clarification and mistaken assignment. A real evaluation would observe current and revised task handling, account for task difficulty and training, and record errors as well as elapsed time.

Acceptance below establishes the agreed behavior. It does not prove the outcome hypothesis.

## Users and permissions

The human persona is a coordinator. In this fictional product, an active manager membership carries `tasks:assign`. An ordinary member can read eligible tasks but cannot assign them. An external collaborator is not an eligible assignee in the initial version. A person can have different memberships in different workspaces.

## Proposed experience

The task view shows the current assignee and a revision-aware assignment control for authorized coordinators. The person list should not suggest ineligible targets as valid. Submission displays the confirmed result only after success. A conflict asks the user to refresh. A denied or invalid operation does not optimistically leave an incorrect assignee displayed.

The implementation must not rely on hidden UI controls for security. The user-visible design and server enforcement are separate requirements.

## Acceptance examples

| ID | Given / when | Required outcome |
| --- | --- | --- |
| A01 | Active authorized manager assigns eligible same-workspace member | Assignee and revision update; one audit event |
| A02 | Unauthenticated caller submits | Denied; no mutation |
| A03 | Ordinary member supplies a manager-looking client field | Denied; server-owned membership remains authoritative |
| A04 | Authorized manager references another workspace's task | No cross-workspace data or mutation |
| A05 | Target is inactive or outside the workspace | Rejected; prior assignment remains |
| A06 | Expected revision is stale | Conflict; no overwrite |
| A07 | Same accepted request is retried | Recorded result; no second audit event |
| A08 | Same request ID is reused with different intent | Conflict; no second mutation |
| A09 | Target lacks access to a restricted task | Rejected; no sharing grant |
| A10 | A persistence step fails before commit | No partial assignment or audit |
| A11 | Manager membership is revoked before a retry | Denied; cached success is not an authorization bypass |

## Non-goals

Bulk assignment, new sharing workflows, notifications, external collaborators, production identity integration, and a complete web application are outside the initial demonstration. They may be separate product work, not silent additions during implementation.

## Deferred technical decisions

The production design must settle transaction consistency, persistence and idempotency retention, route discovery, background-job enforcement, and observability. The technical design may recommend changing scope if those assumptions cannot be supported.
