# The next change — Explicitly shared external collaborators

**Status:** fictional sequential-change exercise, not evidence of general maintainability.

The next requirement permits an active external collaborator to receive an assignment only when the task has already been explicitly shared with that person. Assignment still does not grant access. The public assignment command should not need a new “bypass policy” parameter.

## Expected location of change

The eligibility policy inside the assignment capability changes. Public transport shape, tenant identity, revision handling, and audit behavior should remain stable. If every controller needs a new branch, that suggests the policy is not owned where the design claimed.

The runnable model exposes an example policy profile for this exercise and includes denied and permitted guest cases. This demonstrates a small extension within the model. Because the extension is visible in this repository, it is not a held-out maintainability benchmark.

## What to observe in a real trial

Record changed modules and public interfaces, retained acceptance results, review effort, and any workarounds. Examine why a cross-module change was required rather than penalizing file count automatically. Do not change the initial architecture after seeing the held-out task and then describe the evaluation as blind.

## Another unresolved requirement

What happens to an existing assignment when sharing is revoked? That may require product behavior, events, and consistency decisions beyond target eligibility. It should not be silently handled by deleting an assignment or retaining access. The case illustrates how a later requirement can legitimately reopen a foundational decision.
