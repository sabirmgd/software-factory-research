# Brownfield discovery note

**Status:** hypothetical inventory format, not observed findings.

## Establish behavior before prescribing structure

Locate every path that can update assignment: HTTP handlers, jobs, administrative scripts, imports, and direct database access. Record actual revisions and source pointers in a real investigation. Identify which paths enforce identity, tenant context, target eligibility, and audit behavior.

Inspect existing tests and sample behavior in an approved environment. Characterization tests can preserve behavior, but some existing behavior may be incorrect. Mark the distinction rather than treating every historical response as a requirement.

## Make the uncertainty visible

A useful view can distinguish confirmed writers, suspected writers, and paths not yet inspected. It can show that two controllers use different eligibility rules. Do not call a visually grouped box a module boundary until the implementation actually enforces it.

## Decision to make

Should reassignment history be added separately to every writer, or should the requested path first move behind a supported assignment capability? Compare scope, migration risk, and the effect on later changes. A gradual compatibility adapter may be preferable to changing every entry point at once.

## Missing evidence is not absence

No search result does not prove there is no background writer. An inaccessible integration remains unknown. The research report should state the coverage and limitations of its inventory before the design depends on completeness.
