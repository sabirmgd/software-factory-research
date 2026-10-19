# Use case

**Reusable template.** Use for a business behavior; avoid generating a separate document for every route or UI component.

[Template guide](../README.md) · [Filled or worked reference](../../examples/task-assignment/use-case.md)


## Identity and intent
ID: [UC-...]. Status: [draft / accepted / superseded]. Primary actor: [human or service]. Actor goal: [business outcome]. Trigger and preconditions: [facts required].

## Successful interaction
Describe the actor's actions and observable responses from beginning to successful outcome. Do not replace behavior with a list of implementation calls.

## Alternatives and failures
Describe denied access, invalid input, stale state, retries, partial failure, and cancellation where applicable. What should the actor see, and what must remain unchanged?

## Invariants
Assign stable IDs to rules that must hold across entry points. Separate persona motivation from security role, identity, resource access, and tenant scope.

## Acceptance scenarios
Use concrete Given / When / Then examples including a success, a denied case, and a relevant failure. Link to tests once they exist; do not treat a test plan as execution evidence.

## Open decisions
Name unresolved behavior, the decision owner, and whether implementation can proceed without settling it. Record non-goals.
