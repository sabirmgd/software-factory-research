# 2. The perspectives and the tensions

[Reading guide](../READING-GUIDE.md) · [Previous: Why a factory?](01-why-a-factory.md) · [Next: Our working model](03-our-working-model.md)

> **Status:** Proposed synthesis, with attributed sources. Illustrations are not client results.

## Comparison without flattening the differences

It is tempting to assemble a process by taking the most appealing sentence from every author. That creates agreement cheaply, but may produce a workflow no source would recommend and no team can comfortably operate. We instead compare the problem each mechanism addresses, its default behavior, and the circumstances in which we would change it.

The sources below are separate projects and bodies of work. They are not interchangeable brands for a single approach. Their inclusion does not imply endorsement of this publication. Version-sensitive skill behavior is recorded in the [source ledger](../research/sources/index.md), including content identifiers where retrieved.

## Dex Horthy and HumanLayer: make consequential design inspectable

HumanLayer's RPI workflow distinguishes findings about the current system from decisions about a proposed change. It offers multiple routes after research: a combined design discussion, product requirements, technical design, or implementation. Its technical-design process separates system interactions from program structure and obtains approval for each. Documents carry the decisions between sessions. These are concrete workflow instructions, not merely a generic suggestion to plan. [S01–S03](../research/sources/index.md#s01)

For our purposes, the value is the separation of intent, technical choices, and execution. It helps expose decisions an agent might otherwise make silently. The cost is interaction and artifact maintenance. We adopt the distinctions but not a requirement to create every document for every feature. Where a known pattern already answers the questions, a compact change brief can be enough.

There is an important historical correction. The older `humanlayer/humanlayer` repository now describes its code as deprecated. Its past command files are historical material, not our recommended current implementation base. The newer skills repository is the workflow source examined for this edition. [S04](../research/sources/index.md#s04)

## Matt Pocock: alignment, experiments, and composable practices

Matt's skills repository favors small, adaptable practices rather than a process that owns every development decision. The prototype skill distinguishes questions about state or logic from questions about interface design. It treats prototype code as disposable and records the learning separately from production implementation. The `to-spec` skill synthesizes an existing conversation into a specification that includes implementation and testing decisions. [S05–S07](../research/sources/index.md#s05)

This corrects an overly simple comparison from the conversation. It is not accurate to say Matt only handles product clarification while Dex handles technical design. Their artifacts overlap. The useful distinction is where information is captured and how a user composes the workflow.

We adopt bounded experiments and shared domain language. We do not make every feature wait for a prototype or an extended interview. A prototype must have a question, a small scope, and a verdict. Producing something visually impressive without settling the uncertainty is not success.

## Poteto's PStack: design for the contributor who sees only part of the system

PStack's architect skill starts with grounding, explores structurally distinct designs, compares interfaces, and implements against a chosen sketch. It explicitly revisits a design when recurring workarounds reveal a pattern. Its human checkpoint is opt-in. The related `correct` skill favors removing recurring error classes through structure, types, checks, and tests before relying on more prose. [S08–S10](../research/sources/index.md#s08)

The particularly useful lens is the partial view of the next contributor. A person or agent may see one file, copy the nearest example, and choose the shortest apparent path. Our proposed architecture should make that path more likely to preserve the larger system's obligations.

We adopt caller-first sketches, meaningful alternatives, and correction through enforceable structure. We modify the approval default for our client work: a task may proceed inside an approved scope, but changing tenant isolation, data ownership, external commitments, or other consequential boundaries requires explicit authority. That modification is ours, not a description of PStack's default.

## Uncle Bob: protect the business rules from incidental mechanisms

Robert C. Martin's Clean Architecture describes dependency direction that keeps business rules from depending on delivery and persistence details. This offers a design principle, not a PRD or agent-session format. It helps us ask whether a change to a framework or database representation unnecessarily spreads into core behavior. [S14](../research/sources/index.md#s14)

We adopt that principle where it improves separation. We reject ceremonial interpretation: a controller, service, manager, processor, repository, and facade do not create maintainability merely by existing. A boundary must hide a relevant decision, adapt a real difference, or protect a useful invariant.

The conversation also referenced an interview with Matt. This edition does not rely on an unverified transcript for specific claims about that interview. Established written sources and the separately inspected skills carry the claims we can support. The unresolved attribution is preserved in the [correction record](../research/source-corrections.md).

## John Ousterhout: depth is hidden complexity, not a long call chain

Ousterhout's work supplies the deep-module lens: a useful interface should relieve callers of meaningful complexity. We use the author's book page as the primary bibliographic reference, not as evidence that the complete book was retrieved for this edition. The author also identifies disagreements with Clean Code; we do not erase those disagreements by presenting a unanimous school. [S15](../research/sources/index.md#s15)

For our synthesis, a deep task-assignment capability would own the rules required to perform assignment correctly. It would not require every caller to sequence membership checks, writes, audit creation, and notification decisions manually. This is our illustrative application of the lens. Depth does not mean one enormous object with an unbounded responsibility. It means the public contract saves the caller from learning internal coordination.

## Where the tensions actually matter

| Tension | Useful mechanism | Our proposed choice |
| --- | --- | --- |
| Planning versus learning by implementation | Design documents and disposable experiments | Resolve consequential uncertainty before committing; refine detail in short loops |
| Autonomy versus accountability | Agent initiative and explicit checkpoints | Preauthorize routine work; escalate changes to authority or durable boundaries |
| Standardization versus adaptability | Generators and composable skills | Standardize repeatable plumbing, not every project decision |
| Prevention versus repair | Types, checks, regression tests, redesign | Prevent known failure classes; investigate patterns rather than patch forever |
| Simplicity versus inspectability | Small interfaces and concrete design views | Hide implementation complexity without hiding consequences or evidence |

These are not compromises that split every difference. They are conditional choices. For a trivial copy edit, architectural alternatives are waste. For a new sharing model, skipping a discussion because an agent can implement quickly is false economy. For a one-off report, a general plugin platform may be needless. For a repeated integration across several products, a stable adapter capability may be valuable.

## What the comparison does not establish

The number of prominent sources favoring a practice does not demonstrate its effectiveness in our environment. Nor does consistency between their ideas prove that combining all of them reduces effort. A process can be composed of individually sensible mechanisms and still impose excessive coordination.

The comparison therefore produces hypotheses and design options. The [experiments](../experiments/hypotheses.md) examine whether the selected mechanisms help on actual work. We should be willing to remove a borrowed practice when its local cost exceeds its benefit, even when we admire its author.

## The practical implication

Borrow mechanisms together with their reasons and failure modes. When a practice enters the factory, record the recurring problem it is supposed to solve, the authority it requires, the evidence it expects, and the circumstances under which it should be skipped. That is more useful than maintaining a collection of admired names.

---

[Previous: Why a factory?](01-why-a-factory.md) · [Next: Our working model](03-our-working-model.md)
