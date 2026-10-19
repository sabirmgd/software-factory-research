# Working artifacts, not paperwork quotas

These 14 templates make recurring decisions, handoffs, and evidence explicit. Use only the artifact that reduces meaningful uncertainty or coordinates real work. Combine sections for small changes. Placeholders are intentional here; the chapters and examples are written content, not placeholders.

A status field is not an approval. An expected result is not an executed test. A proposed outcome is not an observed customer improvement. Keep one owning document for each decision and link rather than copy.

| Template | When it earns its place |
|---|---|
| [Outcome hypothesis](product-and-planning/outcome-hypothesis.md) | Use when a meaningful change is justified by a user or customer benefit. A tiny maintenance task can state its purpose in its work item instead. |
| [Use case](product-and-planning/use-case.md) | Use for a business behavior; avoid generating a separate document for every route or UI component. |
| [Bounded research brief](product-and-planning/research-brief.md) | Use when a decision depends on facts not yet established. A quick lookup may be recorded inline instead. |
| [Product requirements document](product-and-planning/prd.md) | Use when user-facing behavior or success criteria need agreement. Skip a standalone PRD when an existing use case already settles them. |
| [Technical design document](product-and-planning/technical-design.md) | Use for consequential technical uncertainty. TDD here means technical design document, not test-driven development. Small known-pattern changes can use a compact design note. |
| [Implementation outline](product-and-planning/implementation-outline.md) | Use when ordering and coordination matter. The outline schedules agreed behavior; it is not a substitute for unresolved product decisions. |
| [Module contract](architecture-and-delegation/module-contract.md) | Use for a meaningful capability boundary, not every utility file. Review when ownership, public meaning, or access rules change. |
| [Architecture decision record](architecture-and-delegation/architecture-decision.md) | Use for a consequential choice with alternatives and ongoing consequences. Do not require an ADR for ordinary implementation details. |
| [Bounded delegation contract](architecture-and-delegation/delegation-contract.md) | Use before autonomous work with material scope or side effects. For low-risk work, these fields can live in a short work item. |
| [Session handoff](architecture-and-delegation/session-handoff.md) | Use when context will reset or another contributor needs to act. Keep facts durable without exporting the whole conversation. |
| [Make Clear brief](review-and-learning/make-clear-brief.md) | Use when understanding is costly or important. It may support exploration, teaching, or review; it does not automatically create an approval gate. |
| [Evidence review](review-and-learning/evidence-review.md) | Use to judge important implementation claims. For small changes use a concise PR section instead of a separate report. |
| [Outcome evaluation](review-and-learning/outcome-evaluation.md) | Use after enough real use to evaluate an outcome hypothesis. Shipping alone does not populate this record. |
| [Factory learning record](review-and-learning/learning-record.md) | Use for a recurring or consequential problem, not as mandatory ceremony after every commit. |

## Suggested use

For a new product, begin with an outcome hypothesis and a few use cases. Resolve uncertainties through evidence and prototypes, then describe the architecture needed for the first useful workflow. For an established feature, start from existing contracts and write only the delta. For an inherited system, research what exists before imposing the desired structure.

The [task-assignment example](../examples/task-assignment/README.md) contains connected filled artifacts. They remain illustrative and do not impersonate a client's approval. The [customer-outcome example](../examples/customer-outcome/README.md) demonstrates where software may not be the first intervention.
