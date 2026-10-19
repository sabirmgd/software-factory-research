# Evaluation plan

**Status: proposed protocol.** Do not populate results with estimates that appear observed. This plan tests a working model, not the reputations of the authors who informed it.

## 1. Define the unit and the decision

Choose one question at a time. The unit may be a task, a review, a sequence of changes, or a customer workflow. State what decision the evidence will inform: retain a planning step, change a review view, enforce a boundary, or adjust permitted autonomy. Predeclare outcomes before inspecting the results.

Start with one greenfield product and one inherited area when feasible, but do not infer broad generality from two projects. Select comparable work that is representative of actual constraints rather than optimized for a demonstration.

## 2. Record a defensible baseline

Describe the existing workflow, staffing, model/tool versions, repository state, risk category, acceptance criteria, and environment. Record missing baseline data explicitly. A retrospective account can motivate a hypothesis but should not masquerade as a controlled comparison.

Where possible use matched tasks or alternate conditions across similar changes. Randomize or counterbalance review presentation to reduce learning effects. Do not withhold essential checks or expose real users to an intentionally unsafe process.

## 3. Measure multiple costs and benefits

| Dimension | Operational definition |
|---|---|
| Human attention | Active minutes spent clarifying, reviewing, correcting, and recovering, not just elapsed ticket time |
| Delivery time | Accepted task to verified, usable change; report waiting separately |
| Rework | Substantive revisions after implementation due to missed intent, design, or defects |
| Escapes | Problems discovered outside the intended verification boundary, with severity and exposure |
| Change locality | Responsibilities and public interfaces altered, interpreted alongside actual task scope |
| Comprehension | Correct explanation and risk recognition, including uncertainty, not self-rated confidence alone |
| Factory overhead | Setup, token/tool cost, maintenance, false-positive handling, and update effort |
| Customer outcome | The task-specific result defined in the outcome hypothesis, with adoption and guardrails |

Do not collapse these into one architecture or productivity score. A process can improve one dimension while worsening another. Show the tradeoff.

## 4. Separate setup from repeated work

Record initial templates, boundary checks, learning time, and environment setup as setup costs. Track recurring task effort separately. Report both cumulative cost and per-task observations without assuming setup amortizes across an unlimited number of future projects.

Track when a guardrail prevents a real error and when it obstructs legitimate work. Delete or adjust constraints that do not earn their maintenance burden. Record work that was stopped rather than dropping it from the dataset.

## 5. Exercise sequential change

Freeze an initial branch and agreed behavior. Prepare multiple realistic later requirements, with at least some withheld from the implementation agent. At each checkpoint retain prior acceptance checks, add new behavior checks, inspect public boundaries, and record changes. Keep evaluation instructions outside the agent's authorized context when testing genuine surprise.

Our public task-assignment example is intentionally visible and tiny. It teaches the protocol but cannot serve as proof that an agent generalized to unseen requirements.

## 6. Capture evidence reproducibly

For each run record source and test revisions, environment, task and risk classification, prompts or task artifacts safe to retain, model settings when known, authority policy, actual commands, output artifacts, reviewer decisions, and deviations. Redact secrets and personal/client data. Declare any missing telemetry.

A reviewer should be able to distinguish claimed success from executed checks and inspect failed attempts. Use the [evidence-review template](../templates/review-and-learning/evidence-review.md) and [result template](results/run-template.md).

## 7. Stop and recovery conditions

Set budget caps and authority boundaries before execution. Stop on unauthorized external actions, privacy exposure, repeated unexplained failures, invalid measurement, or a required decision that has not been made. In an isolated simulation, record the failure and analyze it. In a real environment, prioritize containment and the responsible owner's response.

Do not expand autonomy automatically because a few tasks passed. Consider task class, consequence, evidence quality, and recovery limits.

## 8. Interpret and decide

Report raw counts and distributions suitable to the sample, not unsupported precision or universal multipliers. State confounders, missingness, order effects, operator learning, task selection, and tool changes. Correlation after adopting the framework is not by itself a causal effect.

At the end, choose retain, modify, reject, or inconclusive for the mechanism under study. Publish counterexamples and negative results with enough context to learn from them. Customer benefit, maintainability, and attention cost can require different observation windows.
