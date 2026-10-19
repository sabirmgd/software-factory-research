# 4. Discovery and product intent

[Reading guide](../READING-GUIDE.md) · [Previous: Our working model](03-our-working-model.md) · [Next: Research and adaptive planning](05-research-and-adaptive-planning.md)

> **Status:** Proposed synthesis, with attributed sources. Illustrations are not client results.

## A feature request is a starting point, not a complete product definition

“Allow managers to assign tasks” sounds clear until the system must decide who counts as a manager, which people can be assigned, whether assignment creates access, what happens when membership is revoked, and whether the person assigning needs confirmation. Those are product behaviors with technical consequences.

The first goal of discovery is not to produce a long document. It is to distinguish known behavior, assumptions, and decisions that someone must own. A coding agent can investigate existing behavior. It should not invent a company's access policy because it needs a boolean to finish a function.

The [task-assignment example](../examples/task-assignment/README.md) carries one requirement through the book. It is fictional, uses synthetic actors, and has no implied client approval. This separation matters: a coherent example is not evidence that real customers wanted it.

## From outcome to use case

An outcome hypothesis might be: team coordinators can make responsibility clear without follow-up messages or unauthorized access. That statement still needs observation. We would first learn how assignment works today, what “clear responsibility” means to the users, and which errors are costly.

A use case then describes an actor pursuing a goal. It names the trigger, relevant preconditions, the successful result, alternatives, failure behavior, and invariants. It is not a list of database operations. One use case may cross several screens and APIs; several use cases may share an endpoint.

For assignment, the successful result is not merely an updated row. The authorized coordinator can see the confirmed assignee; the assignee's access remains governed by the existing sharing policy; the audit history records the actual change; and a failed operation leaves no partial state. Whether notification is required immediately, eventually, or not at all is a separate product decision.

## Personas, roles, permissions, and resources

A persona explains a person's motivations and context. A security role groups capabilities. A permission names an operation. A resource and its context determine whether the operation is permitted in this instance. These concepts should be connected explicitly but not collapsed into one enumeration.

A product persona called “team coordinator” might include people with different permissions in different organizations. A service account may have no human persona. A user with a managerial role in one workspace should not automatically gain the same authority in another.

This distinction begins in discovery, not only in security implementation. Product examples should include authorized and unauthorized cases. Later, the technical design must specify how identity and resource context are established at runtime. The typed registry is a useful representation, not the source of the business decision.

## What the PRD owns

Our proposed PRD records the problem, affected actors, success hypothesis, intended behavior, non-goals, important constraints, and acceptance scenarios. It includes the human experience of failures: what users see, what can be retried, and what they are allowed to learn about unavailable resources.

HumanLayer's inspected PRD process separates those user-facing choices from implementation questions and asks how the result will help after release. Its technical details are deferred to the TDD. [S03](../research/sources/index.md#s03)

That separation is useful but not absolute in the sense of ignoring reality. An integration limitation may make a promised behavior impossible or prohibitively costly. Technical research can inform the PRD. The PRD should describe the accepted behavior and constraints without prescribing class names or folder layouts unnecessarily.

## Acceptance is not outcome measurement

Acceptance criteria establish what must be true for the feature to meet the agreed behavioral contract. Outcome evaluation asks whether the feature helped the intended people in practice. They answer different questions.

An acceptance scenario can verify that an inactive person cannot be assigned and that the previous assignment remains unchanged. It cannot establish that team coordinators now spend less time clarifying responsibilities. That requires observation of the workflow and a credible comparison with the prior situation.

A modest project may not support a controlled experiment. It can still record the evidence honestly: a small set of observed tasks, user explanations, error cases, or before-and-after timings with their limitations. The absence of a perfect causal estimate is not a reason to assume that shipping created value.

## Prototype the uncertainty, not the entire product

A logic prototype is appropriate when the difficulty lies in state transitions, rules, or consequences. An interface prototype is appropriate when people need to experience alternative flows or layouts. A technical spike is appropriate when an API, storage mechanism, or performance assumption must be tested. A customer conversation is appropriate when the meaning of the problem is still unclear.

Matt's prototype skill explicitly distinguishes logic and UI questions and keeps prototype artifacts separate from production implementation. We borrow that discipline, not its incidental tooling as a permanent requirement. [S06](../research/sources/index.md#s06)

For assignment, a small state explorer could demonstrate revocation between selection and submission. A UI comparison could test whether users understand the difference between selecting an assignee and granting access. Neither needs real credentials, production persistence, or an elaborate reusable design system.

Each experiment should state a question, an observation, a verdict, and the decision affected. “The demo looks good” is not a useful verdict when the uncertainty was whether assignment should confer access.

## Discovery should challenge the requested solution

The agent should not only ask which implementation the user prefers. It should surface a consequential assumption and explain why it matters. For example: “This proposal treats assignment as access. Is that intentional? The alternative is to require sharing first.” A Make Clear view can show the two outcomes without forcing a nontechnical reviewer to parse an authorization schema.

Challenge is not obstruction. Once the relevant person has made an informed decision within their authority, the factory should record it and proceed. Reopening settled choices without new evidence consumes the attention the system is trying to preserve.

The same applies to deciding not to build. If the requested assistant merely disguises an unreliable inventory source, discovery should expose that limitation. The [customer-outcome example](../examples/customer-outcome/README.md) demonstrates this branch explicitly.

## A useful readiness boundary

A feature is ready for technical design when the next technical decisions have enough product context to be made responsibly. It does not require knowing every future enhancement. It does require visible ownership of the unresolved questions that could reverse the design.

Before implementation, the selected slice should have a demonstrable result, clear failure behavior, and no silent assumption about a consequential permission or external commitment. Where uncertainty remains, a time-boxed experiment may be the implementation task itself.

## The practical implication

Keep the PRD close to examples. A short statement plus concrete permitted, denied, and failed interactions can communicate more than broad adjectives such as secure, seamless, or scalable. Make those examples traceable into the technical design and verification plan. That is how product meaning survives the handoff to agents.

---

[Previous: Our working model](03-our-working-model.md) · [Next: Research and adaptive planning](05-research-and-adaptive-planning.md)
