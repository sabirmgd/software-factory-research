# 10. Verification and safe delivery

[Reading guide](../READING-GUIDE.md) · [Previous: Make Clear and human understanding](09-make-clear-and-human-understanding.md) · [Next: Customer outcomes and factory learning](11-customer-outcomes-and-factory-learning.md)

> **Status:** Proposed. Evidence supports specific claims; it does not create release authority automatically.

## Replace “it works” with a claim

“The feature works” is too broad to verify.

For task reassignment, useful claims include:

- an authorized manager can assign an active member of the same workspace;
- an unauthorized request leaves task and audit state unchanged;
- a member from another workspace cannot become the assignee;
- retrying the same request does not duplicate the audit event; and
- a stale revision does not overwrite a newer assignment.

Each claim needs evidence that can actually observe it.

## Match the evidence to the claim

Different checks answer different questions:

- **Types:** Are known commands, identifiers, and result shapes represented correctly?
- **Domain tests:** Do business rules and state transitions behave correctly?
- **Integration tests:** Do persistence and external boundaries behave as required?
- **Contract tests:** Do public interfaces retain their agreed shape and meaning?
- **End-to-end tests:** Does a real workflow work across components?
- **Architecture checks:** Are specified structural rules being followed?
- **Operational observation:** Does the deployed system behave correctly with its actual configuration and dependencies?

No layer proves everything. A browser test may miss invalid states. A unit test may miss a missing route guard. A schema test may prove shape without proving entitlement.

The runnable assignment model in this repository demonstrates only in-memory behavior and typed declarations. It does not prove database transactions, identity-provider behavior, framework integration, or production readiness.

## Test denied behavior as carefully as allowed behavior

Happy-path tests show what succeeds. Denied cases expose hidden obligations.

For reassignment, test:

- no authenticated actor;
- insufficient permission;
- wrong workspace;
- inactive or ineligible assignee;
- hidden or missing task;
- stale revision;
- repeated request; and
- storage failure before commit.

Also prove what did **not** happen. A rejected request should not partially update the task, write a misleading audit event, or reveal whether a hidden resource exists.

Timing matters. If membership can be revoked while the assignment is being committed, the product and technical design must define the intended result. A test should not quietly assume the race away.

## Independence is more than a second agent

A second agent may notice different problems, but it can share the author's assumptions, model weaknesses, and incomplete context.

Stronger independence can come from:

- externally observable behavior;
- tests derived from an accepted use case;
- a route or policy inventory built separately from the implementation;
- an invalid fixture that challenges the checker; or
- a reviewer examining evidence before reading the author's explanation.

These reduce particular forms of self-confirmation. None guarantees complete coverage.

One rule is critical: the implementing agent must not silently redefine success. If a test or policy is wrong, make that correction visible and review it separately.

## Test whether the tests can fail

A test that stays green when the intended behavior is broken may protect nothing.

Deliberately introduce a representative defect or use mutation testing where appropriate. For example, remove the workspace comparison or allow a failed commit to retain its audit event. The relevant test should fail for the expected reason.

Mutation tools such as Stryker provide one mechanism for JavaScript and TypeScript. Surviving mutations are questions to investigate, not automatic proof that the suite is bad. [S22](../research/sources/index.md#s22)

Expensive analysis does not need to run on every edit. Focus it on important policies and recurring weak spots.

## Package the evidence for review

A useful evidence package contains:

- the accepted behavior;
- the exact revision;
- commands and environments actually used;
- passed, failed, blocked, and unrun checks;
- relevant artifacts; and
- remaining limitations.

A Make Clear view may summarize the user-visible change, boundary, and important failure path. It should link to evidence rather than replace it.

Keep secrets, personal data, and unnecessary customer records out of logs and screenshots.

## Release is a separate action

A commit, merge, preview, limited rollout, and full production release are different actions. Approval of a design does not authorize all of them.

Release planning should state:

- who will be exposed;
- what will be monitored;
- what condition stops expansion;
- what can be rolled back; and
- which effects cannot be undone.

Google's SRE guidance describes canarying as a limited deployment evaluated before wider rollout. It is one containment option, not a requirement for every feature. [S23](../research/sources/index.md#s23)

Reverting code does not reverse a sent message, initiated payment, or disclosed record. Recovery claims must name the state and side effects that can actually be restored.

## Operational readiness belongs to the feature

Correct code may still require configuration, credentials, migrations, backfills, support ownership, alerts, and user access.

Plan these before production. Database changes need compatibility and recovery. An expand–migrate–contract sequence can reduce release coupling, but destructive migrations and backfills still need their own evidence and authority.

> **Do not confuse:** green code checks with a usable deployed feature.

## What to do next

For each important behavior:

1. Write the claim precisely.
2. Choose the cheapest evidence that can observe it credibly.
3. Include the denied or failure case.
4. Record the actual revision and environment.
5. Decide release authority separately.

Confidence should come from inspectable claims, not a polished completion message.

---

[Previous: Make Clear and human understanding](09-make-clear-and-human-understanding.md) · [Next: Customer outcomes and factory learning](11-customer-outcomes-and-factory-learning.md)
