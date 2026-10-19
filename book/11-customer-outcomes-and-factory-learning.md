# 11. Customer outcomes and factory learning

[Reading guide](../READING-GUIDE.md) · [Previous: Verification and safe delivery](10-verification-and-safe-delivery.md) · [Next: Putting it into practice](12-putting-it-into-practice.md)

> **Status:** Proposed. This repository contains no customer trial proving the model's outcome claims.

## Delivery has two endings

Engineering work can end in two different ways:

1. The accepted behavior is available in the intended environment.
2. The change improves the customer's work.

The first is delivery. The second is an outcome.

For task reassignment, delivery means authorized managers can use the feature safely. Outcome means supervisors redistribute work more effectively without creating access mistakes, confusion, or extra support effort.

A feature can be delivered correctly and still fail to help. It can also help one group while making another group's work worse.

## Make the outcome observable

An outcome hypothesis should name:

- the people affected;
- the work they are trying to do;
- the current difficulty;
- the improvement expected;
- how it will be observed; and
- what must not regress.

For example:

> Supervisors can redistribute urgent tasks faster because they no longer need an administrator, while assignment errors and unauthorized visibility do not increase.

Possible observations include time to complete the workflow, support requests, correction frequency, access incidents, and direct customer feedback.

DORA's customer-feedback material supports connecting delivery with adoption and user evidence. This book uses that principle without claiming one universal metric. [S13](../research/sources/index.md#s13)

## Adoption is work too

Shipping a feature does not ensure people can find, understand, or trust it.

Adoption may require:

- suitable permissions and account setup;
- migration of existing data;
- clear product language;
- training or a changed operating procedure;
- support ownership; and
- observation of early failures.

These are not cosmetic tasks after the “real” engineering. They are part of making the intended result possible.

## Learn from the effort as well as the result

After a change, ask two sets of questions.

### Customer learning

- Did people use the change?
- Did their work improve?
- What became harder or riskier?
- Was the original problem correctly understood?

### Factory learning

- Where did the engineer spend avoidable attention?
- Which rule had to be explained again?
- Which test or environment failed too late?
- Which boundary made the change easier or harder?
- Which artifact helped a decision, and which created noise?

The purpose is not a long retrospective for every task. Capture evidence that can improve a repeated class of work.

## Put knowledge where the next action can use it

Different lessons belong in different places:

- A stable domain meaning may belong in the glossary or module contract.
- A repeated structural rule may belong in an architecture check.
- A known implementation pattern may belong in a reference example.
- A release hazard may belong in the deployment workflow.
- A one-off decision may belong in the feature record and nowhere else.

Do not copy every lesson into every document. Duplication becomes stale and creates another reconstruction problem.

The source material on architecture and feedback supports keeping business policy and its enforcement visible. [S10](../research/sources/index.md#s10)

## Remove obsolete knowledge

Learning is not only accumulation.

Delete or revise guidance when it no longer matches the product. Retire checks that enforce obsolete boundaries. Remove template fields that never affect a decision. Replace an old example when it teaches the wrong path.

A factory that only adds rules becomes harder to use and maintain. Simplification is part of learning.

## Do not turn every incident into bureaucracy

One failure may be unusual. A new permanent process is justified when the failure is important, likely to recur, or cheap to prevent reliably.

Ask:

1. What caused the failure?
2. Is the cause likely to recur?
3. Can a stable mechanism prevent or detect it?
4. What will that mechanism cost to maintain?
5. Could it block legitimate work?

The answer may be a test, a clearer contract, a better example, a smaller release, or no permanent change.

## Keep three knowledge layers separate

It helps to distinguish:

- **Product knowledge:** customers, workflows, language, policies, and desired outcomes.
- **Project knowledge:** architecture, integrations, environments, and local conventions.
- **Factory knowledge:** reusable delivery, verification, explanation, and agent practices.

Promote knowledge upward only when its meaning remains valid. A customer-specific permission rule should not become a universal starter default merely because it worked once.

## Measure a balanced result

Useful signals may include:

- customer task success;
- error or correction rate;
- delivery lead time;
- human review and clarification effort;
- escaped defects;
- later change cost;
- factory setup and maintenance cost; and
- work waiting for decisions or environments.

No single number represents the whole system. Faster delivery with more customer harm is not success. Less review time with harder future changes is not clearly leverage.

> **Do not confuse:** agent output with completed value.

## What to do next

After the next delivery, capture three things:

1. one observation about the customer's result;
2. one source of repeated engineering effort; and
3. one factory mechanism to keep, change, remove, or test.

Make the smallest useful update. The factory improves when learning changes future action, not when every task produces another permanent document.

---

[Previous: Verification and safe delivery](10-verification-and-safe-delivery.md) · [Next: Putting it into practice](12-putting-it-into-practice.md)
