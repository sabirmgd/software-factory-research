# 6. Architecture for future change

[Reading guide](../READING-GUIDE.md) · [Previous: Research and adaptive planning](05-research-and-adaptive-planning.md) · [Next: Executable engineering constraints](07-executable-engineering-constraints.md)

> **Status:** Proposed synthesis, with attributed sources. Illustrations are not client results.

## The cost of the next feature

A system can satisfy today's requirement while imposing difficult choices on the next contributor. Our interest in architecture begins with that gap. We want a structure in which ordinary changes have a sensible home, important rules are not repeatedly reconstructed, and a contributor can work from a bounded view without violating hidden obligations elsewhere.

Architecture does not eliminate future change. It chooses which knowledge is grouped together, which dependencies are allowed, and which changes can be made independently. A useful design protects likely variation without inventing a general mechanism for every imaginable future.

## Discover modules from owned knowledge

Start with business capabilities and the decisions they own. A Tasks module might own assignment state and task transitions. Membership might own participation in a workspace. Notifications might own delivery attempts and provider behavior. These are candidates to validate, not a prescribed domain model for every application.

A folder named `database` is not a business capability merely because many modules use a database. Likewise, a global `services` directory says little about who owns a rule. Technical layers can help inside a capability, but they should not substitute for coherent ownership across the system.

The module contract should state purpose, owned state, public operations, allowed dependencies, prohibited knowledge, failure behavior, and a small set of expected change scenarios. Keep it short enough that a new contributor can actually use it.

## Design from the caller backward

Consider two ways to assign a task. In the first, the caller loads membership, checks a role, checks the task's workspace, updates an assignment row, appends an audit entry, and sends a notification. Every new caller must reconstruct that sequence and its failure handling.

In the second, the caller invokes an assignment capability with an authenticated actor context and a command. The capability owns the required orchestration and exposes a defined outcome. The caller still needs to understand the public contract, but not the private coordination required to uphold it.

![Caller-orchestrated rules compared with a module that owns the assignment operation.](../diagrams/rendered/05-module-depth.png)

*The second design is not automatically correct. Its purpose is to make ownership inspectable; the operation still needs adequate runtime checks and well-defined failure semantics.*

PStack's architect skill writes the caller's usage before deriving the type sketch. Its red-flag reference distinguishes shallow interfaces, leaked internal knowledge, split ownership, duplicated approaches, importable internals, and hand-maintained parallel lists. We use those as review prompts, not an automatic numerical score. [S08–S09](../research/sources/index.md#s08)

## A deep module is not a large mystery box

A useful interface hides the details callers should not coordinate. It must still expose outcomes, constraints, and relevant failure conditions. An operation returning only `true` or `false` may be too simple to use responsibly if callers must distinguish denied access, stale state, and a transient external failure.

Nor does depth mean a long chain of tiny wrappers. A sequence of forwarding methods can make understanding more distributed without hiding meaningful complexity. Keep a layer when it adds policy, adaptation, ownership, or a useful seam. Remove it when it only changes the name of the same call.

Our design question is therefore not “How few methods exist?” It is “How much relevant coordination does the caller no longer need to understand, and are the remaining obligations clear?”

## Clean dependency direction without ceremonial layers

A practical modular monolith is a reasonable starting hypothesis for our NestJS/Next.js example: one backend deployment with explicit internal capability boundaries. That is our proposed baseline, not a universal rule. Independent scaling, isolation, ownership, or deployment requirements can justify a different structure.

Inside a capability, business behavior should not casually depend on HTTP objects, UI state, ORM models, or vendor SDKs. Define the required capabilities on the business-facing side and implement adapters at the edges. The composition root wires them together. This applies the dependency principle from Clean Architecture without requiring an elaborate class hierarchy. [S14](../research/sources/index.md#s14)

A pure business policy can be a function. An application operation can coordinate ports. A controller can parse and authenticate a request and translate the outcome. These responsibilities need not all become separate files until separation improves clarity or change independence.

## Shared types and common clients

Two objects with the same fields do not necessarily represent the same concept. A public API payload, a database row, and a domain entity may differ in ownership and change cadence. Sharing them indiscriminately can turn a convenient package into the most coupled part of the system.

Share a contract when consumers genuinely share its meaning. Keep storage representations private. Let the browser consume a public wire contract or generated client, not backend internals. Place vendor SDKs behind the capability that owns the integration. Avoid creating a universal `CommonModule` simply because several features need helpers.

The source of truth also matters. When a permission list drives several derived artifacts, derive them from one registry where feasible. When the lists represent different things, test their intended relationship rather than pretending they are interchangeable.

## Database ownership is architectural ownership

A single physical database can support several logically owned modules. Each table or aggregate should have an accountable owner, and writes should pass through that owner's supported capability or an explicitly approved integration path.

This does not mean every reporting query must traverse a chain of HTTP calls. Read models, analytical views, and controlled joins can be appropriate. Their ownership, freshness, and access restrictions should be explicit. The anti-pattern is a feature making a convenient direct write into someone else's state without understanding its invariants.

Transaction boundaries deserve special attention. If assignment requires membership to remain active at a particular consistency point, state precisely what that point is and how it is enforced. A membership check followed much later by a write is not automatically equivalent to an atomic invariant. The illustrative in-memory example does not prove distributed consistency.

## Repeated friction as feedback

One awkward case does not condemn an architecture. A pattern is more informative: different callers need the same internal workaround; several features duplicate the same rule; types require recurring escape hatches; or a supposedly local change repeatedly touches unrelated modules.

Investigate whether the cause is a missed requirement, an implementation mistake, an unclear contract, or a boundary that no longer fits. PStack's architect process explicitly treats patterns of friction as a reason to revisit the sketch. Our adaptation requires a review of consequential boundary changes rather than an automatic rewrite. [S08](../research/sources/index.md#s08)

A useful record contains the repeated symptom, concrete examples, the implicated decision, alternative explanations, and a small corrective experiment. Do not jump from “this feels awkward” to “replace the architecture.”

## Measure what can be measured without pretending it is everything

An architecture test can enforce an agreed dependency boundary. It cannot establish that the boundary makes future work easy. For that, use a later change scenario and inspect the actual work: public interfaces altered, modules affected, repeated knowledge, rework, and regressions.

Change locality is a signal, not an absolute goal. A genuine change in business policy may correctly require coordinated changes. Penalizing every cross-module edit can encourage duplicating logic or hiding coupling. Compare the observed change with the responsibility model and the nature of the requirement.

## The practical implication

Establish a small set of module contracts, implement a reference behavior, and then challenge it with a plausible next change. Preserve stable defaults, not frozen guesses. Good architecture should reduce the knowledge required to make a correct ordinary change while keeping consequential decisions visible.

---

[Previous: Research and adaptive planning](05-research-and-adaptive-planning.md) · [Next: Executable engineering constraints](07-executable-engineering-constraints.md)
