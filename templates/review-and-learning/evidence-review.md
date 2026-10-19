# Evidence review

**Reusable template.** Use to judge important implementation claims. For small changes use a concise PR section instead of a separate report.

[Template guide](../README.md) · [Filled or worked reference](../../examples/task-assignment/verification-plan.md)


## Scope
Task, exact source revision, deployment/environment if relevant, and claims under review. Distinguish specification compliance from customer benefit.

## Evidence table
For each claim: requirement ID, supporting test or observation, command/environment, result, artifact, and known limitation. Failed, skipped, and unavailable checks must be visible.

## Adversarial cases
How could the implementation satisfy the apparent happy path while violating intent? Check denial, stale state, retry, partial failure, and boundary bypass where relevant.

## Design and test changes
Identify changes to public contracts, security policy, acceptance tests, and verification infrastructure. Explain why these changes are legitimate rather than made to fit the implementation.

## Judgment and authority
Record findings by consequence, what is blocked, what is acceptable within scope, and who can authorize release. Code review, test execution, and release permission are distinct.
