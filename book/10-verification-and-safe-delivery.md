# 10. Verification and safe delivery

[Reading guide](../READING-GUIDE.md) · [Previous: Make Clear and human understanding](09-make-clear-and-human-understanding.md) · [Next: Customer outcomes and factory learning](11-customer-outcomes-and-factory-learning.md)

> **Status:** Proposed synthesis, with attributed sources. Illustrations are not client results.

## Verification answers a claim, not a feeling

“The feature works” is too broad to evaluate. A useful claim identifies behavior, conditions, and evidence: an authorized manager can assign an active member in the same workspace; an unauthorized request leaves state unchanged; a repeated command does not duplicate the audit event. Each claim needs an appropriate observation.

Verification is not a single agent role. It is a collection of mechanisms that compare the implementation with accepted behavior and constraints. A reviewer may interpret the evidence, but evidence should remain independently inspectable rather than existing only in the reviewer's summary.

## A layered evidence plan

Types can check certain representations. Domain tests can exercise rules and state transitions. Integration tests can examine persistence and external boundaries. Contract tests can check public shapes. End-to-end tests can exercise a real workflow across components. Architecture checks can detect specified structural violations. Operational observation can reveal behavior in deployment.

None substitutes for all the others. A browser flow may not explore every invalid state. A unit test may not reveal a missing route guard. A schema check may not establish that a user is entitled to the data returned. Select the evidence according to the claim and the risk rather than maximizing the number of tests indiscriminately.

The runnable assignment model in this repository provides a deliberately narrow demonstration. Its tests establish behavior of an in-memory implementation and typed declarations. They do not establish the correctness of a NestJS integration, database transaction, identity provider, or production system. See the [example's scope](../examples/task-assignment/runnable/README.md).

## Negative cases expose hidden obligations

For an assignment operation, test unauthenticated access, insufficient capability, cross-workspace references, inactive membership, unavailable targets, stale revisions, and repeated commands. Also test that failures do not leave partial state or leak details the actor should not see.

A policy test matrix is valuable because it makes the intended distinction explicit. The case “manager in the wrong workspace” is different from “member in the right workspace.” Roles alone do not settle resource access.

Timing can matter. A check performed before a concurrent revocation may have different semantics from a policy enforced at commit time. The technical design must choose the requirement and an implementation mechanism. Tests should reproduce the relevant timing where feasible; they should not quietly assume away the race.

## Independence has several meanings

A second agent can review without being the original author, but it may still share the same assumptions, model weaknesses, or incomplete context. Treat it as another source of scrutiny rather than as an oracle.

Stronger independence can come from externally observable behavior, tests derived from an accepted use case, a separate route inventory, or a reviewer examining evidence without seeing the author's rationale first. These mechanisms reduce particular forms of self-confirmation. They do not guarantee complete coverage.

One rule is especially important: the implementing agent must not silently redefine success. It may identify a faulty test or an outdated policy, but changing the evaluator should be separately visible and authorized. A green result obtained by deleting a relevant assertion is not equivalent to a correct implementation.

## Test quality can itself be challenged

A test that continues to pass when the intended behavior is broken may not protect the claim it appears to protect. Deliberately introduce a representative defect, or use mutation testing where appropriate, to examine whether the test detects the change. Mutation tooling such as Stryker supplies one mechanism for JavaScript and TypeScript; selecting and configuring it remains project work. [S22](../research/sources/index.md#s22)

This need not run on every local edit. Focus expensive analysis on consequential policies and recurring weak spots. Treat a surviving mutation as a question to investigate, not automatic proof that the test suite is bad; the mutation may be equivalent or outside the relevant behavior.

## The evidence package

A compact review package should identify the accepted behavior, the change revision, the actual commands and environments used, their outcomes, relevant artifacts, and remaining limitations. It should distinguish passed, failed, not run, and blocked checks.

A Make Clear view can make the package easier to understand: what changed for the user, which boundary changed, and which important failure path was demonstrated. It must link back to the evidence rather than replacing it with a confident narrative.

Do not include secrets, production personal data, or unnecessary customer records in logs and screenshots. Evidence should be sufficient for the claim and appropriately scoped for the audience.

## Delivery is an action with its own authority

A merge, preview deployment, limited rollout, and full production release are different actions. Approval of a technical design does not automatically authorize all of them. The delegation contract should state which are permitted.

Release design includes who is exposed, what will be observed, what conditions stop expansion, and what recovery can accomplish. Google's SRE guidance describes canarying as a limited deployment evaluated before broader rollout. We use that principle as one possible containment mechanism, not a universal requirement for every application. [S23](../research/sources/index.md#s23)

Reverting code is not the same as reversing consequences. A message sent, a payment initiated, or data disclosed may require compensation or incident response. A claim of reversibility must name the state and side effects that can actually be restored.

## Operational readiness is part of the feature

A feature may require configuration, credentials, migrations, backfills, support ownership, alerts, and access for its users. These are not cosmetic delivery details. Missing one can prevent value even when the code is correct.

For database changes, plan compatibility and recovery explicitly. An expand/migrate/contract sequence may reduce coupling between releases, but destructive migrations and backfills still require their own evidence and authority. Do not let an agent discover these requirements only when it reaches production.

## The practical implication

Define verification at design time, execute it against the actual change, and preserve its scope. Then decide separately whether the available evidence and recovery plan justify the permitted release. Confidence should come from inspectable claims, not a polished completion message.

---

[Previous: Make Clear and human understanding](09-make-clear-and-human-understanding.md) · [Next: Customer outcomes and factory learning](11-customer-outcomes-and-factory-learning.md)
