# Questions and coverage

These are condensed lines of inquiry from the discussion, not verbatim quotations. Repetition, transcription fragments, and unrelated personal context are omitted. The map preserves curiosity without making the book a question-and-answer transcript.

**Coverage status:** every inquiry below has a substantive treatment in the indicated chapter. “Treated” does not mean experimentally resolved. Measurement and optimality claims remain open in the experiment program.

| ID | Line of inquiry | Deeper issue | Main treatment |
| --- | --- | --- | --- |
| Q01 | Why does more generated code not necessarily mean better software? | Output versus sustainable value | [Chapter 1](../book/01-why-a-factory.md) |
| Q02 | What is Dex trying to prevent with design leverage? | Alignment before costly execution | [Chapter 2](../book/02-the-perspectives-and-tensions.md) |
| Q03 | What does program design contain? | Code shape versus component interactions | [Chapter 5](../book/05-research-and-adaptive-planning.md) |
| Q04 | How is maintainability measured? | Future change cost and imperfect signals | [Chapter 6](../book/06-architecture-for-future-change.md) |
| Q05 | Can architecture be tested in CI? | Enforcing a chosen design versus choosing well | [Chapter 7](../book/07-executable-engineering-constraints.md) |
| Q06 | What belongs in pre-commit rather than every edit? | Feedback latency and independently enforced gates | [Chapter 7](../book/07-executable-engineering-constraints.md) |
| Q07 | Can a second agent make the code pretty? | Mechanical formatting versus substantive review | [Chapter 7](../book/07-executable-engineering-constraints.md) |
| Q08 | What was the slop repository and what can it tell us? | Benchmark versus a production checker | [Chapter 7](../book/07-executable-engineering-constraints.md) |
| Q09 | How do modules hide meaningful complexity? | Caller-first design and responsibility | [Chapter 6](../book/06-architecture-for-future-change.md) |
| Q10 | Where should common clients and shared types live? | Shared semantics versus accidental coupling | [Chapter 6](../book/06-architecture-for-future-change.md) |
| Q11 | How do clean architecture and module ownership fit together? | Dependency direction without ceremonial layers | [Chapter 6](../book/06-architecture-for-future-change.md) |
| Q12 | Can an undefined permission make a build fail? | Static declarations and runtime enforcement | [Chapter 7](../book/07-executable-engineering-constraints.md) |
| Q13 | Are personas the same as authorization roles? | Product meaning versus security policy | [Chapter 4](../book/04-discovery-and-product-intent.md) |
| Q14 | Who owns data in a shared database? | Physical infrastructure versus logical ownership | [Chapter 6](../book/06-architecture-for-future-change.md) |
| Q15 | What is the logical order for a new project? | Bootstrap before repetitive feature work | [Chapter 12](../book/12-putting-it-into-practice.md) |
| Q16 | How does the process differ for maintenance? | Grounding and incremental adoption | [Chapter 12](../book/12-putting-it-into-practice.md) |
| Q17 | Can the stack and foundations become a template? | Validated golden paths before generators | [Chapter 12](../book/12-putting-it-into-practice.md) |
| Q18 | How do we run small agent sessions? | Bounded objectives and durable handoffs | [Chapter 8](../book/08-bounded-autonomy-and-agent-sessions.md) |
| Q19 | What distinguishes PRD, TDD, and outline? | Information ownership | [Chapter 5](../book/05-research-and-adaptive-planning.md) |
| Q20 | Does TDD mean technical design or test-driven development? | Ambiguous terminology | [Chapter 5](../book/05-research-and-adaptive-planning.md) |
| Q21 | Does each feature derive from existing architecture? | Stable foundations and deliberate deltas | [Chapter 5](../book/05-research-and-adaptive-planning.md) |
| Q22 | How much planning is enough? | Risk-adaptive uncertainty reduction | [Chapter 5](../book/05-research-and-adaptive-planning.md) |
| Q23 | Can research run automatically? | Read authority, bounded questions, and provenance | [Chapter 8](../book/08-bounded-autonomy-and-agent-sessions.md) |
| Q24 | Are human checks needed during implementation? | Delegation and consequential escalation | [Chapter 8](../book/08-bounded-autonomy-and-agent-sessions.md) |
| Q25 | How does Matt differ from Dex? | Composable mechanisms and overlapping artifacts | [Chapter 2](../book/02-the-perspectives-and-tensions.md) |
| Q26 | What does Poteto add? | Design for partial context and recurring mistakes | [Chapter 2](../book/02-the-perspectives-and-tensions.md) |
| Q27 | What is special about the architect skill? | Usage sketches and structural alternatives | [Chapter 6](../book/06-architecture-for-future-change.md) |
| Q28 | What does repeated friction as feedback mean? | Pattern diagnosis rather than automatic rewrite | [Chapter 6](../book/06-architecture-for-future-change.md) |
| Q29 | How does Uncle Bob fit without overplanning? | Design principles versus workflow defaults | [Chapter 2](../book/02-the-perspectives-and-tensions.md) |
| Q30 | Is this an optimal human–agent balance? | A hypothesis rather than a universal optimum | [Chapter 13](../book/13-limits-and-open-questions.md) |
| Q31 | Do we have an original perspective? | Synthesis anchored in experience and testable choices | [Chapter 3](../book/03-our-working-model.md) |
| Q32 | Can diagrams help on a phone? | Readable focused views and fallbacks | [Chapter 9](../book/09-make-clear-and-human-understanding.md) |
| Q33 | Why was Make Clear needed? | Reducing human reconstruction effort | [Chapter 9](../book/09-make-clear-and-human-understanding.md) |
| Q34 | Is understanding broader than approval? | Learning and exploration without a decision | [Chapter 9](../book/09-make-clear-and-human-understanding.md) |
| Q35 | Should Make Clear trigger automatically? | Useful explanation without new bureaucracy | [Chapter 9](../book/09-make-clear-and-human-understanding.md) |
| Q36 | Can a visualization be misleading? | Evidence provenance and uncertainty | [Chapter 9](../book/09-make-clear-and-human-understanding.md) |
| Q37 | How do we zoom out beyond software? | Customer outcomes and intervention choice | [Chapter 1](../book/01-why-a-factory.md) |
| Q38 | Why do I personally want a factory? | More capacity without permanent supervision | [Chapter 1](../book/01-why-a-factory.md) |
| Q39 | Can the factory decide not to build? | Discovery can change the intervention | [Chapter 4](../book/04-discovery-and-product-intent.md) |
| Q40 | How do we know the customer benefited? | Outcome evaluation after delivery | [Chapter 11](../book/11-customer-outcomes-and-factory-learning.md) |
| Q41 | What if human review is the bottleneck? | Flow and WIP rather than agent utilization | [Chapter 8](../book/08-bounded-autonomy-and-agent-sessions.md) |
| Q42 | How can repeated corrections become assets? | Mechanisms that remove recurring effort | [Chapter 11](../book/11-customer-outcomes-and-factory-learning.md) |
| Q43 | How can the factory avoid becoming bureaucracy? | Rule retirement and selective generalization | [Chapter 11](../book/11-customer-outcomes-and-factory-learning.md) |
| Q44 | Who can change the tests and constraints? | Evidence integrity and authority separation | [Chapter 10](../book/10-verification-and-safe-delivery.md) |
| Q45 | What can actually be reversed after release? | Containment and irreversible side effects | [Chapter 10](../book/10-verification-and-safe-delivery.md) |
| Q46 | How can we test the factory itself? | Comparisons, held-out changes, and limitations | [Chapter 13](../book/13-limits-and-open-questions.md) |
| Q47 | How should the inquiry be published? | A layered research book rather than a transcript | [Chapter 3](../book/03-our-working-model.md) |
| Q48 | How do we preserve questions without a Q&A? | Editorial question-to-argument mapping | [Chapter 1](../book/01-why-a-factory.md) |
| Q49 | What earlier claims need correction? | Source integrity and explicit uncertainty | [Chapter 13](../book/13-limits-and-open-questions.md) |
| Q50 | What should the next coding session actually do? | One reference behavior and phased validation | [Chapter 12](../book/12-putting-it-into-practice.md) |

## Deliberate exclusions and limits

Raw transcripts, speech-recognition fragments, unrelated personal details, and client-specific material are excluded. Earlier unsupported claims are not silently promoted into facts. The exact local Make Clear implementation and the interview transcript remain unavailable; see [source corrections](source-corrections.md).

The two archived handoffs preserve implementation detail that predates the broader customer-value and understanding model. They are linked for historical continuity, not treated as complete current instructions.
