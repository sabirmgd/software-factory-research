# 5. Research and adaptive planning

[Reading guide](../READING-GUIDE.md) · [Previous: Discovery and product intent](04-discovery-and-product-intent.md) · [Next: Architecture for future change](06-architecture-for-future-change.md)

> **Status:** Proposed synthesis, with attributed sources. Illustrations are not client results.

## Planning is a purchase of information

The useful question is not whether planning is good. It is what expensive uncertainty a planning activity can remove, and whether a cheaper action could remove it just as credibly. A long document can expose a mistaken assumption; it can also repeat settled information while the real uncertainty remains untouched.

Our proposed rule is that substantial research or design work should name the question it will answer and the decision that depends on the answer. “Research the notification system” has no clear boundary. “Determine whether the existing delivery mechanism prevents duplicate messages, because that determines whether reassignment can safely retry” does.

## Research establishes the current situation

Research should distinguish observed facts from interpretations and unknowns. A useful report identifies the relevant paths, tests, interfaces, data ownership, and constraints at a known revision. It describes what is there before proposing a replacement.

Autonomous research can be the default within the resources the task is allowed to access. That does not mean unrestricted access to client records, production logs, paid services, or arbitrary network destinations. Reading documentation may be harmless; running a script found in a repository may have side effects. Retrieved content is evidence to evaluate, not new authority for the agent.

The depth should scale with the question. A label change may need a file lookup and a neighboring test. A membership change may require tracing several entry points and checking the runtime source of tenant context. A new integration may require reading current vendor documentation and running an isolated experiment. A research agent must record when it could not access something rather than turning a guess into a finding.

## Four different artifacts, four different jobs

![Planning artifacts derived from one feature, with feedback to earlier decisions.](../diagrams/rendered/04-planning-artifacts.png)

*This shows information ownership. It does not require four separate documents for every change.*

The research report says what the system currently does and what remains unknown. The PRD says what people should be able to accomplish and what behavior is required. The technical design document says how system responsibilities and code structure will support that behavior. The outline says in what order the work will be implemented and verified.

Here, TDD means **technical design document**. Elsewhere, TDD commonly means test-driven development. This book writes out the term when the context could be ambiguous. Test-driven development is an implementation feedback practice, not another name for a design document.

For assignment, the PRD might require that an authorized manager assign an active member without creating new access. The system design identifies the source of identity, membership, task ownership, persistence, and audit. The program design specifies a task-assignment operation and the ports it uses. The outline begins with a small complete permitted assignment and then adds the denied and conflicting interactions.

## System design and program design

System design describes interactions among components and data stores, including transaction boundaries, resource context, failure behavior, and external systems. Program design describes the shape of the implementation: public interfaces, important types, file responsibilities, dependency injection, call sequences, and test seams.

HumanLayer's inspected TDD process treats these as separate reviewable sections. That offers a concrete way to expose both the high-level design and the internal decisions before code makes them expensive to revisit. [S02](../research/sources/index.md#s02)

Our adaptation is to review the decisions that matter at the appropriate level. A new data-sharing model deserves explicit attention. The name of a private helper usually does not. A design sketch is useful when it reveals ownership, invariants, or coordination—not because every future function must be specified in advance.

## The outline must describe demonstrable increments

“Build the database, then build the backend, then build the frontend” is a sequence, but not necessarily a good learning sequence. It postpones integration evidence until late. A thin end-to-end operation can reveal whether the contracts, authorization, and user interaction fit together while the system is still small.

A true vertical slice crosses the relevant layers to demonstrate one behavior. A domain-only unit of work may be an appropriate preparatory step, but it should not be mislabeled as a complete vertical slice. This corrects a loose use of the term earlier in the conversation.

An outline should name each increment's result, relevant files or boundaries, acceptance evidence, and stop conditions. It should also distinguish what is safe to deploy from what is merely safe to commit. A feature can be incrementally integrated behind controlled exposure without claiming the whole user workflow is ready.

## Choose a route, not a paperwork tier

For familiar, low-impact changes, use a compact brief and targeted verification. For a change with a few open choices, combine product and technical reasoning into a short design discussion. For substantial product uncertainty and architectural consequences, separate the PRD, technical design, and outline.

RPI itself supports several routes and permits skipping artifacts when the necessary detail is already settled. Our routing policy builds on that flexibility. It is not a fixed requirement inherited from the source. [S01](../research/sources/index.md#s01)

Risk and uncertainty are related but not identical. A small, well-understood change to an access-control rule can still require review because of its possible harm. A large exploratory prototype can be low risk when isolated from customers and production data. Do not classify work using line count alone.

## The stopping rule for planning

Continue planning when another finding could change a consequential decision or make the next step substantially safer. Stop when further detail is unlikely to change the next responsible action and implementation can provide better evidence at acceptable cost.

That rule requires judgment. An agent cannot simply declare that uncertainty is low because it has generated a plausible design. It should point to an existing pattern, a relevant test, an accepted requirement, or an experiment. When evidence is weak, the next action can be a bounded spike rather than a full feature.

A planning budget is useful as a review trigger, not as permission to ignore remaining danger. If the budget is exhausted and the unknown is still consequential, the result is an escalation or a smaller scope. It is not an instruction to proceed blindly.

## Documents must not become a second implementation

Reference the artifact that owns a decision rather than duplicating it everywhere. The PRD owns intended behavior. The module contract owns public responsibilities. The feature design owns the accepted technical delta. Test evidence describes a particular implementation revision.

When a technical discovery changes the product promise, update the PRD and associated views. When code deviates from a design, record and review the deviation. A document saying the right thing cannot compensate for code doing another thing.

## The practical implication

Begin the next feature by answering: what is already settled, what could reverse the approach, what is the smallest useful evidence, and who owns the remaining decision? Select the artifacts after answering those questions. Planning is valuable when it prevents avoidable surprise, not when it makes an uncertain plan look complete.

---

[Previous: Discovery and product intent](04-discovery-and-product-intent.md) · [Next: Architecture for future change](06-architecture-for-future-change.md)
