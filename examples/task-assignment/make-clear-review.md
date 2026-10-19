# Make Clear — Assignment is not sharing

**Question:** does assigning a person also give them access? **Audience:** product owner and engineer. **Status:** proposed product behavior, with a limited local model; not a production observation.

![Assignment checks authority and existing access before applying the change.](../../diagrams/rendered/08-assignment-flow.png)

## The consequence that matters

An eligible person can become responsible for a task they can already access. An ineligible person does not gain access merely by being selected. That rule prevents assignment from becoming an undocumented second sharing mechanism.

Compare two proposals. In proposal A, assignment grants access. It is convenient, but it changes the information boundary and requires explicit product and security approval. In proposal B, sharing remains separate and assignment requires existing access. This example uses B.

## What is observed, proposed, and unverified?

The local model's behavior can be executed through the documented tests. The diagram represents the intended flow. The real authentication boundary, database transaction, browser behavior, and concurrency semantics remain unimplemented. A passing local model test does not turn those boxes into observed production behavior.

## Questions worth challenging

Should external collaborators ever be eligible? Does an inactive membership invalidate an existing assignment or merely prevent new assignments? When a retry returns a historical success, how should the UI communicate later changes? Who decides the consistency point for membership revocation?

Understanding these consequences may be the only purpose of this view. Any requested approval must identify the specific decision and cannot be inferred from the reader having seen the diagram.
