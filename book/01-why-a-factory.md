# 1. Why a factory?

[Reading guide](../READING-GUIDE.md) · [Start here](../README.md) · [Next: The perspectives and the tensions](02-the-perspectives-and-tensions.md)

> **Status:** Proposed synthesis, with attributed sources. Illustrations are not client results.

## The problem behind the project

This investigation began with a practical contradiction. Coding agents can produce a large amount of implementation while leaving an experienced engineer with a large amount of work: checking behavior, reconstructing intent, untangling boundaries, correcting assumptions, and determining whether the result can safely be maintained. Faster production does not, by itself, resolve that contradiction.

Sabir's starting perspective combines hands-on development with extensive agent delegation. He values both the speed of agents and the work of engineering. He does not want a return to approving every line. He also does not want to inherit systems whose apparent speed depends on someone else absorbing the maintenance cost later. The desired increase in capacity is personal and practical: undertake more worthwhile client work without becoming the permanent supervisor of every implementation detail.

This book is an AI-assisted editorial synthesis of that investigation, not a verbatim transcript or a claim that every proposed mechanism has already worked. The original questions and the evolution of the answers remain discoverable in the [research map](../research/questions-and-coverage.md). The purpose is to make the reasoning useful to other engineers without asking them to replay a long conversation.

## A change in the unit of progress

At first, the factory can appear to be a system for producing code. Zoom out once and it becomes a system for completing features. Zoom out again and it becomes a system for delivering reliable changes. One more level exposes the real objective: helping people accomplish something worthwhile.

![The levels of the problem: customer outcome, behavior, engineering decisions, execution, and evidence.](../diagrams/rendered/01-levels.png)

*This is a conceptual hierarchy, not a requirement to execute five sequential phases. Evidence must be able to change decisions at every level.*

Suppose a customer requests an AI assistant. Producing a working chat interface satisfies a construction task. It does not establish that the customer's staff can now find reliable information, make fewer mistakes, or complete work faster. The right intervention might be a better search experience, a corrected data feed, a changed operating procedure, or a smaller application. A useful factory must remain capable of recommending those alternatives.

We therefore propose a different objective: increase valuable, reliable change that can be delivered and sustained without a proportional increase in unnecessary human attention. This is a direction for evaluation, not a single numerical score. Customer value, safety, delivery time, attention, and future change cost are different quantities. Collapsing them prematurely into one number can hide a serious failure behind an improvement elsewhere.

## Human attention is not all the same

Reducing human involvement indiscriminately would be a mistake. Time spent discovering what a client actually needs is not equivalent to time spent reconstructing an agent's confusing pull request. Time spent resolving a consequential ownership decision is not equivalent to repeatedly explaining the same naming convention.

The factory should move attention toward work where judgment changes the outcome. That includes understanding a difficult domain, recognizing an inappropriate product direction, choosing a security boundary, or deciding that a risky release should not proceed. It should reduce repeated reconstruction, mechanical correction, and decisions that a stable contract can settle.

This distinction also prevents an unrealistic promise. A capable engineer is not merely an approval service that can be removed once prompts improve. Some of the most valuable work consists of noticing that the stated problem is incomplete. An operating model that suppresses such involvement may increase the speed of execution while reducing the quality of decisions.

## What the factory metaphor helps us see

The metaphor directs attention toward repeatable work, explicit interfaces, quality controls, and accumulated capability. A good module generator can preserve an established boundary. An authorization policy inventory can make an omission visible. A reference slice can communicate conventions more precisely than repeated reminders. A review capability can present evidence in a form someone can understand.

But software work is not simply repeated assembly of identical units. Requirements change, integration constraints surprise us, and the meaning of success must often be discovered. We should standardize mechanisms that support learning, not assume that the learning itself can be standardized away.

DORA's account of small batches emphasizes feedback and revising assumptions, rather than treating a plan as a guarantee of the right result. We use that as support for short delivery loops, not as empirical proof of this particular factory. [S11](../research/sources/index.md#s11)

## The three kinds of debt we are trying not to create

Implementation debt appears when the code becomes difficult to change. Decision debt appears when consequential choices were never made explicitly, so every later feature must rediscover them. Understanding debt appears when no one can efficiently explain the system or inspect why a decision was made.

These are working categories introduced by this publication. They overlap. A shared database table with several undocumented writers may create all three. The categories help locate an intervention: a type or boundary rule may address implementation debt; a short decision record may address decision debt; a grounded system view may address understanding debt.

Documentation alone does not resolve all three. Nor does code alone. The goal is to put each important piece of knowledge where it can guide action and, where possible, be checked.

## A factory should be able to refuse unnecessary work

Consider three responses to a feature request. The first implements immediately. The second writes a comprehensive specification before implementing. The third identifies the uncertain assumption that determines whether implementation is worthwhile, then runs a small experiment. Any of the three may be appropriate. The third is not automatically superior; sometimes the request is clear and low risk. The point is that the operating model must have more than one response.

Success may mean shipping a feature. It may mean avoiding an unnecessary feature. It may mean discovering that the data or organizational process needs attention first. This is why the customer-value loop must surround the engineering-delivery loop.

## What would count as progress?

A credible first improvement would be narrower than a claim of autonomous software engineering. For comparable changes, we might see less rework, fewer avoidable explanations, and less time spent finding where a change belongs, while preserving acceptance quality and release safety. Later changes in the same area should not become disproportionately difficult.

We also need to count setup and maintenance of the factory itself. Building elaborate tools that save a few minutes on a task performed once is not obvious leverage. A recurring class of mistakes, a repeated review burden, or a capability reused across projects is a stronger reason to invest.

This leads to the central question of the book: how can engineering judgment become reusable without freezing assumptions, and how can autonomous work remain accountable without turning every task into bureaucracy? The following chapters develop a proposed answer and a way to challenge it.

## The practical implication

Before designing agent roles, identify one customer workflow, one representative delivery task, and the current human effort needed to get it right. That gives the factory something real to improve. The objective is not to remove the engineer. It is to stop paying repeatedly for the same understanding and the same correction.

---

[Start here](../README.md) · [Next: The perspectives and the tensions](02-the-perspectives-and-tensions.md)
