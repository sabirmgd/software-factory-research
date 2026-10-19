# Implementation outline

**Reusable template.** Use when ordering and coordination matter. The outline schedules agreed behavior; it is not a substitute for unresolved product decisions.

[Template guide](../README.md) · [Filled or worked reference](../../examples/task-assignment/implementation-outline.md)


## Objective and governing contracts
Link the agreed use case, relevant technical design, and delegation contract. Confirm the current repository revision and what must remain unchanged.

## Preparation
Identify necessary scaffolding, seams, fixtures, or environment work. Label preparation honestly: adding a database table alone is not a user-visible vertical slice.

## Increments
For each increment give its user-observable or testable result, approximate scope, dependencies, checks, expected evidence, and rollback or discard path. A slice should exercise meaningful behavior through the necessary layers.

## Sequence and parallel work
Expose uncertainty early. State which work can proceed independently and which shared files, contracts, or environments require serialization.

## Stop and handoff
Stop on scope changes, authority gaps, repeated failed attempts beyond the budget, or evidence that contradicts the design. Record state, actual commands and results, deviations, and the next bounded task.
