# Technical design document

**Reusable template.** Use for consequential technical uncertainty. TDD here means technical design document, not test-driven development. Small known-pattern changes can use a compact design note.

[Template guide](../README.md) · [Filled or worked reference](../../examples/task-assignment/technical-design.md)


## Inputs and status
Link use cases, product decisions, current research, repository revisions, and existing architecture contracts. Distinguish approved decisions, proposals, and unknowns.

## System design
Describe component interactions, boundaries, data ownership, API or event shapes, persistence and transactions, identity and resource authorization, failure/retry semantics, and operational constraints. Explain how this change fits the established system.

Show the smallest useful interaction or data-flow view. Identify what the view omits. Compare structurally different options when the decision is consequential; do not generate ceremonial alternatives for a settled pattern.

System-design decision: [pending / accepted by ... on ...]. Record required changes to upstream product meaning.

## Program design
Write caller usage first, then public types, signatures, dependency direction, key state ownership, and private responsibilities. Include a focused file-tree delta or call sequence if it exposes a decision. Avoid committing to every helper before implementation teaches anything.

Program-design decision: [pending / accepted by ... on ...]. Define which internal refinements can proceed without approval and which public-contract changes must return to review.

## Evidence and release plan
Map significant claims to checks. Name type/build constraints, behavior tests, integration evidence, negative cases, architecture fixtures, observability, and recovery. Describe what remains outside the evidence.

## Pressure and next steps
State likely future changes, design risks, unresolved owners, and the next increment. Repeated deviations trigger investigation, not automatic redesign.
