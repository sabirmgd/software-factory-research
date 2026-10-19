# 4. Discovery and product intent

[Reading guide](../READING-GUIDE.md) · [Previous: Our working model](03-our-working-model.md) · [Next: Research and adaptive planning](05-research-and-adaptive-planning.md)

> **Status:** Proposed. The task-assignment story is illustrative.

## Start with the request, but do not stop there

A feature request tells us what someone currently thinks should be built. It does not automatically tell us the problem, the affected people, the rules, or the expected improvement.

“Add task reassignment” is a reasonable starting point. Discovery turns it into something a team can responsibly design:

> An authorized manager can move an existing task to an active member of the same workspace, without granting new visibility or losing the assignment history.

That sentence is not the whole product requirement, but it exposes much more meaning than the feature name.

## Describe the user-visible path

A useful use case shows what happens from the person's point of view:

1. A manager opens a task they are allowed to manage.
2. They choose an eligible member.
3. The system shows what will change.
4. The manager confirms.
5. The task receives the new assignee and records the event.
6. If the task changed meanwhile, the manager sees a conflict instead of silently overwriting another update.

Include important denied paths as well. A manager from another workspace must not learn whether the task exists. An inactive member must not become the assignee. A repeated request must not create duplicate audit events.

Concrete paths expose product questions earlier than broad phrases such as “secure reassignment support.”

## Keep four concepts separate

Product and security discussions often mix these concepts:

- **Persona:** the person's context and motivation, such as a supervisor coordinating urgent work.
- **Role:** a named position in the system, such as manager or member.
- **Permission:** a capability, such as `tasks:assign`.
- **Resource relationship:** whether this person may act on this particular task in this workspace.

A manager role alone may not authorize every assignment. The decision may also depend on workspace membership, task visibility, assignee eligibility, and the current task revision.

Separating these concepts avoids building product assumptions into vague role names.

## What the product requirement owns

The product requirement should answer:

- Who needs the change?
- What are they trying to accomplish?
- What behavior is required?
- What is deliberately out of scope?
- Which failures must be visible?
- What must remain unchanged?
- How will acceptance be demonstrated?
- What customer improvement do we expect?

It should not dictate every class, database table, or framework choice. Those belong to technical design unless the product behavior depends on them.

HumanLayer's inspected product-design material offers one source for separating user intent from technical structure. This book adopts that separation without requiring a long PRD for every change. [S03](../research/sources/index.md#s03)

## Acceptance and outcome are different

Acceptance evidence asks whether the implementation behaves as agreed. Outcome evidence asks whether the change helped people in their real work.

For reassignment:

- **Acceptance:** an authorized manager can reassign an eligible member, denied cases leave state unchanged, and the audit event is recorded.
- **Outcome:** supervisors redistribute urgent work faster, with no increase in access incidents or assignment mistakes.

The first can be checked before release. The second usually requires observation after people use the change.

> **Do not confuse:** meeting requirements with creating customer value.

## Prototype the uncertainty

A prototype should answer a question, not imitate the whole product.

If the uncertainty is whether managers understand that reassignment does not grant visibility, build the smallest interaction that tests that explanation. If the uncertainty is whether access rules can be represented safely, build a small state model. If the uncertainty is provider behavior, run an isolated integration experiment.

Matt Pocock's inspected material supports focused experiments as part of alignment and design. [S06](../research/sources/index.md#s06)

A prototype can influence production. Its existence does not make it production-ready.

## Challenge the requested solution

Discovery is useful when it can change the plan.

A customer asking for an AI assistant may actually have unreliable data, poor search, or an unclear operating process. A reassignment request may be caused by incorrect workload data rather than missing controls.

Challenge should be specific and helpful: name the assumption, explain its consequence, and propose a cheaper way to test it. Endless questioning is not discovery. It is delay.

## Know when the work is ready

A change is ready for technical planning when the team understands:

- the intended result;
- the people and resources involved;
- the main allowed and denied paths;
- the rules that must not change;
- the most important remaining uncertainty; and
- who owns unresolved product decisions.

Not every detail must be settled. The next step must simply be responsible and likely to produce better evidence.

## What to do next

Before writing the implementation plan, answer four questions in plain language:

1. What is the person trying to accomplish?
2. What behavior would count as success?
3. What must not become possible?
4. Which assumption could still reverse the approach?

Then choose the smallest artifact or experiment that makes those answers usable by the people and agents doing the work.

---

[Previous: Our working model](03-our-working-model.md) · [Next: Research and adaptive planning](05-research-and-adaptive-planning.md)
