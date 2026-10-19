# Incremental adoption plan

Begin with a behavior baseline for the actual requested path. Add tests for assignment and denied cases before restructuring it. Capture known structural violations separately from active security issues.

Introduce one supported capability for the new reassignment behavior, with clear state ownership and audit semantics. Migrate the relevant caller through a compatibility layer when necessary. Keep the external contract stable unless product review approves a change.

Add an architecture rule that prevents new callers from importing the capability's internals. Where legacy imports cannot be removed immediately, list explicit exceptions with scope, reason, owner, and a review point. Test that a new unapproved import fails. A global count alone can hide moving a violation from one place to another; inspect the actual edge set.

Verify the new behavior through the existing application, including persistence and failure paths. Do not infer integration success from a local domain test. Update the current-system map so the newly enforced boundary is distinguishable from the remaining inferred areas.

For the next feature, prefer the supported capability and remove one obsolete path when the change justifies it. Record whether the new boundary reduced repeated coordination. If the wrapper merely forwards to several inconsistent writers, the ownership problem may remain unresolved.

A complete rewrite is an option to justify with evidence, not an entry requirement for benefiting from the factory.
