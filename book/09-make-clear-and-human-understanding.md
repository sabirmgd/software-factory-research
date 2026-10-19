# 9. Make Clear and human understanding

[Reading guide](../READING-GUIDE.md) · [Previous: Bounded autonomy and agent sessions](08-bounded-autonomy-and-agent-sessions.md) · [Next: Verification and safe delivery](10-verification-and-safe-delivery.md)

> **Status:** Proposed. The original local Make Clear implementation was not retrieved; this chapter describes the capability developed in this publication.

## The problem is reconstruction

A technical review often starts long before the decision.

The reviewer must find the relevant code, rebuild the system in their head, separate current behavior from proposed behavior, identify important omissions, and decide which evidence to trust. Only then can they judge the change.

Make Clear tries to reduce that reconstruction work.

Its purpose is not to generate diagrams. Its purpose is to help someone accurately understand something important with less effort.

## Start with the question

The right representation depends on what the person needs to understand.

- A short explanation may settle a simple distinction.
- A sequence diagram may reveal when authorization and persistence occur.
- A before-and-after dependency view may expose new coupling.
- A state table may clarify allowed and denied transitions.
- A small prototype may reveal whether an interaction makes sense.

Producing every possible view creates another review burden. Use the smallest representation that answers the question, then state what it leaves out.

HumanLayer's inspected `show-me` skill also chooses among focused representations. This Make Clear proposal adds explicit uncertainty, evidence pointers, and support for understanding without requiring approval. [S20](../research/sources/index.md#s20)

## A concrete example

“Explain the task-reassignment change” is too broad.

A better question is:

> Does this change alter who can see a task, including the important denied cases?

A useful answer could contain:

1. one sentence stating that reassignment does not grant visibility;
2. a small flow showing identity, workspace membership, task visibility, eligibility, and the denied result;
3. links to the policy code and tests; and
4. one unresolved assumption about membership changing during the transaction.

That is enough to support a focused review. It does not need a map of the entire application.

## Good architecture and good explanation solve related problems

Good architecture hides details a developer should not need. A good explanation hides details a reviewer should not need.

Neither may hide important risk.

A module can conceal a dangerous side effect. A diagram can omit the failure path that decides whether the design is acceptable. Simplicity helps only when the remaining interface preserves the obligations and consequences that matter.

After reading a Make Clear view, ask:

> What can the person now understand, and what important surprise is still possible?

## Label three information states

Keep these states visible when they affect the conclusion:

- **Observed:** established from inspected source or executed behavior.
- **Proposed:** intended future behavior or structure.
- **Unverified:** assumed or claimed but not yet established.

For example, code may show that an endpoint checks membership. The claim that membership remains valid throughout the commit may still be unverified.

A diagram that draws both with identical confidence hides the difference. Use a caption, annotation, or separate line of text.

Evidence also belongs to a revision and environment. A prototype screenshot is not production proof. A test result supports the code and environment that actually ran.

## Show consequences, not decorative boxes

A box labeled “Authorization” says little.

When access is the question, show where identity comes from, which resource context is used, which rule is checked, and what the caller learns when access is denied.

When comparing product choices, show what changes for the user. When comparing architectures, show where a likely future change would go. When explaining a release, show who is exposed, what is monitored, and what recovery cannot undo.

Make Clear should challenge a flawed premise rather than make it visually persuasive. The challenge should name the assumption, explain its consequence, and point to evidence or a way to test it.

## Use it where understanding is the bottleneck

Make Clear can help during:

- **research:** map the current system and distinguish known from inferred boundaries;
- **discovery:** compare journeys, states, or product choices;
- **design:** show ownership, interfaces, alternatives, and failure paths;
- **implementation review:** explain what changed and connect it to evidence; and
- **learning:** show recurring friction across several changes.

Do not generate a visual report merely because a template has a diagram field. A familiar change may need only two clear paragraphs.

Understanding and authority remain separate. Understanding a design does not authorize deployment. Producing an explanation does not create a new approval gate.

## Make views usable

Use short labels, readable type, meaningful captions, and focused layouts. Avoid enormous posters that require zooming. Do not use color as the only carrier of meaning. Provide a text alternative and a route back to source material.

This repository keeps canonical graph data plus SVG and PNG outputs so the concepts remain readable across viewers. [S21](../research/sources/index.md#s21)

## Guard against false confidence

A polished explanation may increase confidence without improving correctness. It can select convenient evidence, become stale, or hide a detail that would be obvious in a diff.

Keep the evidence accessible. Include important failure paths. Label uncertainty. Evaluate whether reviewers detect the right issues, not only whether they prefer the presentation.

> **Do not confuse:** a clear explanation with proof that the explained system is correct.

## What to do next

For the next difficult review:

1. Write the exact question the reviewer must answer.
2. Choose one representation that reduces the most reconstruction.
3. Show the important consequence and failure path.
4. Label observed, proposed, and unverified information where needed.
5. Link back to the evidence.

Success is accurate understanding with less effort—not more diagrams.

---

[Previous: Bounded autonomy and agent sessions](08-bounded-autonomy-and-agent-sessions.md) · [Next: Verification and safe delivery](10-verification-and-safe-delivery.md)
