# Runnable assignment model

**Illustrative executable example, not production software.** This model demonstrates declared permissions, runtime policy based on trusted fixture state, no mutation on denied requests, optimistic revisions, scoped replay receipts, and one state-plus-audit commit point. It does not authenticate real tokens, start NestJS or Next.js, store durable data, or establish concurrent transaction safety.

## Run

Use Node.js 22 or later and TypeScript 5.8.3 (the compiler version used for this edition). No npm runtime packages are required. Install the compiler in your normal development tooling, then run from the repository root:

```bash
tsc -p examples/task-assignment/runnable/tsconfig.json
node --test examples/task-assignment/runnable/assignment.test.mjs
```

The compiler creates `.build/`, excluded from Git. `contracts.test.ts` contains three `@ts-expect-error` negative type fixtures. A missing expected error makes compilation fail. These fixtures show the guarantee for declared registries, not discovery of arbitrary Nest routes.

## Design boundaries

`TaskAssignments.assign` is the business operation. The actor's identity is assumed to have come from a trusted boundary; the model deliberately does not trust a caller-provided role. Membership and task visibility come from synthetic state. Manager access to all tasks in its workspace is an illustrative product decision, not a universal rule.

The fixture constructor and snapshot/revocation/failure-injection methods exist for testing. They are not proposed public application endpoints. Replay requires current caller authority and returns a historical successful receipt. It is not a guarantee that the assignee remains eligible forever. A new command re-evaluates eligibility and revision.

A cloned state is prepared and replaced synchronously only after checks and a simulated pre-commit failure point. This is not a demonstration of database durability, cross-process locks, or protection from concurrent membership changes.

## The next change

The `allowExplicitlySharedGuests` profile demonstrates one predeclared extension: a guest is eligible only when the task has already been shared with that guest. Assignment never grants sharing. Both baseline and extension tests are known in advance; this is **not a held-out maintainability experiment**.

See the [technical design](../technical-design.md), [acceptance criteria](../prd.md), [verification plan](../verification-plan.md), and [local execution report](../../../experiments/results/local-validation.md).
