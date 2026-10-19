# 3. Our working model

[Reading guide](../READING-GUIDE.md) · [Previous: The perspectives and the tensions](02-the-perspectives-and-tensions.md) · [Next: Discovery and product intent](04-discovery-and-product-intent.md)

> **Status:** Proposed synthesis, with attributed sources. Illustrations are not client results.

## A learning system with a production capability

A software factory that only implements approved requests can be very efficient at preserving a mistaken assumption. A factory that only discovers valuable problems can leave them poorly implemented. A factory that does both but never improves its own operation can keep the engineer permanently overloaded.

Our working model has three connected feedback loops. They are not three departments or three agents. A small task may traverse them in a single session; a larger product may involve many people and tools. The distinction concerns the question being answered.

![Three connected loops: customer value, engineering delivery, and factory learning.](../diagrams/rendered/02-three-loops.png)

*The model is a proposed synthesis. The arrows describe information that should change decisions, not proof that the process is effective.*

## The customer-value loop

This loop asks whether the problem is worthwhile and whether the intervention helps. Its inputs include customer observations, operating constraints, requested changes, and evidence from existing behavior. Its output is not necessarily a feature list. It may be a revised hypothesis, a smaller scope, a decision to fix data, or a decision not to build.

A minimal outcome hypothesis names the affected people, the work they are trying to perform, the present difficulty, and how improvement will be evaluated. It also names what must not get worse. Reducing the time to send a quote would not be useful if it increased quoting errors or disclosed information to the wrong customer.

DORA's customer-feedback guidance links product decisions to evidence about customer interaction and adoption. Our extension is to make that feedback a first-class boundary around agent execution, rather than treating it as an optional activity after delivery. [S13](../research/sources/index.md#s13)

## The engineering-delivery loop

This loop asks how to make the accepted change safely and maintainably. It contains research, design, implementation, verification, and release. The depth of each activity depends on the change, not on a fixed ceremony.

The durable foundation consists of current product meaning, module contracts, allowed dependencies, security intent, reference patterns, and executable checks. A feature-specific design derives from that foundation. It does not re-create the entire architecture, and it cannot silently discard an inconvenient rule.

The result is a bounded, inspectable change with evidence. The evidence may justify a merge, a preview deployment, or a further experiment. Those are distinct permissions. Passing tests does not automatically authorize a production rollout.

## The factory-improvement loop

This loop asks why the work required its particular effort and what should change next time. It draws on repeated review comments, failed checks, surprising dependencies, unclear domain terms, waiting time, and outcome observations.

It should improve the right layer. Repeated unknown permission names may call for a typed registry. Repeated confusion about who a customer is may call for a domain-language decision. Repeated deployment delays may reveal missing authority or an unavailable test environment. Repeated client rejection may mean the solution was validated too late.

The loop must also remove unnecessary machinery. A guardrail that consistently blocks legitimate work may need redesign. A template field no one uses may need deletion. A shared abstraction used once may not belong in the foundation. The factory itself is software and process that must be maintained.

## Four capabilities operating across the loops

Human engineering supplies intent and consequential judgment. Autonomous execution performs bounded investigation and implementation. Verification establishes evidence about specific claims. Make Clear turns the relevant material into a form someone can understand and challenge.

Make Clear is not a fourth sequential stage. It may help during discovery, technical design, debugging, review, or learning. It does not automatically create a human approval requirement. Someone can use it simply to understand a system, and an already authorized change can remain autonomous even when a visual record is produced.

Likewise, research is not restricted to the beginning. An agent may discover an unknown during implementation. A bounded investigation can resolve it without reopening every decision. If the finding changes product intent or a foundational boundary, the workflow must return to the relevant decision owner.

## The contract connecting human judgment and autonomous action

We propose that a delegated work item carry six pieces of information: desired outcome, approved scope, stable constraints, required evidence, permitted actions, and escalation conditions. These need not be six new files. They can be six short sections of one work item.

This turns the vague instruction “use your judgment” into something operational. The agent may refactor private code within a module, but may not change its public authorization behavior. It may run a preview with synthetic data, but may not contact real customers. It may propose a new dependency, but may not introduce a recurring paid service under an existing feature approval.

A missing decision is not a blank check. Nor should every small unknown become a question to the human. The distinction is whether resolving it would exceed the task's authority or change a consequential contract.

## Leverage as a hypothesis about repeated work

We use leverage to mean that an investment improves more than one later action. A generator can encode a known structure. A precise module contract can reduce discovery work. A runtime deny-by-default mechanism can prevent a class of omissions. A grounded visual can reduce the reconstruction needed for review.

The investment has costs: initial design, ongoing maintenance, exceptions, and the risk of enforcing a wrong default. Therefore “more reusable” is not automatically better. A useful factory accumulates validated capabilities, not every abstraction an agent can imagine.

An approximate evaluation can separate setup effort from recurring effort. Count the attention needed to clarify, implement, verify, and support comparable changes before and after introducing a mechanism. Then observe subsequent changes in the same area. We do not claim a universal formula converts those observations into a definitive factory score.

## Flow matters more than agent utilization

If implementation produces changes faster than a team can evaluate them, unfinished work accumulates. A factory dashboard should show blocked decisions, waiting reviews, unavailable test environments, and unresolved customer questions—not just active agents.

DORA's work-in-process guidance emphasizes the complete value stream and addressing its constraint. We adapt that reasoning by allowing agents to stop starting new review-heavy work when downstream capacity is full. They may improve evidence, resolve a known blocker, or finish existing work instead. This is a proposed application, not a measured result of this repository. [S12](../research/sources/index.md#s12)

## The operating rules in one paragraph

Start from a worthwhile outcome. Identify consequential uncertainty. Use the smallest credible action that can reduce it. Establish durable contracts where repeated work warrants them. Delegate only the authority actually granted. Verify claims against evidence. Make the relevant reality understandable. Release with an appropriate containment plan. Observe customer effects. Improve or simplify the factory when the evidence warrants it.

The next chapters make each rule concrete. Their purpose is not to create a longer checklist. It is to help decide which work can proceed quickly and which decisions deserve attention.

---

[Previous: The perspectives and the tensions](02-the-perspectives-and-tensions.md) · [Next: Discovery and product intent](04-discovery-and-product-intent.md)
