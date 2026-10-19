# 7. Executable engineering constraints

[Reading guide](../READING-GUIDE.md) · [Previous: Architecture for future change](06-architecture-for-future-change.md) · [Next: Bounded autonomy and agent sessions](08-bounded-autonomy-and-agent-sessions.md)

> **Status:** Proposed synthesis, with attributed sources. Illustrations are not client results.

## Turn intentions into mechanisms

“Keep the architecture clean” asks every contributor to reinterpret a goal. “Code outside Tasks may import only its published entry point” states a checkable boundary. The first can be useful guidance, but the second can become a reliable feedback mechanism.

The aim is not to enforce every preference. It is to make recurring, consequential mistakes difficult to introduce and easy to diagnose. A check should explain the violation, identify the supported alternative, and provide a governed exception path when necessary.

## Choose the strongest useful representation

Our preferred order is to remove an invalid path through architecture when possible, use types for representable constraints, add static or build checks for structural requirements, test runtime behavior, and retain prose for judgment that cannot be encoded usefully. This resembles the hierarchy in PStack's `correct` skill, which also requires demonstrating that a new check catches a real mistake. [S10](../research/sources/index.md#s10)

The order is not a law. A simple regression test may be the right immediate intervention while an ownership refactor remains too risky. The important distinction is between a reminder and a mechanism that actually detects or prevents the problem.

## What compile-time authorization can and cannot do

A typed permission registry can reject an unknown permission string. A complete typed policy map can reject a missing entry for a declared endpoint. Discriminated unions can make invalid combinations of configuration harder to express. TypeScript's narrowing and exhaustiveness mechanisms support this kind of representation. [S17](../research/sources/index.md#s17)

However, the compiler does not know that a real HTTP request has a valid identity, that a membership is still active, or that a resource belongs to the correct tenant. Those are runtime facts. A cast, unchecked input, an unregistered route, or a separate entry point can also evade a poorly designed static convention.

The proposed design therefore combines a typed registry with a route-inventory check and runtime deny-by-default behavior. Every actual route must have an explicit policy or a reviewed public designation. Application capabilities must enforce resource-specific invariants even when called outside HTTP. Nest's authorization documentation provides mechanisms such as guards and metadata; our deny-by-default and inventory requirements are additional design choices, not guarantees provided merely by using the framework. [S16](../research/sources/index.md#s16)

## Four separate assurances

| Mechanism | What it can establish in scope | What remains unproven |
| --- | --- | --- |
| Typed registry | A declaration uses known identifiers and shapes | Whether all runtime entry points use the declaration |
| Route inventory | Discovered routes match the policy inventory | Whether the policy itself is appropriate |
| Runtime policy checks | The checked request satisfies the implemented conditions | Whether omitted conditions should have existed |
| Negative acceptance tests | Specific forbidden interactions are denied | All possible inputs, races, integrations, and deployments |

The combination is stronger than any one element, but it is still not a proof of complete security. Public routes, background jobs, websocket handlers, and administrative scripts require deliberate scope. A rule that protects only REST controllers should say so.

## Architecture checks should have adversarial fixtures

Dependency tools can enforce forbidden imports and cycles. For JavaScript and TypeScript, dependency-cruiser provides rule-based dependency validation; ArchUnit and Import Linter address related needs in Java and Python respectively. These are tools to evaluate for the chosen environment, not interchangeable configurations. [S18](../research/sources/index.md#s18)

For each adopted rule, create a small valid fixture and a deliberately invalid one. A rule forbidding domain-to-infrastructure imports should fail when such an import is introduced. A rule restricting cross-module access should catch path aliases as well as ordinary relative imports within its documented scope.

The meta-test matters. A configuration file with a persuasive rule name can match no files at all. A passing command then creates confidence without enforcement. Test the checker against the failure it is meant to catch, and ensure CI runs the same command used locally.

## Three speeds of feedback

Pre-commit should run cheap, relevant checks and safe mechanical transformations. Examples include formatting staged files and high-confidence local lint rules. It is not the place to run every browser and database scenario.

Pull-request CI should independently run the required checks from a clean environment: types, boundaries, behavior, integration, migration, contract, and relevant end-to-end tests. Local hooks can be skipped. The server-side policy must not depend on a contributor voluntarily running them.

Periodic analysis can investigate broader change scenarios, mutation testing, dependency trends, or expensive environments. Start uncertain metrics as advisory signals. Turn them into blocking gates only after their meaning and false-positive cost are understood.

A pre-commit hook does not itself instruct an AI to fix a failure. It rejects or transforms a change. An agent driver must observe the result, attempt an appropriate correction within a budget, rerun the check, and stop when it cannot resolve the failure without changing authority or scope.

## Mechanical cleanup is not architectural review

Formatting can be delegated to deterministic tooling. A separate agent can inspect behavior, dependency changes, test adequacy, and unnecessary complexity. These are different responsibilities.

A cleanup pass should not quietly rewrite unrelated code, broaden the change, or change public behavior. Large cosmetic edits can make the functional change harder to review. Separate them when they obscure evidence. An independent reviewer should not silently become the author of the code it is evaluating.

## Metrics and the danger of optimizing the representation

Complexity, duplication, dependency counts, and changed-file counts can reveal interesting patterns. They can also be improved superficially. Splitting code into many forwarding wrappers may lower one metric while making the system harder to understand. A single public method can hide a poorly designed collection of responsibilities.

SlopCodeBench is a separate research benchmark focused on erosion across iterative specification changes. It is not a ready-made production CI plugin for our TypeScript application. We borrow the sequential-change evaluation idea while treating specific metrics as limited signals. [S19](../research/sources/index.md#s19)

The project-specific question is whether later changes preserve expected behavior and remain understandable within the intended boundaries. A score cannot replace inspection of that question.

## Governance of the guardrails

An agent implementing a feature must not silently weaken the policy used to judge that feature. It may propose a change to a constraint and explain the evidence, but the proposal requires the appropriate owner. Exceptions should identify scope, rationale, authority, and a review point rather than becoming permanent invisible bypasses.

For an inherited codebase, baseline existing structural violations and prevent new ones where a full cleanup would be impractical. Do not use a baseline to excuse an active data-access vulnerability. Structural debt and an exploitable security defect require different risk responses.

## The practical implication

Start with a few high-confidence rules that catch actual mistakes: forbidden internal imports, undefined permission identifiers, missing route policies, and behavior regressions. Prove the checks fail on known bad fixtures. Expand only when the evidence justifies the additional machinery. The factory should accumulate dependable constraints, not decorative configuration files.

---

[Previous: Architecture for future change](06-architecture-for-future-change.md) · [Next: Bounded autonomy and agent sessions](08-bounded-autonomy-and-agent-sessions.md)
