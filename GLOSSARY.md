# Glossary

These definitions explain how this book uses its recurring terms.

**Acceptance criteria.** The behavior a change must demonstrate before it can be accepted. Meeting it does not prove that customers benefit.

**Architecture contract.** A current statement of a module's responsibilities, public interface, dependencies, and rules.

**Architecture check / fitness function.** A repeatable check for one chosen structural rule. It can enforce the rule without proving the rule is correct.

**Authority boundary.** What a task is allowed to do. Technical capability does not expand that permission.

**Bounded autonomy.** Independent work inside an approved scope, with required evidence and clear stop conditions.

**Brownfield / inherited system.** An existing product whose users, behavior, and constraints must be understood before it is changed.

**Change locality.** How closely a change stays within the responsibilities expected to own it. Touching many files is a signal to inspect, not automatic failure.

**Deep module.** A small public interface that saves callers from coordinating substantial internal work. It is not a giant class or a long call chain.

**Delegation contract.** The result, scope, stable rules, evidence, allowed actions, and stop conditions for a task.

**Delivered.** The accepted behavior is available in its intended environment. Customer benefit may still be unknown.

**Decision debt.** The cost of important choices left implicit and repeatedly rediscovered.

**Deterministic check.** A check that gives reproducible results for controlled inputs. Its consistency does not prove that it checks the right rule.

**Evidence package.** The exact revision, claims, checks, results, artifacts, and limitations prepared for review.

**Factory.** The learning and delivery system proposed by this book. Its purpose is more sustainable customer value without proportional unnecessary human effort.

**Golden path.** A supported and demonstrated way to perform recurring work, with a route for legitimate exceptions.

**Greenfield.** A new product without an inherited application, though it still has business and integration constraints.

**Guardrail.** A rule or mechanism that limits behavior. Written guidance is weaker than tool-level enforcement.

**Leverage.** An investment that improves several later actions after setup and maintenance costs are counted.

**Make Clear.** Choose the smallest explanation, comparison, visual, or experiment that creates accurate understanding while preserving evidence and uncertainty.

**Module ownership.** Responsibility for a piece of state or business knowledge and the supported ways to change it.

**Outcome hypothesis.** A testable expectation that an intervention will improve particular people's work without unacceptable regressions.

**Persona.** A person's context and motivation in product design. It is not automatically a security role.

**PRD.** Product requirements document: the problem, intended behavior, scope, success hypothesis, and acceptance examples.

**Program design.** The code shape used to realize the system design: types, public operations, file responsibilities, call sequences, and test seams.

**Prototype.** A disposable experiment used to answer one uncertainty. It is not production evidence.

**Reversibility.** The ability to restore a named state or compensate for a named side effect. Reverting code does not reverse every consequence.

**RPI.** Research, Plan, Implement; also the name of an inspected HumanLayer workflow with several possible routes.

**System design.** The responsibilities and interactions among components, data stores, interfaces, and external systems.

**TDD.** Either technical design document or test-driven development. This book writes the intended meaning when context may be ambiguous.

**Understanding debt.** The effort needed to reconstruct meaning, reasoning, or evidence that should have remained accessible.

**Vertical slice.** A small behavior demonstrated across the layers it actually needs.

**WIP.** Work in process: started but unfinished work, including work waiting for decisions, review, environments, or release.
