# 9. Make Clear and human understanding

[Reading guide](../READING-GUIDE.md) · [Previous: Bounded autonomy and agent sessions](08-bounded-autonomy-and-agent-sessions.md) · [Next: Verification and safe delivery](10-verification-and-safe-delivery.md)

> **Status:** Proposed synthesis, with attributed sources. Illustrations are not client results.

## The hidden work in human review

A technical review often begins before the reviewer reaches the actual decision. They must reconstruct the system from prose, code, diagrams, and changes; identify which details are relevant; distinguish existing behavior from a proposal; and decide what evidence to trust. Only then can they evaluate the work.

Make Clear began from Sabir's objection to that reconstruction burden. Text alone is sometimes an inadequate interface between an agent's work and a person's understanding. The goal is broader than approval. Someone may want to learn a system, explore an idea, compare consequences, or challenge an assumption without making any decision yet.

This chapter specifies that perspective as a proposed factory capability. It does not claim that the original local Make Clear skill was retrieved or verified. Available evidence establishes the user's intent; the implementation described here is a new, explicit design proposal. The [source-correction record](../research/source-corrections.md) preserves that limitation.

## Understanding is the product of the capability

A diagram is not automatically clearer than prose. A short explanation may be best for a simple distinction. A sequence diagram may reveal the timing of authorization and persistence. A before-and-after dependency view may reveal a new coupling. A state explorer may expose a rule that is hard to reason about statically. A UI prototype may help someone recognize an unexpected interaction.

The representation should follow the question. Producing every possible view creates another reconstruction task. The capability should select the smallest useful view and explain what it leaves out.

HumanLayer's inspected `show-me` skill likewise selects among code-shape sketches, call trees, diffs, diagrams, and focused HTML views. Our Make Clear design extends that mechanism with explicit uncertainty, evidence provenance, and support for understanding without approval. [S20](../research/sources/index.md#s20)

## Architecture and explanation reduce different kinds of context

A well-designed module reduces the internal knowledge a caller needs in order to act correctly. A grounded explanation reduces the material a reviewer needs to reconstruct in order to understand or judge. These are analogous goals, not identical mechanisms.

Both can fail by hiding the wrong thing. A module can conceal a dangerous side effect. A diagram can omit the failure path that determines whether a design is acceptable. Simplicity is useful only when the remaining interface preserves the obligations and consequences that matter.

This suggests a review question for Make Clear: after reading the view, what can the person understand or decide, and what important uncertainty would still surprise them?

## The input and output contract

The input should identify the question, audience, relevant artifacts, revision or state, known uncertainty, and whether a decision is being requested. “Explain the PR” is broad. “Show whether this PR changes who can see an assignment, including denied cases” is focused.

The output should include a view or explanation, the important consequence, evidence pointers, unresolved assumptions, and any requested decision. It should not fabricate an approval where none is required. It should not replace the governing product or technical artifact with a disconnected summary.

![Make Clear transforms source material into an inspectable view while preserving evidence and uncertainty.](../diagrams/rendered/06-make-clear.png)

*The view is derived from evidence or an explicitly labeled proposal. It is not verification by itself.*

## Three information states

An observed statement is grounded in an inspected source or executed behavior. A proposed statement describes an intended change. An unverified statement is an assumption or claim that has not yet been established. These labels should remain visible in the output, especially when a diagram combines existing and planned components.

For example, “the endpoint checks membership” may be observed in code, while “membership remains valid throughout the transaction” may still be unverified. A diagram showing both with identical arrows can conceal the distinction. A caption or visual annotation should make the gap explicit.

Evidence is also revision-specific. A before-and-after view should identify the baseline and proposed revision. A screenshot from a prototype is not proof that production behaves that way. A test result applies to the environment and code that actually ran.

## Show consequences, not only structure

A box labeled Authorization may tell a technical reader very little. A flow showing the source of identity, the resource's tenant, the permission check, and the denied result is more useful when the question concerns access.

For a product decision, compare the user-visible consequence of two alternatives. If assignment grants access in one design but not another, demonstrate the difference with an external collaborator. For architecture, show where a future provider change would be implemented under each option. For release, show what is exposed, what is monitored, and what can and cannot be reversed.

The capability should challenge the premise when necessary. It should not make a flawed proposal visually persuasive simply because the proposal was requested. Challenge should be specific, grounded, and tied to the user's goal.

## Where it fits in the workflow

During research, Make Clear can map the current system and distinguish known boundaries from inferred ones. During discovery, it can compare journeys or state transitions. During technical design, it can show interfaces and alternatives. During implementation review, it can explain the actual change and connect it to evidence. During learning, it can reveal a recurring pattern of friction.

It should be callable at any of these points. A high-impact decision may trigger it automatically as preparation for review. A small familiar change should not generate a visual report merely because a template contains a diagram field.

Understanding and authority remain separate. A person understanding a design does not automatically authorize deployment. An agent producing a view does not automatically require a person to approve it.

## Phone-friendly and accessible views

Use short labels, readable type, meaningful captions, and layouts that do not require zooming into an enormous poster. Favor several focused views over a dense omnibus diagram. Do not encode essential meaning through color alone. Provide text alternatives for images and a route back to the source artifacts.

This repository keeps canonical graph data, Mermaid exports, and rendered SVG/PNG views. The rendered images make the concepts readable without depending on a particular chat client's diagram support. GitHub's Markdown supports Mermaid, but other viewers may differ. [S21](../research/sources/index.md#s21)

## What could make this fail?

A polished explanation can increase confidence without increasing correctness. Selection of evidence can hide relevant disagreement. A generated diagram can become stale. A prototype can be mistaken for a working product. A visual reviewer may overlook details that would have been obvious in a diff.

The remedy is not to abandon visualization. It is to keep evidence accessible, label uncertainty, include consequential failure paths, and evaluate the effect on review quality as well as review time. The [Make Clear experiment](../experiments/hypotheses.md) therefore examines misunderstandings found and missed, not simply whether reviewers prefer the visual presentation.

## The practical implication

Treat Make Clear as the human-understanding interface of the factory. Its success is a person accurately understanding something important with less reconstruction—not the number of diagrams generated or approvals obtained.

---

[Previous: Bounded autonomy and agent sessions](08-bounded-autonomy-and-agent-sessions.md) · [Next: Verification and safe delivery](10-verification-and-safe-delivery.md)
