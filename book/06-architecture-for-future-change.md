# 6. Architecture for future change

[Reading guide](../READING-GUIDE.md) · [Previous: Research and adaptive planning](05-research-and-adaptive-planning.md) · [Next: Executable engineering constraints](07-executable-engineering-constraints.md)

> **Status:** Proposed. The examples describe design choices, not one universal architecture.

## Architecture is about the next change

Architecture matters because software will change again.

A design is useful when it helps a contributor find where a change belongs, understand what must remain true, and modify behavior without learning unrelated internals.

For task reassignment, the question is not which folder name looks cleanest. It is who owns assignment rules, membership checks, conflict handling, persistence, and audit behavior—and how another feature can use that responsibility safely.

## Find modules through owned knowledge

A module should own a coherent piece of business knowledge or state.

The Tasks module may own the lifecycle and assignment of tasks. A Membership capability may answer whether a person is an active member of a workspace. An Audit capability may record accepted events. The exact boundaries depend on the product, but ownership should be explicit.

Do not create modules merely by grouping technical files or nouns. Ask:

- What decision does this module own?
- What state may it change?
- What rules does it protect?
- How may other code ask it to act?

If several modules can directly edit the same task assignment, the system has hidden shared ownership.

## Design from the caller backward

Begin with what a caller needs to accomplish.

Instead of exposing repositories and expecting every caller to coordinate membership, task loading, authorization, conflict checks, persistence, and audit, expose one operation with clear inputs and outcomes.

For example:

```text
assign(actor, workspace, task, assignee, expected revision, request id)
  -> success with new revision
  -> or a named failure
```

The operation is not automatically correct because it is small. It must still define permissions, transaction behavior, side effects, and failure semantics. Its purpose is to give one place responsibility for the coordination.

## Prefer deep modules, not mystery boxes

A deep module has a small useful interface and substantial internal responsibility. It saves callers from repeating coordination they should not own.

Ousterhout's module-depth idea supports this direction. [S14](../research/sources/index.md#s14)

Depth does not mean a giant class, a long call chain, or hidden side effects. A module must expose the consequences callers need to reason about. If reassignment sends notifications, grants access, or triggers billing, those effects cannot disappear behind an innocent-looking method name.

## Protect business rules without ceremonial layers

Clean Architecture argues that business policy should not depend directly on web frameworks, databases, or external providers. [S08–S09](../research/sources/index.md#s08)

The practical benefit is change isolation. The assignment rules can be tested without a running web server. A new persistence mechanism does not redefine eligibility. An HTTP error mapper does not become the source of business truth.

But layers are not valuable by themselves. An interface that simply forwards every method to an identical implementation adds movement without hiding complexity or protecting a decision.

> **Do not confuse:** more layers with better boundaries.

## Share contracts carefully

Shared types can reduce drift across services or applications. They can also couple unrelated release cycles and expose internal concepts as permanent public contracts.

Share a type when several consumers genuinely depend on the same stable meaning. Keep local implementation details local. A task-assignment command may be a useful public contract; the private shape of a database row usually is not.

The source material on stable boundaries supports separating policy from delivery mechanisms, but the correct package structure remains project-specific. [S08](../research/sources/index.md#s08)

## Database ownership is part of architecture

A folder boundary means little when any module may write any table.

State ownership should identify:

- who may write the data;
- which operations are supported;
- which invariants must hold;
- how other modules read or react to changes; and
- what transaction guarantees are available.

One physical database may serve several modules. That does not require shared write ownership.

For reassignment, task state and audit state may need one atomic decision. If the storage cannot provide that behavior, the design must define an alternative rather than letting a partial update appear successful.

## Treat friction as design feedback

One awkward change does not prove the architecture is wrong. Repeated friction is more informative.

Signals include:

- the same rule implemented in several places;
- frequent changes touching unrelated modules;
- recurring private-detail leaks through public interfaces;
- tests requiring large amounts of unrelated setup; and
- contributors repeatedly asking where a behavior belongs.

The response may be a better boundary, a clearer operation, a new check, or removal of an abstraction that no longer helps.

## Measure without pretending the metric is the goal

Change locality, public-interface growth, duplication, test setup, and later modification cost are useful signals. None is a universal score.

A legitimate cross-cutting change may touch many files. A tiny diff may hide a dangerous behavior. Use metrics to find questions, then inspect why the change took its shape.

## What to do next

For the next feature, draw a small ownership map:

1. Which module owns the decision?
2. Which state may it change?
3. Which other capabilities must it consult?
4. What is the smallest public operation callers need?
5. Which failure or side effect must remain visible?

If those answers are unclear, resolve the ownership before extracting generators or adding more layers.

---

[Previous: Research and adaptive planning](05-research-and-adaptive-planning.md) · [Next: Executable engineering constraints](07-executable-engineering-constraints.md)
