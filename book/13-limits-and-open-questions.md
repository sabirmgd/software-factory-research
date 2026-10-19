# 13. Limits and open questions

[Reading guide](../READING-GUIDE.md) · [Previous: Putting it into practice](12-putting-it-into-practice.md) · [Experiments](../experiments/evaluation-plan.md)

> **Status:** Open questions. A coherent proposal is not proof that the proposal works.

## What remains unproven

This book offers a coherent operating model. It does not establish that the model improves outcomes or saves effort.

A team can have clear requirements, careful architecture, strong tests, bounded agents, and polished explanations while still spending more than the result is worth.

The following questions are not footnotes. Their answers should be allowed to change or narrow the model.

## When does planning cost more than it saves?

The proposed rule is to scale planning with uncertainty, risk, and consequence. The hard part is calibration.

An apparently familiar change may hide an important assumption. A detailed design may prevent one expensive reversal while increasing average preparation time. A long document may also fail to change a single decision.

A useful experiment should compare similar tasks and count both avoided rework and planning overhead. The goal is not one universal planning ratio. It is knowing which conditions justify more preparation.

## What if the guardrail is wrong?

A check can enforce a mistake perfectly.

A dependency rule may preserve a boundary that no longer matches the business. A required abstraction may add wrappers without reducing complexity. A policy registry may encode the wrong authorization decision.

The model therefore requires explicit revision. An agent should not silently remove the rule, but a team should not defend it merely because it is automated.

A strong factory can revise or retire a constraint without losing the reason and evidence behind the change.

## Can a clearer explanation make us confidently wrong?

Yes.

A polished diagram can hide omitted behavior. A concise summary can select only supporting evidence. A prototype can look like a finished product. A reviewer may prefer the presentation while missing a critical failure path.

Evaluate Make Clear using both effort and correctness. Ask whether reviewers can explain the system, find a deliberately included ambiguity, and predict a failure. Compare confidence with actual understanding.

The diagrams in this repository illustrate the model. They do not prove that visual review improves engineering outcomes.

## How independent is another agent?

Different prompts or models may expose alternatives, but they may share assumptions and blind spots. A second agent can also be persuaded by the first agent's confident explanation.

Independence should come from several sources: accepted behavior, externally observable results, adversarial fixtures, runtime evidence, and human judgment where consequences require it.

A useful study would compare review mechanisms against known defect classes rather than count how many comments a second agent produces.

## Can maintainability be measured honestly?

Change locality, public-interface growth, duplication, rework, and regression rates are useful but incomplete.

A valid requirement may be cross-cutting. A small interface may hide complexity. A metric may improve because the problem moved somewhere the measurement does not inspect.

Sequential changes are a stronger test than one static snapshot. But even they can be biased if the architecture was designed around the exact future tasks used for evaluation.

Hold out plausible later requirements when possible. Record what was known during the original design. Examine why each change took its shape. SlopCodeBench offers one relevant benchmark direction, not a definitive answer. [S19](../research/sources/index.md#s19)

## How much should become reusable?

A shared mechanism can spread good practice. It can also spread assumptions that belong to one product.

This book proposes promoting patterns after repeated value. The unresolved questions are how much repetition is enough and how to count migration, exception, and support cost.

Logging conventions and customer authorization semantics probably deserve different thresholds. “Reusable” is not one category of decision.

## Could engineers lose the skill to inspect the details?

If engineers review only compressed summaries, they may gradually lose the ability to understand the implementation underneath. If they inspect every detail, the factory may fail to increase capacity.

Make Clear should support drill-down, not replace it. Critical paths may need periodic deep review. Consequential design still benefits from direct participation. Customer understanding still requires real observation.

The correct balance may differ by system and by engineer.

## What would count as evidence against the model?

Evidence against the central proposal would include:

- comparable work requiring more total human attention without better outcomes;
- guardrails repeatedly forcing workarounds;
- explanations increasing confidence while hiding more important errors;
- later changes becoming harder despite the architecture investment;
- agents producing more unfinished review work; or
- customer outcomes staying unchanged while factory maintenance grows.

Mixed results are also useful. The model may help inherited systems more than small new applications, or security-sensitive work more than ordinary content changes.

The claim should become narrower when the evidence requires it.

## Avoid endless research

Uncertainty is not a reason to postpone action forever.

Choose a bounded experiment. State its limitations. Observe the result. Let that result change the next decision.

A failed experiment, counterexample, source correction, or simpler mechanism can improve the publication more than another confident restatement of the model.

## The conclusion for this edition

The strongest idea is simple:

> Make important judgment reusable, let agents work inside clear authority, connect claims to evidence, reduce avoidable reconstruction, and let customer reality change the plan.

That is an operating hypothesis worth testing. This repository preserves the reasoning and provides a concrete starting point. It does not declare the investigation finished.

---

[Previous: Putting it into practice](12-putting-it-into-practice.md) · [Experiments](../experiments/evaluation-plan.md)
