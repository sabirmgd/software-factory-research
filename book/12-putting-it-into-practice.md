# 12. Putting it into practice

[Reading guide](../READING-GUIDE.md) · [Previous: Customer outcomes and factory learning](11-customer-outcomes-and-factory-learning.md) · [Next: Limits and open questions](13-limits-and-open-questions.md)

> **Status:** Proposed synthesis, with attributed sources. Illustrations are not client results.

## Start with a product and one reference behavior

The first implementation should not be a giant orchestration platform. Choose one real workflow and a small set of consequential foundations. Build one representative vertical slice and examine the next change. This reveals whether the proposed boundaries help before they are reproduced by generators.

For this investigation, the concrete stack preference is TypeScript with NestJS and Next.js. Database, ORM, authentication provider, deployment target, monorepo tooling, and exact versions remain project decisions. They should not be invented merely to make a template appear complete.

The original handoff is preserved in the [archive](../archive/README.md). It is a historical implementation-oriented draft, not the current authority for the broader research model. Its stricter planning assumptions should be read alongside the adaptive approach in this book.

## A sensible bootstrap sequence

First establish outcome, actors, use cases, and important non-goals. Resolve the uncertainty that could reverse the first design with the smallest appropriate experiment. Identify candidate capabilities and their owners. Choose the few technology and operational constraints that the first slice genuinely needs.

Then create a minimal runnable application with a supported build, test, and development path. Add a clear public contract between browser and backend. Implement identity and authorization behavior using a deliberate policy, not an invented demo role list accidentally promoted to production.

Next, implement one complete behavior across user interaction, transport, application rules, persistence, errors, and evidence. Establish the dependency and policy checks that protect its intended boundaries. Challenge those checks with known invalid fixtures.

Only then extract generators and reusable skills from the working pattern. A generator should reproduce demonstrated structure, not amplify an untested design sketch.

## The repository template is not a fixed business model

A template may provide compiler settings, error conventions, test harnesses, route-policy plumbing, documentation templates, and generator mechanics. It should not pre-create a dozen speculative business modules or assume that every customer uses the same tenancy and permission semantics.

One possible structure is a backend composition root with capability modules, a web application with feature views, and a small public contracts package. Cross-cutting tooling and configuration can be shared where semantics are genuinely shared. Database ownership remains explicit even when one physical database serves several capabilities.

The template should provide a small set of supported commands and a working example. A new agent should be able to discover how to add a capability without searching through many obsolete patterns. A short `AGENTS.md` can point to current rules and examples instead of duplicating every document.

## Architecture before generators, evidence before scale

The reference slice should demonstrate permitted behavior, important denied cases, errors, persistence, and observability. It should also demonstrate that a prohibited import or missing policy fails the relevant check. A template that merely starts successfully has not demonstrated architectural enforcement.

After the first slice, introduce a plausible next requirement. Observe whether the change stays within the expected ownership boundaries and whether the public contract remains useful. A need to change the contract is not automatically failure, but it should be explained.

Do not claim success because a directory exists for every planned capability. The decisive evidence is whether a contributor can follow the supported path and whether known violations are caught.

## Adopting the model in an inherited codebase

Start by reconstructing behavior and ownership in the area being changed. Use existing tests, user-visible behavior, code paths, and available operational evidence. Mark inferred boundaries as inferred. Make Clear can help the engineer and agent develop a shared view before editing.

Do not force the entire application into the template's folder names. Add characterization tests around important behavior, identify one problematic seam, and improve the path required by the actual feature. Baseline structural violations when appropriate and prevent new ones. Treat active security defects according to their risk rather than hiding them in a general debt baseline.

The [inherited example](../examples/inherited-codebase/README.md) walks through this adoption path without pretending a rewrite is necessary for every legacy system.

## How the normal feature session changes

The next request begins with outcome and scope, then a targeted investigation. The task is routed according to unresolved product decisions, architectural impact, risk, and evidence availability. Small work can use a compact brief. Larger work may separate product and technical design.

A Make Clear view appears where it materially improves understanding. The agent receives a bounded assignment and implements a small verified increment. It reports actual evidence and deviations. The appropriate person accepts consequential decisions and authorizes release separately. Outcome feedback and recurring friction feed the next iteration.

The workflow should become lighter for familiar changes because the repository carries more of the relevant knowledge. That is a hypothesis to measure, not permission to remove safeguards based on a few successful demonstrations.

## What this publication actually implements

This repository is a research book with templates, examples, diagrams, and local validation tools. It includes a small executable assignment model to demonstrate bounded claims. It does not contain a production NestJS/Next.js application, a deployed multi-agent orchestrator, or a verified installation of the original Make Clear skill.

Keeping the publication separate from the eventual application starter is intentional. Readers can challenge the model without adopting a stack, and the starter can evolve without making every experimental idea a runtime dependency.

## A phased implementation handoff

The first project phase should settle consequential unknowns and define success. The second should provide a runnable base. The third should prove module and policy enforcement. The fourth should implement the reference behavior. The fifth should extract generators and agent guidance. The sixth should evaluate sequential changes and customer use.

Each phase should leave a usable result and visible evidence. A blocked phase should report the specific missing authority or capability, not continue by guessing. Decisions such as production credentials, paid services, licensing, and irreversible migrations require deliberate ownership.

## The practical implication

Build the smallest factory that helps one real project. Improve it in response to repeated evidence. The goal is to make future work easier, not to create a large framework that must itself be supervised before any customer value can be delivered.

---

[Previous: Customer outcomes and factory learning](11-customer-outcomes-and-factory-learning.md) · [Next: Limits and open questions](13-limits-and-open-questions.md)
