# 7. Executable engineering constraints

[Reading guide](../READING-GUIDE.md) · [Previous: Architecture for future change](06-architecture-for-future-change.md) · [Next: Bounded autonomy and agent sessions](08-bounded-autonomy-and-agent-sessions.md)

> **Status:** Proposed. Checks can enforce accepted rules; they cannot prove that the rules themselves are wise.

## Turn repeated instructions into checks

Written guidance is useful when judgment is needed. It is weak when the same mechanical rule must be remembered on every change.

If every route must declare an access policy, a test can fail when a route has none. If one module must not import another module's private database code, a dependency check can enforce that rule. If permission names come from a registry, the type system can reject unknown names.

The point is not maximum automation. It is to stop spending human review on a rule a machine can check reliably.

## Use the strongest useful representation

A rule can live in several places:

1. a sentence in guidance;
2. a working example;
3. a template or generator;
4. a static check;
5. a runtime control; or
6. a monitored operational limit.

Choose the strongest representation that matches the rule.

“Use clear names” still needs judgment. “Every externally reachable route declares an access policy” can be checked. “An unauthorized assignment changes nothing” needs runtime behavior, not only a type declaration.

## Types protect representations, not reality

TypeScript can make permission names, endpoint identifiers, commands, and results explicit. It can ensure every known endpoint appears in a policy registry.

It cannot prove that a caller's token is valid, that membership is current, that the task belongs to the workspace, or that a database commit was atomic.

For task reassignment, compile-time declarations help prevent missing or misspelled policy entries. Runtime code must still establish identity, resource context, eligibility, and transaction behavior.

> **Do not confuse:** a well-typed permission with an authorized real-world action.

The separation between policy and delivery mechanisms follows the source material on architecture boundaries. [S10](../research/sources/index.md#s10)

## Check four different things separately

Authorization work often combines four claims:

- **Declaration:** every operation has a policy.
- **Identity:** the actor is authenticated as claimed.
- **Entitlement:** the actor may perform this operation on this resource.
- **Effect:** allowed and denied requests change state correctly.

One green test cannot be assumed to prove all four.

For example, a route inventory can prove that `tasks.assign` has a declared policy. A domain test can prove that a manager from another workspace is rejected. An integration test can prove that a rejected request writes neither task state nor audit state.

## Test the checker with invalid examples

An architecture check that has never caught a violation may be protecting nothing.

Keep small invalid fixtures that deliberately break the rule:

- a route with no policy;
- a forbidden import;
- an unknown permission;
- a module writing another module's state; or
- a denied operation that still writes an audit event.

The check should fail for the expected reason. This guards against a test that stays green because it scans the wrong files or ignores a new code shape.

The idea of testing tests connects with mutation and adversarial-fixture practices. [S17](../research/sources/index.md#s17)

## Use three feedback speeds

Not every check belongs in the same place:

- **Fast local checks:** types, focused tests, formatting, and small architecture rules.
- **Integration checks:** persistence, external contracts, and multi-component behavior.
- **Deployment checks:** real configuration, routes, credentials, migrations, and operational signals.

Fast checks guide the edit loop. Slower checks prove boundaries that cannot be simulated credibly. A production-like check should not run on every keystroke, and a fast unit test should not be presented as deployment proof.

The inspected testing sources distinguish several evidence layers and their tradeoffs. [S16](../research/sources/index.md#s16)

## Keep cleanup separate from design review

A formatter or simplifier can remove duplication and improve readability. It cannot decide whether assignment should grant access, who owns membership, or whether a transaction is safe.

Mechanical cleanup is useful after behavior is protected. Architectural review asks different questions about ownership, interfaces, side effects, and future change.

## Do not optimize the representation

Any metric can be gamed. A team can reduce file count by creating a giant module, improve coverage by testing trivial lines, or make changes appear local by hiding coupling behind shared utilities.

SlopCodeBench and related work point toward evaluating maintainability through later changes rather than only static snapshots. [S19](../research/sources/index.md#s19)

Use metrics as signals. Examine the real behavior and the next-change cost.

## Govern the guardrails

A check can enforce a wrong decision perfectly. Every important guardrail should therefore have:

- an owner;
- a plain-language reason;
- a known scope;
- invalid examples it catches;
- an exception or revision path; and
- a way to retire it when the rule no longer helps.

Security guidance on policy enforcement supports making controls explicit, but each project still owns its actual rules. [S18](../research/sources/index.md#s18)

## What to do next

Choose one repeated review comment. Ask:

1. Is the rule stable enough to automate?
2. What is the strongest appropriate representation?
3. What invalid example proves the check works?
4. Who may revise or remove the rule?

Automate that one rule well before building a broad governance framework.

---

[Previous: Architecture for future change](06-architecture-for-future-change.md) · [Next: Bounded autonomy and agent sessions](08-bounded-autonomy-and-agent-sessions.md)
