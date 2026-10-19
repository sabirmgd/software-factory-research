# 13. Limits and open questions

[Reading guide](../READING-GUIDE.md) · [Previous: Putting it into practice](12-putting-it-into-practice.md) · [Experiments](../experiments/evaluation-plan.md)

> **Status:** Proposed synthesis, with attributed sources. Illustrations are not client results.

## A working model is not an established optimum

The conversation produced a coherent set of ideas. Coherence is useful, but it is not proof that the combined process improves outcomes. A system can have clear requirements, careful architecture, strong tests, and visual review while still costing more effort than it saves for a particular project.

This chapter keeps the unresolved questions visible. The aim is not to undermine the proposal. It is to preserve the conditions under which learning can change it.

## When does planning stop paying for itself?

The proposed answer is to scale planning with consequential uncertainty and risk. The unresolved part is operational calibration. How reliably can an agent identify a supposedly familiar change that actually touches an important hidden assumption? How much human attention does the routing decision itself consume?

An experiment should compare planning approaches on reasonably similar tasks, including both avoided rework and planning overhead. A detailed plan that prevents one large reversal may be valuable even if it increases average preparation time. Conversely, a comprehensive document that never changes a decision may be unnecessary.

We should report the conditions, not declare one universal planning ratio. The conversation's interest in leverage does not justify claiming that a fixed percentage of human planning produces a fixed percentage of reliable automation.

## What if the guardrails encode the wrong architecture?

A constraint can reliably enforce a mistake. Preventing all cross-module changes might preserve a boundary that no longer matches the business. A required abstraction can create wrappers that add no value. A route policy can consistently implement an inappropriate permission decision.

This is why architectural feedback and explicit revision are part of the model. Enforcement protects an accepted decision while evidence remains capable of changing that decision. The agent should not silently remove the rule, but the human should not defend it merely because it is automated.

A strong test of the factory is whether it can retire or revise a constraint without losing accountability.

## Does visualization improve understanding or just confidence?

Make Clear is one of the most distinctive proposals, but it has a serious failure mode: an elegant view may make an incomplete explanation easier to believe. Reviewers may prefer it while missing consequential omissions.

Evaluation should therefore include both review effort and errors detected or missed. Ask reviewers to explain the system, identify a deliberately included ambiguity, or predict a failure path. Compare confidence with correctness rather than treating satisfaction as sufficient.

This repository's diagrams illustrate the model. They are not evidence that visual reviews improve engineering outcomes. The [experiment plan](../experiments/evaluation-plan.md) keeps that distinction explicit.

## How much independence does another agent provide?

Different prompts or models can expose alternatives, but they may share training patterns and blind spots. A reviewer may rationalize the author's design when given a persuasive explanation. A consensus among agents can remain wrong.

The model therefore relies on multiple kinds of evidence and authority separation, not simply more model votes. But the appropriate mix of independent tests, adversarial review, runtime observation, and human scrutiny remains project-specific. Cost and delay matter too.

A useful study would compare review mechanisms on known defect classes and realistic changes, rather than merely asking whether the second agent found something to criticize.

## Can we measure maintainability without gaming it?

Change locality, public-surface growth, duplication, rework, and regression rates are informative but incomplete. A legitimately cross-cutting requirement may require many files. An implementation can hide complexity behind a deceptively small interface. A metric can improve because complexity moved to a place the measurement does not inspect.

Sequential change scenarios are a better probe than a single static snapshot, but their selection can bias the result. If the initial architecture is designed around the exact future tasks used to evaluate it, the exercise tests preparation for those tasks rather than broader maintainability.

Hold out some plausible later requirements where possible. Record the initial information available. Combine metrics with examination of why the changes were necessary. SlopCodeBench provides a relevant benchmark direction, not a definitive answer to this measurement problem. [S19](../research/sources/index.md#s19)

## What is the right amount of generalization?

A mechanism reused across projects can create leverage. It can also spread inappropriate assumptions. A highly configurable starter may become harder to understand than several small purpose-built systems.

We propose promoting patterns after demonstrated repeated value, while keeping project-specific policy separate. The unresolved question is how much repetition is enough and how to account for migration and support costs. There is no reason to assume the same threshold for logging conventions and customer authorization semantics.

## What about the human skill we are trying to preserve?

If the engineer only reviews compressed summaries, they may gradually lose the ability to inspect the underlying implementation. If they inspect every detail, the factory may fail to increase capacity. This is a real tension rather than an inconvenience to explain away.

Make Clear should support drill-down and learning, not replace them. Periodic deeper review of critical paths, participation in consequential design, and direct customer observation may preserve the knowledge needed for good judgment. Their value should be considered alongside immediate throughput.

## What would falsify the central hypothesis?

Evidence against the proposed model would include comparable work requiring more total human attention without improved outcomes; visual review hiding more consequential errors than it reveals; guardrails repeatedly forcing workarounds; or subsequent changes becoming harder despite the architecture investment.

Other evidence may be mixed. The model might help inherited systems more than small new applications, or help security-sensitive work while imposing too much overhead on ordinary content changes. Those are useful findings. The publication should allow narrower claims to replace broad ones.

## How to contribute a useful challenge

A useful contribution identifies the claim, the context where it fails, the evidence or reasoning, and an alternative mechanism. A report of a failed experiment is welcome. So is a correction to an attribution, an example of a legitimate exception, or evidence that a template field imposes unnecessary work.

Do not turn uncertainty into a demand for endless research. Choose a bounded experiment, state its limitations, and let the next observation improve the model.

## The conclusion for this edition

The most promising idea is not a new universal sequence of documents. It is a separation of concerns: make human judgment reusable, keep autonomous action within explicit authority, connect claims to evidence, reduce unnecessary reconstruction, and let customer reality change the plan.

That is an operating hypothesis worth testing. This repository preserves the reasoning and supplies a concrete starting point. It does not declare the investigation finished.

---

[Previous: Putting it into practice](12-putting-it-into-practice.md) · [Experiments](../experiments/evaluation-plan.md)
