# Start here: the five-minute version

This book starts from one practical problem:

> AI agents can produce code quickly, but the engineer can still become the bottleneck for deciding, checking, explaining, and repairing everything they produce.

The answer is not to remove the engineer. It is to stop making the engineer repeat the same judgment and reconstruction work on every change.

## The whole idea

A useful software factory does three things:

1. **Chooses worthwhile work.** It begins with the customer's job and the result they need, not with a feature request treated as an order.
2. **Delivers change safely.** It gives agents clear boundaries, lets them work independently inside those boundaries, and asks for evidence about the result.
3. **Makes the next change easier.** It learns from repeated confusion, review comments, failures, and customer feedback.

![Three connected loops: customer value, engineering delivery, and factory learning.](diagrams/rendered/02-three-loops.png)

These are feedback loops, not departments or mandatory phases. A small change may move through all three in one session.

## One example

Imagine a customer asks:

> Let managers reassign tasks to other people.

A code generator could add an assignee field, an endpoint, and a dropdown. That would produce code, but it would leave important questions unanswered:

- Can every manager assign every task?
- Must the new assignee already belong to the same workspace?
- Does assignment also grant access to the task?
- What happens if two managers reassign it at the same time?
- What proves that a rejected request changed nothing?

The factory handles the request differently.

### 1. Clarify the result

The desired result might be: an authorized manager can hand work to an active member of the same workspace without changing who is allowed to see the task.

That is more useful than “add reassignment” because it states the behavior and one rule that must not change.

### 2. Find the important unknowns

The team inspects how identity, membership, task ownership, and access currently work. It does not research the whole codebase. It investigates the unknowns that could change the design.

### 3. Give the agent a bounded job

The assignment says what outcome is expected, what code is in scope, which rules must remain stable, what the agent may do, what evidence is required, and when it must stop and ask.

The agent can choose private implementation details. It cannot silently change the authorization model or deploy to production.

### 4. Verify specific claims

Instead of reporting “the feature works,” the evidence shows that:

- an authorized manager can assign an eligible member;
- an unauthorized request changes nothing;
- a member from another workspace is rejected;
- retrying the same request does not create a duplicate audit event; and
- conflicting updates do not silently overwrite each other.

Passing these checks supports a claim about the tested implementation. It does not, by itself, authorize a release or prove that customers benefit.

### 5. Make the change easy to understand

A reviewer should not have to reconstruct the whole system before reaching the decision. A short explanation or focused view shows what changed, what did not change, the important denied case, and where the evidence comes from.

### 6. Learn from the work

If every feature requires rediscovering workspace membership, that knowledge should become easier to find or enforce. If the same authorization omission appears repeatedly, a shared check may be worthwhile. If a template field never helps a decision, remove it.

This is how the factory becomes more useful without becoming larger for its own sake.

## The six rules

1. Start with the customer result, not the requested implementation.
2. Investigate only the unknowns that could change the next responsible action.
3. Record decisions agents should not have to rediscover.
4. Give agents freedom inside clear authority boundaries.
5. Match evidence to the claim being made.
6. Improve the system when the same friction appears repeatedly.

## Important distinctions

- **Accepted behavior is not customer value.** A feature can meet its requirements and still fail to help.
- **A test result is not release permission.** Verification and authorization are separate.
- **An explanation is not evidence.** It should point back to code, tests, or observed behavior.
- **Technical capability is not authority.** An agent may be able to perform an action it was not allowed to perform.
- **Reusable is not automatically better.** A shared mechanism is useful only when its repeated value exceeds its setup and maintenance cost.

## What is proven and what is proposed

This repository contains a proposed operating model, source-backed comparisons, fictional examples, and local checks for its documentation and small assignment model. It does not prove that the complete factory improves customer outcomes or engineering throughput. The [experiments](experiments/evaluation-plan.md) describe how those claims could be tested.

## Where to go next

- Read [Why a factory?](book/01-why-a-factory.md) for the problem behind the model.
- Read [Our working model](book/03-our-working-model.md) for the three loops.
- Follow the [task-assignment example](examples/task-assignment/README.md) for the complete worked path.
- Use the [reading guide](READING-GUIDE.md) to choose the shortest route for your purpose.
