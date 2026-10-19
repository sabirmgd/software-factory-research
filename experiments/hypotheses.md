# Hypotheses, not promises

**Status: proposed research program. No customer or factory-effectiveness experiments have been completed in this edition.** The [local validation](results/local-validation.md) checks publication mechanics and a small model only.

## H1 — Proportional planning buys useful uncertainty reduction

We expect planning focused on consequential unknowns to reduce post-implementation surprises relative to immediate implementation for ambiguous tasks, without imposing equivalent overhead on familiar tasks. Compare matched changes under a declared lightweight versus uncertainty-adaptive process. Count planning time, total lead time, review attention, scope corrections, and unmet acceptance criteria. A result in which documents grow but total rework does not improve weakens the mechanism.

The comparison should not deliberately remove essential security review. Record prior familiarity and requirement quality. Do not interpret a better result on a simpler feature as evidence of a better workflow.

## H2 — Make Clear improves comprehension, not just confidence

We expect grounded, focused views to reduce reconstruction effort and reveal consequential misunderstandings. Compare the same class of review with text plus code references versus a fit-for-purpose view with the same underlying evidence. Counterbalance order or use independent matched reviewers to limit learning effects. Ask reviewers to explain behavior, locate a risk, and state what is unknown before asking how much they liked the presentation.

Measure correct issue detection, missed issues, false alarms, time, and confidence calibration. Attractive diagrams that increase confidence without improving accuracy are a negative result. Do not hide critical evidence in the control condition. Avoid using only the author of a diagram as its evaluator.

## H3 — Enforced boundaries improve later change

We expect a well-chosen module interface with demonstrated checks to reduce unintended coupling and repeated human corrections, relative to written guidance alone. Use meaningful sequential changes in a representative codebase; retain previous tests at every checkpoint. Record public contract changes, touched responsibilities, review effort, regressions, exceptions, and guardrail false positives.

A small touched-file count is not the objective if it is achieved by making one file enormous. The test is useful change with intelligible responsibilities. Hold future tasks back from the implementation agent; public tutorial tasks in this repository are not held-out data.

## H4 — Bounded delegation reduces unnecessary interruption without increasing harm

We expect explicit authority, stopping conditions, and evidence requirements to reduce avoidable escalation while preserving consequential decisions. Compare tasks with equivalent risk and review obligations. Record authorized execution time, interruption reasons, missed escalations, unauthorized actions, and recovery costs. Do not treat an agent that never asks as successful if it silently changes product meaning.

Low-frequency severe failures may not appear in a small trial. Maintain safety controls and negative-case simulations; absence of observed incidents does not establish safety.

## H5 — Finishing work beats maximizing busy agents

We expect a work-in-progress limit calibrated to the actual constraint to improve completed outcomes and reduce review backlog, compared with continually starting new work. Observe waiting time, age of unfinished changes, reviewer workload, and throughput over comparable periods. Name the constraint: a client decision, integration environment, human reviewer, or deploy window may matter more than model capacity.

The effect may be small when the queue is empty. Avoid attributing unrelated changes in demand or staffing to the policy.

## H6 — Closing the outcome loop changes product choices

We expect explicit post-delivery evaluation to reveal when an intervention should be revised, removed, or expanded. Record the original hypothesis, user adoption, task outcomes, negative effects, and follow-up decisions. Compare with the prior process only where adequate historical data exists; do not reconstruct a favorable baseline from memory.

Evidence that teams still ship the original plan despite contradictory user results would challenge the claim that the loop is functioning. A decision to build less is a valid positive learning outcome, not necessarily a failure of delivery.

## Cross-cutting question

Do improvements persist beyond the first enthusiastic experiment and transfer to a different project? Separate reusable infrastructure, client-specific rules, model/tool versions, operator experience, and one-time setup cost. Every hypothesis can be revised or rejected.

Continue with the [evaluation plan](evaluation-plan.md).
