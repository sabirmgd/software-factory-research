# Glossary

**Acceptance criteria.** Observable conditions defining the agreed behavior of a change. They are not the same as evidence that the feature benefits customers.

**Architecture contract.** A current statement of responsibilities, public interfaces, dependencies, and invariants. Some parts can be enforced; others require judgment.

**Architecture test / fitness function.** A repeated check of a chosen architectural property. It does not prove that the chosen architecture is optimal.

**Authority boundary.** The actions and decisions explicitly permitted for a task, independent of whether the agent is technically capable of doing more.

**Bounded autonomy.** Independent action inside an approved scope, with evidence requirements and escalation conditions.

**Brownfield / inherited system.** An existing product whose behavior, constraints, and users must be understood before changing it.

**Change locality.** The extent to which a change stays within the expected responsibilities. It is a signal to interpret, not a universal objective to minimize touched files.

**Deep module.** A capability whose public contract saves callers from understanding substantial internal coordination. Not a deep call chain or an unbounded god object.

**Delegation contract.** A task's intended result, allowed scope, stable constraints, required evidence, permitted actions, and stop conditions.

**Delivered.** The accepted behavior is available in its intended environment. This alone does not mean the customer outcome has been evaluated.

**Design debt / decision debt.** Working terminology for the cost of consequential decisions left implicit or repeatedly rediscovered.

**Deterministic check.** A specified computation over an input whose result can be reproduced under controlled conditions. The usefulness of the property being checked remains a separate question.

**Evidence package.** Revision-specific claims, actual checks and results, artifacts, and limitations supplied for review.

**Factory.** In this publication, a learning and delivery system intended to increase sustainable customer value without proportional unnecessary human effort.

**Golden path.** A supported, demonstrated way to perform recurring work. It should have an exception path and should not preserve obsolete patterns indefinitely.

**Greenfield.** A new product with no inherited application implementation, though it still has surrounding business and integration constraints.

**Guardrail.** A mechanism or policy that constrains behavior. Written guidance is not equivalent to tool-level enforcement.

**Leverage.** A proposed benefit in which an investment improves multiple later actions. Its setup and maintenance costs must also be counted.

**Make Clear.** The proposed human-understanding capability: choose the smallest useful explanation, comparison, visualization, or experiment; preserve evidence and uncertainty. Understanding need not lead to approval.

**Module ownership.** Accountability for a piece of state or business knowledge and the supported means of changing it.

**Outcome hypothesis.** A testable expectation about how an intervention helps particular people perform a task, with a plan for observing improvement and unacceptable regressions.

**Persona.** A human context and motivation used in product design. It is not automatically a security role.

**PRD.** Product requirements document: the problem, intended behavior, success hypothesis, scope, and acceptance examples.

**Program design.** The code shape that realizes a system design: types, public operations, file responsibilities, call sequences, and test seams.

**Prototype.** A disposable experiment answering an uncertainty. Its learning can influence production; its existence does not prove production readiness.

**Reversibility.** The specific ability to restore a state or compensate a side effect. Reverting source code does not reverse every consequence.

**RPI.** Research, Plan, Implement; also the name of an inspected HumanLayer skill with several workflow routes.

**System design.** Responsibilities and interactions among components, data stores, interfaces, and external systems.

**TDD.** Ambiguous abbreviation: technical design document in the planning chapters; test-driven development when discussing red–green–refactor. The meanings are not interchangeable.

**Understanding debt.** Working terminology for the effort required to reconstruct meaning, rationale, or evidence that should have remained accessible.

**Vertical slice.** A small demonstrable behavior across the layers it requires. A database-only or domain-only task may be useful but is not necessarily a complete vertical slice.

**WIP.** Work in process: started but unfinished work, including waiting for decisions, review, environments, and release.
