# Module contract

**Reusable template.** Use for a meaningful capability boundary, not every utility file. Review when ownership, public meaning, or access rules change.

[Template guide](../README.md) · [Filled or worked reference](../../examples/task-assignment/technical-design.md)


## Purpose and ownership
What business knowledge and state does this module own? Which decisions should callers not need to know? Name the owner of each authoritative state item.

## Public capability
Show a caller accomplishing a task with the public API. Define input/output semantics, errors, identity context, invariants, and compatibility expectations. Avoid repository accessors that push orchestration back to callers.

## Private knowledge and dependencies
Define what is hidden: representations, storage, provider mechanics, coordination, or policy. State allowed dependency direction and explicit exceptions. Shared types need shared meaning, not merely similar shapes.

## Consistency and access
Explain authorization responsibility, tenant scope, atomicity, retries, and side effects. A boundary document does not itself implement enforcement.

## Enforcement and examples
Link package exports, dependency checks, behavior tests, fixtures demonstrating rejection, and a reference usage. State advisory signals separately from hard constraints.

## Change scenarios
Give plausible next requirements, predicted locality, and conditions that would challenge the interface. Do not prebuild all possible futures.
