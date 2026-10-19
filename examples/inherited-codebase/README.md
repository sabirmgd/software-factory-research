# Adopting the factory in an inherited codebase

**Status:** fictional scenario. No private repository was inspected for this example.

Suppose an application has several controllers writing task state, authorization mixed into UI assumptions, and few reliable tests. The request is to add reassignment history. A large rewrite might promise conceptual cleanliness, but it also postpones evidence and risks changing behavior nobody has fully documented.

The first task is to understand the mutation paths relevant to history. Use [the discovery note](discovery.md), then [the adoption plan](adoption-plan.md). The goal is one safer path for the requested change, not immediate conformity with a greenfield folder template.

Make Clear is useful before implementation: show the known writers, inferred owners, and missing evidence. A human can then correct the map before the agent relies on it. Label the map as a proposal when the code does not yet enforce the boundaries.

## The important contrast

A greenfield starter can begin with a strict boundary. An inherited system may require a temporary compatibility path and a baseline of existing violations. That is not permission to preserve an active vulnerability. Distinguish structural cleanup from immediate security risk.

Success would be the requested behavior delivered with evidence and one clearer ownership path, followed by a later change that can use it. It would not be the number of directories renamed.
