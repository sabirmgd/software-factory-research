# TDD-001 — One owner for assignment

**TDD means technical design document. Status: proposed design for the illustrative product.** See [PRD-001](prd.md) for behavior.

## System design

The request boundary authenticates identity and parses the command. The application capability derives access from trusted membership and resource state, validates target eligibility and the expected revision, and applies assignment plus audit atomically within the chosen consistency model. The browser consumes a public response and does not import repositories or ORM models.

Tasks owns assignment state and its transitions. Membership owns participation and role meaning. Sharing determines whether a restricted resource is visible. A production integration needs a deliberate way to obtain these facts at the required consistency point. A single physical database does not remove the need for logical ownership.

The first design alternative leaves orchestration in each controller or job. It makes initial coding easy but spreads policy and mutation order among callers. The second exposes one assignment capability. We choose the second for this example because the operation should have one supported policy and mutation path. This is an illustrative choice, not an empirical comparison result.

## Public operation

```ts
assign(actor: AuthenticatedActor | null, command: AssignCommand): AssignResult
```

The command contains workspace ID, task ID, assignee ID, expected revision, and request ID. The actor contains authenticated identity only; a client-supplied role is not trusted. The result is a discriminated success or failure with defined semantics. A production async port may return a promise; the local model is synchronous by design.

## Failure and replay semantics

Authentication and current caller authority are checked before returning cached command results. Idempotency is scoped by workspace, actor, and request ID. Reusing a key for different command content fails. A valid replay returns the prior applied result and does not assert that the world has remained unchanged since that result.

A stale revision fails rather than overwriting new state. Ineligible assignees do not cause a sharing mutation. A task outside the selected workspace is not exposed. State and audit are committed together in the model by replacing a prepared state only after validation; real durability and concurrent atomicity require a database implementation and integration evidence.

## Program design

`contracts.ts` owns the typed permission and endpoint-policy declarations plus public types. `assignment.ts` owns the assignment capability and its private fixture state. `assignment.test.mjs` exercises its public behavior. `contracts.test.ts` contains expected compile failures for invalid declarations. These are small example files, not a complete Nest module layout.

The caller's sequence is parse → authenticate → call assignment → map result. It must not separately coordinate the model's internal membership, visibility, audit, and state mutations. Test-only snapshot access permits assertions about no mutation; it is not proposed as a production public data-export endpoint.

## Production integration requirements not implemented here

Implement real identity validation, persistent transactions, route inventory and policy coverage, audit retention, tenant-scoped queries, input limits, telemetry, and an actual browser flow. Specify membership consistency during concurrent revocation. Define idempotency expiration and behavior when historical resources are deleted. Verify all non-HTTP entry points.

## Approval and deviation policy

The example's decisions are illustrative, not human approvals. In a real task, changing access semantics or state ownership requires review. Private implementation choices may evolve inside the accepted public contract. A repeated need to bypass the capability is architectural feedback to investigate.
