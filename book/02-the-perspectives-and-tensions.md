# 2. The perspectives and the tensions

[Reading guide](../READING-GUIDE.md) · [Previous: Why a factory?](01-why-a-factory.md) · [Next: Our working model](03-our-working-model.md)

> **Status:** Source-backed comparison followed by this book's proposed choices.

## Why compare these sources?

This model did not appear from one method. It combines ideas from several bodies of work that solve different problems.

The useful question is not “Which author is right?” It is:

> What problem does this idea solve, what does it cost, and when should we use it?

The sources do not form one agreed methodology, and their inclusion does not imply that their authors endorse this book.

## The ideas in plain language

| Source | Useful idea | Risk if applied mechanically |
| --- | --- | --- |
| HumanLayer / Dex Horthy | Separate research, product decisions, technical design, and implementation so agents do not make important decisions silently. | Every change can become a paperwork exercise. |
| Matt Pocock | Use focused experiments and composable practices instead of one mandatory workflow. | Small experiments can be mistaken for proof of the whole system. |
| Poteto's PStack | Design and document for contributors who see only part of the codebase. | Local simplicity can hide problems that cross module boundaries. |
| Robert C. Martin | Keep business rules from depending directly on frameworks and delivery mechanisms. | Layering can become ceremony with no real change protection. |
| John Ousterhout | Prefer deep modules: small interfaces that hide substantial coordination. | A small interface can hide dangerous behavior as easily as useful complexity. |

## HumanLayer: expose decisions before code hides them

HumanLayer's inspected RPI material separates findings about the current system from decisions about the proposed change. It offers several routes: research, product requirements, technical design, or implementation. The technical design distinguishes system interactions from program structure. [S01–S03](../research/sources/index.md#s01)

We keep the separation because it prevents agents from silently deciding product behavior or architecture. We do not require every artifact for every task. A familiar, low-impact change may need only a compact brief and targeted evidence.

## Matt Pocock: use the smallest experiment that answers the question

The inspected material emphasizes alignment, bounded experiments, and practices that can be composed according to the task. [S04](../research/sources/index.md#s04)

We adopt the idea that an experiment should answer one uncertainty. For task reassignment, a small type or state model may reveal whether assignment and access are being confused. That experiment is useful without pretending it is the production feature.

## PStack: help the contributor who sees only part of the system

PStack's inspected material treats repository guidance, examples, and checks as tools for contributors working with partial context. [S05–S07](../research/sources/index.md#s05)

That fits agent work well. An agent should not need the entire history of a company to add one safe operation. But local guidance must still point to wider product, security, and data rules when those rules matter.

## Clean Architecture: protect business rules from incidental mechanisms

The inspected Clean Architecture material argues for dependency direction that keeps business policy independent from frameworks, databases, and delivery details. [S08–S10](../research/sources/index.md#s08)

We keep the principle and reject ceremonial layering. If a domain operation can be tested without a web framework or database, future changes are easier to reason about. Extra interfaces that merely forward calls do not create the same benefit.

## Ousterhout: hide complexity behind useful interfaces

Ousterhout's deep-module idea asks whether an interface saves callers from understanding substantial internal coordination. [S14](../research/sources/index.md#s14)

For task reassignment, a useful operation may own authorization, eligibility, concurrency, persistence, and audit behavior behind one clear contract. “Deep” does not mean a large class or long call chain. It means the interface is simpler than the responsibility it manages.

## The real tensions

The sources become useful when their tensions are visible:

- **Planning versus feedback:** design enough to avoid expensive mistakes, then let implementation provide better evidence.
- **Local context versus system context:** make one change area understandable without hiding cross-cutting obligations.
- **Separation versus ceremony:** protect important business rules without creating layers that add no value.
- **Small interfaces versus hidden danger:** hide internal detail, but expose side effects, permissions, and failure behavior.
- **Reusable practice versus local fit:** promote a pattern after repeated value, not merely because it can be generalized.

The book also draws on feedback, flow, and customer-outcome material from DORA and related sources. Those sources support parts of the model; they do not establish that the combined model works. [S15](../research/sources/index.md#s15)

## What this comparison proves—and does not prove

The comparison explains where the proposed mechanisms came from and why they were selected. It does not prove that combining them improves delivery, customer value, or maintainability.

That requires experiments on real changes, including setup cost, review effort, escaped defects, later change cost, and customer results.

## What to do with these ideas

For each practice, ask four questions:

1. What recurring problem does it solve?
2. What is the smallest form that could help?
3. What new work or failure mode does it introduce?
4. What evidence would justify keeping, changing, or removing it?

Use the source as a tool, not as a badge. The factory should be coherent because its choices fit the problem, not because it collected respected names.

---

[Previous: Why a factory?](01-why-a-factory.md) · [Next: Our working model](03-our-working-model.md)
