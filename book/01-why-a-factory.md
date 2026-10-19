# 1. Why a factory?

[Five-minute version](../START-HERE.md) · [Reading guide](../READING-GUIDE.md) · [Next: The perspectives and the tensions](02-the-perspectives-and-tensions.md)

> **Status:** Proposed. The examples are illustrative, not client results.

## The short version

AI agents can write code faster than an engineer can safely review it. If every change still requires the engineer to reconstruct the problem, inspect unfamiliar decisions, correct the same mistakes, and explain the same rules, code generation has moved the bottleneck rather than removed it.

The factory is an attempt to solve that problem. It makes important judgment reusable, gives agents room to work inside clear boundaries, connects claims to evidence, and learns from repeated friction.

The goal is not more code. The goal is more useful, reliable change without a matching increase in supervision or future maintenance.

## Start with the work people need to do

A feature request is not yet a customer outcome.

Suppose a customer asks for “task reassignment.” A fast implementation could add an assignee field, an endpoint, and a dropdown. But the customer may actually need supervisors to redistribute urgent work without exposing tasks to the wrong people or losing the audit trail.

That difference matters. The requested feature describes a possible solution. The outcome describes what should improve for a person and what must not get worse.

The best intervention may still be software. It may also be a smaller change, a corrected data feed, a search improvement, or a process change. A useful factory must be allowed to discover that the requested feature is not the right answer.

## Change the unit of progress

It is easy to measure generated code, completed tickets, or active agents. Those are production signals, not proof of value.

Zoom out through five levels:

1. Code was produced.
2. The code behaves as intended.
3. The change is safe to release and maintain.
4. People can use it in their real work.
5. Their work improves without unacceptable harm elsewhere.

![The levels of the problem: customer outcome, behavior, engineering decisions, execution, and evidence.](../diagrams/rendered/01-levels.png)

These are not five mandatory phases. They are five different claims. Evidence at a lower level does not automatically prove a higher one.

> **Do not confuse:** a completed implementation with an improved customer outcome.

## Protect valuable human attention

The factory should not remove human involvement indiscriminately. Some attention changes the outcome; some attention merely repairs avoidable confusion.

High-value attention includes understanding a difficult domain, choosing a security boundary, noticing that the stated problem is incomplete, or deciding not to release a risky change.

Low-value repetition includes rediscovering the same naming rule, finding the same authorization entry point, correcting the same missing test, or reconstructing an agent's unexplained pull request.

The aim is to preserve the first kind and reduce the second. An experienced engineer is not an approval service. Their greatest value may be recognizing that the team is solving the wrong problem.

## Avoid three kinds of debt

This book uses three working categories:

- **Implementation debt:** the code is hard to change safely.
- **Decision debt:** important choices were left implicit, so later work must rediscover them.
- **Understanding debt:** people cannot quickly explain the system, the reason for a decision, or the evidence behind a claim.

One problem may create all three. An undocumented shared database table can make changes risky, hide ownership, and force every contributor to investigate the same questions.

Code alone cannot remove every kind of debt. Documentation alone cannot either. Important knowledge should live where it can guide action and, when possible, be checked automatically.

## Let the factory refuse unnecessary work

A request can lead to several responsible actions:

- implement it because the need and risk are already clear;
- clarify product or technical decisions first;
- run a small experiment because one assumption determines whether the work is worthwhile; or
- recommend a non-software solution.

None is always correct. The important point is that “build immediately” is not the only available route.

DORA's discussion of small batches supports short feedback loops and revising assumptions. It does not prove this particular factory model. [S11](../research/sources/index.md#s11)

## What progress would look like

A credible early result is modest. For similar changes, the engineer should spend less time on avoidable explanation, rework, and navigation while acceptance quality and release safety stay at least as strong. Later changes in the same area should not become disproportionately harder.

Factory work also has a cost. A generator, template, or guardrail is not leverage merely because it is reusable. Count the effort to design, maintain, explain, and handle exceptions. Invest when the same costly problem appears repeatedly, not whenever an abstraction is possible.

## What to do next

Before designing agent roles or orchestration, choose:

1. one real customer workflow;
2. one representative change;
3. the human effort currently needed to deliver it safely; and
4. the repeated confusion or correction you want to reduce.

That gives the factory something real to improve. The goal is not to remove the engineer. It is to stop paying repeatedly for the same understanding.

---

[Five-minute version](../START-HERE.md) · [Next: The perspectives and the tensions](02-the-perspectives-and-tensions.md)
