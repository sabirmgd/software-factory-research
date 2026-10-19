# 12. Putting it into practice

[Reading guide](../READING-GUIDE.md) · [Previous: Customer outcomes and factory learning](11-customer-outcomes-and-factory-learning.md) · [Next: Limits and open questions](13-limits-and-open-questions.md)

> **Status:** Proposed implementation path. This repository is the research publication, not the production factory described here.

## Start with one product and one behavior

Do not begin by building an orchestration platform, a large template, or a collection of agent roles.

Choose one real product, one customer workflow, and one representative change. The change should be important enough to reveal real constraints but small enough to complete and learn from.

Task reassignment is useful because it crosses product intent, authorization, state ownership, concurrency, audit, user interaction, and release evidence without requiring an entire business application.

The first goal is not a reusable factory. It is one change delivered with less avoidable confusion and with honest evidence.

## A practical bootstrap sequence

### 1. Write the outcome

Name the affected people, their work, the expected improvement, and what must not get worse.

### 2. Inspect the current system

Find the relevant behavior, ownership, tests, entry points, and unknowns. Separate observed facts from inference.

### 3. Settle the important decisions

Clarify product rules, state ownership, public operations, failure behavior, and release boundaries. Do not specify private details that implementation can decide safely.

### 4. Build one thin behavior

Implement the smallest useful path across the required layers. Demonstrate one allowed case before scaling the mechanism.

### 5. Add the important denied cases

Prove that wrong-workspace, inactive-member, stale-revision, repeated-request, and storage-failure paths behave safely.

### 6. Make the result understandable

Prepare one focused explanation that shows what changed, what stayed stable, the important failure path, and the evidence.

### 7. Release within explicit authority

Choose the permitted environment, exposure, monitoring, stop condition, and recovery plan.

### 8. Learn from customer and engineering evidence

Observe whether the workflow improved and where the delivery process consumed repeated effort.

### 9. Extract only the repeated value

After the pattern works, consider a generator, shared test, reusable skill, or template. Do not automate an untested sketch.

## Keep the starter small

A useful starter may include:

- compiler and lint settings;
- error and result conventions;
- a test harness;
- policy declaration and enforcement plumbing;
- a small working example;
- a few architecture checks; and
- short guidance pointing to current patterns.

It should not pre-create speculative business modules or assume that every product uses the same tenant, permission, and data-ownership rules.

One possible structure is a composition root, capability modules, a web application, and a small public-contracts package. That is a starting option, not the business model of every project.

## Prove the path before generating it

The reference behavior should demonstrate:

- a permitted action;
- important denied actions;
- named failures;
- persistence and audit behavior;
- the structural rules that keep ownership clear; and
- evidence from the intended environment.

Also prove that prohibited imports, missing policies, or invalid permissions fail the relevant check.

A template that starts successfully has shown bootstrapping. It has not shown that the architecture protects future change.

Introduce a plausible next requirement. For example, allow an explicitly shared guest to receive a task without making every guest eligible. Observe whether the change stays inside the expected boundary and whether the public contract remains useful.

## Adopt the model gradually in an existing system

Do not rename the whole codebase or force it into the starter's folders.

For the area being changed:

1. reconstruct current behavior and ownership;
2. add characterization tests around important behavior;
3. identify one difficult seam;
4. improve the path required by the real feature; and
5. prevent new violations without pretending old debt vanished.

Baseline structural problems only when that is honest and safe. Active security defects should be handled according to risk, not hidden inside a broad “legacy exception.”

The [inherited-codebase example](../examples/inherited-codebase/README.md) shows this route.

## What a normal feature session should feel like

The workflow should become lighter as the repository carries more knowledge.

A familiar change may require only:

- a compact outcome and scope;
- targeted investigation;
- one bounded implementation owner;
- focused checks;
- a clear evidence summary; and
- the appropriate release decision.

A risky or unfamiliar change expands because the decision requires it, not because every feature follows the same ceremony.

If the factory makes familiar work heavier over time, that is evidence against its design.

## What this repository implements

This repository contains the book, sources, examples, diagrams, templates, local documentation checks, and a small executable assignment model.

It does not contain:

- a production NestJS/Next.js starter;
- a deployed multi-agent orchestrator;
- customer outcome evidence;
- production authorization integration; or
- proof that the complete factory saves more effort than it costs.

Keeping the research publication separate lets the model be challenged without requiring adoption of one stack.

## A sensible phased handoff

1. Settle the outcome and important unknowns.
2. Create a runnable base.
3. Prove module and policy enforcement.
4. Implement the reference behavior.
5. Test the next plausible change.
6. Extract only the mechanisms that demonstrated repeated value.
7. Evaluate customer use and total human effort.

Each phase should leave a usable result and visible evidence. A blocked phase should name the missing decision, access, or capability instead of guessing.

## What to do next

Build the smallest factory that helps one real project:

1. choose one workflow;
2. measure the current effort;
3. deliver one representative behavior;
4. observe the customer and engineering result; and
5. keep only the mechanisms that make the next change easier.

The factory is successful when future work becomes clearer and safer—not when the factory itself becomes large.

---

[Previous: Customer outcomes and factory learning](11-customer-outcomes-and-factory-learning.md) · [Next: Limits and open questions](13-limits-and-open-questions.md)
