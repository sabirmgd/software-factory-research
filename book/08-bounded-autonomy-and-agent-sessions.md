# 8. Bounded autonomy and agent sessions

[Reading guide](../READING-GUIDE.md) · [Previous: Executable engineering constraints](07-executable-engineering-constraints.md) · [Next: Make Clear and human understanding](09-make-clear-and-human-understanding.md)

> **Status:** Proposed. The chapter describes an operating policy, not a capability automatically supplied by an agent.

## Autonomy belongs to a task

“How autonomous is the agent?” is the wrong starting question.

A difficult experiment can be safe when it uses synthetic data in an isolated workspace. A one-line permission change can be dangerous when it affects real customers. Autonomy depends on the task, environment, possible harm, evidence, and recovery options.

The useful question is:

> What may this task do without further approval, and what must make it stop?

The model does not require a person to supervise every edit. It requires clear authority and a reliable route for decisions outside it.

![Responsibility map: autonomous work stays inside approved contracts and escalates consequential deviations.](../diagrams/rendered/03-responsibilities.png)

## Give the agent a delegation contract

A bounded assignment should state:

1. **Result:** what should be true when the work is complete.
2. **Scope:** the files, modules, behavior, or systems included.
3. **Stable rules:** what must not change.
4. **Evidence:** what must be demonstrated.
5. **Allowed actions:** tools, environments, data, commits, previews, or external writes.
6. **Stop conditions:** findings that require escalation.

For task reassignment, an agent may change the Tasks module, add tests, and run a preview with synthetic users. It may not redefine who can assign, make production changes, contact customers, or hide a failed authorization check.

This need not be a long document. Six short sections in a work item may be enough.

## Keep research available during implementation

Research is not only a planning phase. Implementation may reveal that membership comes from a different service, a provider behaves differently from its documentation, or a transaction boundary is weaker than expected.

The agent can run a bounded investigation when the question fits its access and authority. If the result changes product intent, data ownership, security behavior, cost, or release risk, the relevant owner must decide what happens next.

HumanLayer's inspected RPI material supports returning to research or design when new findings change the work. [S01](../research/sources/index.md#s01)

## Preserve decisions, not entire conversations

An agent session will end. Another person or agent may continue later.

A useful handoff records:

- the accepted goal and scope;
- important decisions and their reasons;
- the current revision and environment;
- evidence already gathered;
- unresolved risks or unknowns; and
- the next responsible action.

A full transcript contains more text but often less usable context. The next contributor should not have to replay every attempt to discover which decisions still matter.

## Use one agent or several for a reason

More agents do not automatically create better work. Parallel work can duplicate investigation, create incompatible assumptions, or increase review burden.

Use one owner when the work is tightly connected and benefits from a consistent mental model. Use several bounded agents when the tasks are genuinely separable—for example, current-system research, source verification, and an isolated prototype.

Each agent needs a distinct result, authority, and handoff. A manager agent that only creates more managers increases coordination without improving evidence.

## Escalate consequences, not trivia

Human involvement is appropriate when a finding would:

- change accepted product behavior;
- modify an authorization or privacy boundary;
- move ownership of important state;
- create a new external or financial commitment;
- use sensitive data outside approved scope;
- make an irreversible or poorly recoverable change; or
- proceed without required evidence.

Private naming, established error mapping, or a local defect repair can usually remain autonomous when the contract stays intact.

A numeric “risk score” should not replace an explanation. State the specific consequence.

## Bound retries and make failure useful

An agent should not keep generating variations indefinitely.

Give the task a review point: a work budget, a maximum number of materially similar failures, or a specific missing-evidence threshold.

When the work stops, report:

- the smallest unresolved issue;
- the evidence gathered;
- the approaches already attempted; and
- the decision, access, or capability needed.

“The provider sandbox rejects the required operation” is actionable. “I could not finish” is not.

A failed checker is not permission to remove the checker. If the rule is wrong, propose that correction separately with evidence.

## Watch the real bottleneck

If implementation finishes faster than review, work accumulates. Keeping every agent busy makes the problem worse.

Track work waiting for decisions, evidence, review, environments, and release. When review is the constraint, reduce change size, improve the evidence package, use Make Clear, finish existing work, or pause new work.

Measure completed outcomes and recurring human effort, not active sessions or generated commits.

## What to do next

Before automating a workflow, write down:

1. what the task may change;
2. what it may not change;
3. what evidence it must produce;
4. what external actions are allowed; and
5. what finding must stop the work.

A reliable factory can explain why a task proceeded, why it stopped, and what supported the decision. Autonomy comes from scope and feedback, not from stronger instructions to “be autonomous.”

---

[Previous: Executable engineering constraints](07-executable-engineering-constraints.md) · [Next: Make Clear and human understanding](09-make-clear-and-human-understanding.md)
