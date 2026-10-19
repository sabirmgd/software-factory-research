# Evidence plan

## What runs in this publication

The TypeScript project checks the public contracts and expected-invalid declarations. The Node tests exercise the synchronous in-memory assignment capability, including permitted, denied, ineligible, conflicting, retry, and pre-commit-failure cases. Actual local execution is recorded in [the preparation result](../../experiments/results/local-validation.md).

## What the real application would still need

Map A01–A11 from the PRD to real transport and database tests. Discover all assignment entry points and compare them with the policy inventory. Exercise invalid and expired credentials, tenant-scoped lookups, concurrent revocation, transaction failure, retries across process restarts, and the browser's failure handling.

Add an intentionally invalid architectural fixture and confirm the dependency check fails. Add a missing-policy route and confirm discovery or runtime default denial catches it. These checks are design requirements, not implemented features of the local model.

## Claim boundaries

The result of `tsc` says the checked TypeScript files satisfy the compiler under this configuration, including the deliberately invalid cases guarded by `@ts-expect-error`. It does not verify runtime request identity.

The result of the Node suite says the model meets its tested scenarios. It does not establish production security, distributed consistency, complete correctness, customer adoption, or reduced review time.

## Release and outcome

A real release needs operational evidence and explicit authority. Customer evaluation should observe whether responsibility becomes clearer without increased errors or exposure. No such release or customer study has occurred in this repository.
