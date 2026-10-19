# 5. Research and adaptive planning

[Reading guide](../READING-GUIDE.md) · [Previous: Discovery and product intent](04-discovery-and-product-intent.md) · [Next: Architecture for future change](06-architecture-for-future-change.md)

> **Status:** Proposed. The examples show how to scale planning, not a mandatory document sequence.

## Planning should buy useful information

The question is not whether planning is good. The question is:

> Which unknown could make us choose the wrong approach, and what is the cheapest credible way to resolve it?

A long document can expose an important mistake. It can also repeat facts everyone already knows while the real uncertainty remains untouched.

For task reassignment, “research the task system” is too broad. A useful research question is: “Where does current workspace membership come from, and can it change between the permission check and the assignment commit?” The answer affects both the design and the tests.

## Research the current system before replacing it

A useful research note separates:

- **Observed:** found in code, tests, configuration, or executed behavior.
- **Inferred:** the best explanation from incomplete evidence.
- **Unknown:** not established with the available access or time.
- **Proposed:** a possible change, not current behavior.

It identifies the relevant paths, interfaces, ownership, tests, and constraints at a known revision. It does not turn a plausible guess into a current-system fact.

Research depth should match the question. A label change may need one file and a nearby test. A membership rule may require tracing identity, tenant context, persistence, and several entry points. A new provider may require current documentation and an isolated experiment.

Autonomous research is appropriate inside the task's approved resources. That does not grant access to arbitrary customer data, production logs, paid services, or scripts with unknown side effects.

## Give each artifact one job

![Planning artifacts derived from one feature, with feedback to earlier decisions.](../diagrams/rendered/04-planning-artifacts.png)

Four artifacts can be useful, but they do not need to be four files:

- **Research:** What does the system do now, and what remains unknown?
- **Product requirement:** What should people be able to do, and what behavior is required?
- **Technical design:** How will system responsibilities and program structure support that behavior?
- **Implementation outline:** In what order will we build and verify useful increments?

For reassignment, one compact document might contain all four. A large cross-system change may keep them separate so different owners can review the right decisions.

Here, technical design document is written out instead of shortened to TDD, because TDD also commonly means test-driven development.

## Separate system design from program design

System design explains components, data stores, external systems, transactions, resource context, and failure behavior.

Program design explains public operations, important types, file responsibilities, call sequences, dependency injection, and test seams.

For reassignment, the system view might show identity, membership, task storage, and audit storage. The program view might define one `assign` operation and the ports it uses.

HumanLayer's inspected technical-design process reviews these as separate concerns. That is useful when both contain important choices. [S02](../research/sources/index.md#s02)

Do not specify every future function. Review decisions that affect ownership, invariants, coordination, security, or future change cost.

## Plan in demonstrable increments

“Build the database, then backend, then frontend” divides work by layer. It may postpone the first proof of real behavior until the end.

A better first increment might demonstrate one allowed assignment through the required layers. Later increments add denied cases, concurrency, audit behavior, and the user interaction.

A vertical slice crosses the layers needed to demonstrate one behavior. A domain-only step may still be useful, but it should not be described as complete user behavior.

Each increment should state:

- the observable result;
- the relevant files or boundaries;
- the evidence expected;
- what is safe to commit or deploy; and
- what would stop the work.

## Choose a route, not a paperwork tier

Use a route that fits the decision:

- **Familiar and low impact:** compact brief plus targeted checks.
- **A few open choices:** short combined product and technical discussion.
- **High product uncertainty or architectural impact:** separate research, product, technical, and implementation decisions.
- **One decisive unknown:** bounded experiment before a full plan.

RPI supports several routes and allows artifacts to be skipped when the necessary detail is already settled. This book keeps that flexibility. [S01](../research/sources/index.md#s01)

Risk is not the same as size. A one-line permission change can be dangerous. A large isolated prototype using synthetic data can be low risk.

## Know when to stop planning

Continue while another finding could change an important decision or make the next step substantially safer.

Stop when further detail is unlikely to change the next responsible action and implementation can provide better evidence at acceptable cost.

An agent should support “uncertainty is low” with an existing pattern, accepted requirement, relevant test, or experiment. A plausible design is not evidence merely because it is well written.

A planning budget is a review point, not permission to ignore danger. If the budget ends while an important unknown remains, reduce scope or escalate the decision.

## Keep documents and code connected

Reference the artifact that owns a decision instead of copying it everywhere. When implementation discovers that a product promise cannot be met, update the product decision. When code departs from an accepted design, make the deviation visible.

A correct document cannot compensate for different runtime behavior.

## What to do next

Before planning the next feature, answer:

1. What is already settled?
2. What unknown could reverse the approach?
3. What is the smallest credible evidence that reduces it?
4. Who owns the remaining decision?

Choose the planning route after those answers. Planning is valuable when it prevents avoidable surprise, not when it makes uncertainty look complete.

---

[Previous: Discovery and product intent](04-discovery-and-product-intent.md) · [Next: Architecture for future change](06-architecture-for-future-change.md)
