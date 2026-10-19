# O-001 — Demonstrable increments

**Status:** proposed implementation plan. The runnable model covers only the subset stated in its README.

## Preparation: settle the contract and environment

Confirm the PRD decisions, identity boundary, storage consistency, and permitted environments. Define the public command and outcomes. A type-only sketch is useful preparation, but is not a complete vertical slice.

## Slice 1: one permitted assignment

Build the smallest complete path through the real UI or API, authenticated actor, assignment capability, owned persistence, and returned result. Demonstrate A01 and a persistent audit record. Use synthetic data in a preview. Do not call a domain-only test a complete application slice.

## Slice 2: denied and ineligible interactions

Add the actual user-facing failure handling and server-side negative scenarios A02–A05 and A09. Test another workspace, inactive participation, forged client hints, and restricted access. Verify that no failure leaves an optimistic UI or persistent state showing an unconfirmed assignment.

## Slice 3: conflicts and retries

Implement the selected revision and idempotency semantics. Demonstrate A06–A08 and A11 through the real transport and persistence path. Observe that replay does not bypass current authorization and does not duplicate audit events.

## Slice 4: operational failure and release evidence

Demonstrate A10 with an injected persistence failure and inspect the actual transaction outcome. Add telemetry without sensitive payloads. Prepare the Make Clear review, record unrun checks, and obtain the separately required release authority.

## Stop rather than improvise

Escalate when the approved interface cannot express the behavior, a transaction cannot uphold the required invariant, a new external service is needed, or a guardrail would need weakening. Do not silently change the PRD to make the implementation easier.
