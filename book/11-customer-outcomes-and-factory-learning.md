# 11. Customer outcomes and factory learning

[Reading guide](../READING-GUIDE.md) · [Previous: Verification and safe delivery](10-verification-and-safe-delivery.md) · [Next: Putting it into practice](12-putting-it-into-practice.md)

> **Status:** Proposed synthesis, with attributed sources. Illustrations are not client results.

## There are two different endings

A feature can be delivered while its customer effect remains unknown. Treating both as one “Done” state makes it easy to stop learning at the moment code reaches production.

We propose separate states: delivered, operationally supported, and outcome evaluated. They need not require separate ceremonies, but the distinction should be visible. A feature may pass acceptance while adoption is low, or be adopted while creating a new support burden. Those are product findings, not necessarily implementation failures.

## Make the outcome hypothesis observable

At the start, name the people, task, present difficulty, hoped-for improvement, and unacceptable regressions. After release, collect evidence suited to that claim. For task assignment, evidence might include observed task completion, mistaken assignments, follow-up clarification, and whether users can explain current responsibility.

DORA's customer-feedback guidance emphasizes using customer interaction to inform product decisions. Our proposed operating model makes that feedback capable of changing the next task the agents receive. [S13](../research/sources/index.md#s13)

Do not overstate causality. A change in task time may reflect training, a different mix of work, cleaner data, or familiarity with the system. Record the comparison, sample, context, and uncertainty. A small qualitative observation can be useful without being described as proven return on investment.

## Software delivery and adoption are different work

People may need access, training, clear responsibility, migrated data, or a changed operating procedure. A factory that ignores these can deliver technically correct software that nobody can use effectively.

The outcome owner should be named. That person need not be the developer. The developer should, however, know whether an adoption dependency blocks evaluation. “The feature shipped but no one has access” is an actionable state, not a successful outcome.

Sometimes the best next intervention is not another feature. It may be a corrected integration, a clearer workflow, or removal of an unnecessary step. The factory should be capable of taking that feedback seriously even when it has already invested in a technical direction.

## Learn from the effort, not only the result

The factory-improvement loop examines what repeatedly consumed attention. Did an agent ask the same domain question? Did a reviewer catch the same authorization omission? Did different callers duplicate one business rule? Did deployment wait for an unowned decision? Did the explanation obscure the same distinction?

Classify the cause before adding a rule. An architectural problem may need a clearer owner. A representation problem may need a type. A structural omission may need a build check. A behavior regression may need a test. A judgment problem may need a decision record or a better example.

PStack's `correct` skill provides an especially concrete source for addressing recurring mistake classes through mechanisms and demonstrating the check against a known failure. Our broader learning loop also includes product and operational causes. [S10](../research/sources/index.md#s10)

## Remove knowledge that should no longer be repeated

Suppose three agent sessions each implement a slightly different assignment sequence. Writing a longer instruction to use the right sequence may help temporarily. A stronger intervention could be one supported assignment capability that owns the sequence, plus removal of obsolete examples and direct write paths.

Now the next contributor needs less knowledge. The correction has changed the environment rather than merely increasing the amount of prose the contributor is expected to remember.

This is the kind of leverage the project seeks: a human correction becomes an improvement to future work. It does not happen automatically. The new abstraction can be wrong or too broad. It should be tested against the actual recurring cases and a legitimate variation.

## Do not turn every incident into permanent bureaucracy

A one-off event may not justify a universal rule. A check can become obsolete. An exception can reveal that a boundary no longer matches the product. A template can accumulate fields no one reads.

Every durable rule should have a reason, an owner, a mechanism, and a review condition. The learning loop should be allowed to remove it. Otherwise, the factory becomes a growing collection of constraints that preserves old mistakes as policy.

A useful question is: what evidence would convince us that this rule is no longer worth its cost? If the answer is “nothing,” we may have turned an engineering hypothesis into dogma.

## Keep three knowledge layers separate

Reusable foundations contain conventions and capabilities that genuinely apply across projects: a tested route-policy pattern, an evidence format, or a validated module generator. Project knowledge contains the client's language, authorization meaning, data ownership, and operating constraints. Experiments contain practices whose value remains uncertain.

Do not promote a client-specific policy into the general starter merely because it appeared in a successful project. Nor should experimental orchestration become a mandatory foundation before it has been evaluated. Separation makes it easier to change or remove one layer without disrupting the others.

Versioning matters. A project should know which factory defaults it adopted. Updating the template should not silently change an existing product's behavior. A migration path is required when a shared mechanism changes.

## Measure a balanced set of outcomes

Track customer task outcomes, delivery time, human attention, rework, escaped defects, waiting time, and subsequent change cost. Record setup costs separately. Compare similar work where possible and explain differences in scope or risk.

Do not optimize a single proxy such as number of commits, tests, agents, diagrams, or documents. More activity can accompany worse outcomes. A shorter review can be worse if it misses important issues. A higher test count can hide tests that repeat implementation details.

The [evaluation plan](../experiments/evaluation-plan.md) specifies a modest first study. Its purpose is to discover whether the proposed mechanisms improve real work, not to manufacture a positive headline.

## The practical implication

After each meaningful delivery, ask two questions: did this help the intended people, and what should become easier next time? Record the evidence, including inconclusive or negative results. That is how the factory becomes a learning system rather than a faster queue of feature requests.

---

[Previous: Verification and safe delivery](10-verification-and-safe-delivery.md) · [Next: Putting it into practice](12-putting-it-into-practice.md)
