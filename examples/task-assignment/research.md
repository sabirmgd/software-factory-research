# R-001 — Research before choosing implementation

**Status:** worked research brief, not findings from a real client codebase.

## Decision-dependent questions

Where is actor identity established? Which capability owns task state? Which capability owns workspace membership? Does a task's visibility differ from workspace membership? Does the existing system support optimistic revisions and deduplicated commands? Which entry points can change assignments outside HTTP?

Each question changes the design. An existing assignment operation should usually be reused rather than creating another writer. If sharing is independent from membership, merely checking workspace participation is insufficient. If jobs can assign tasks, controller-only authorization leaves an uncovered path.

## Evidence to collect in an actual project

Inspect the current route and job inventory, the task mutation path, membership and sharing rules, migrations, public contracts, and tests. Record revision-specific file pointers. Run only authorized commands in an isolated environment. Mark inaccessible production behavior as unknown.

## Synthetic starting assumptions for this example

There is one logical Tasks owner and a Membership source. The model receives an already authenticated actor from a trusted boundary. Workspace memberships and shares are trusted fixture state. Revisions are integers. Persistence is synchronous memory. These assumptions make the small demonstration runnable; they are not claims about a production architecture.

## Stop conditions

Do not implement by guessing whether assignment grants access. Do not add a second direct database writer because it is convenient. If the required consistency point cannot be supported by the existing transaction model, present alternatives before promising atomic behavior.

## Handoff

Proceed to the PRD with the illustrative decision that assignment preserves existing access. In a real project, attach actual evidence and unresolved questions before replacing this brief's synthetic assumptions.
