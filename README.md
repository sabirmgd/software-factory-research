# Beyond Code Generation
## A practical model for building useful software with AI agents

**A living research book by Sabir Moglad.** Plain-language revision · October 19, 2026.

AI agents can produce code quickly. The harder problem is deciding what is worth building, keeping changes safe, understanding what the agents changed, and proving the result helped.

This book proposes a software factory built around that harder problem. Human judgment becomes reusable. Agents work independently inside clear boundaries. Claims are connected to evidence. Repeated friction improves the next change instead of becoming permanent review work.

**[Read the five-minute version](START-HERE.md)** · **[Choose a reading route](READING-GUIDE.md)** · **[Follow one complete example](examples/task-assignment/README.md)**

![Three connected loops: customer value, engineering delivery, and factory learning.](diagrams/rendered/02-three-loops.png)

The model has three connected loops:

- **Customer value:** Are we solving a worthwhile problem?
- **Engineering delivery:** Can we make and release the change safely?
- **Factory learning:** What should become easier next time?

These are not three departments or a fixed sequence. A small change may pass through all three in one session.

## The problem this book addresses

Faster code generation does not automatically create more useful or maintainable software. It can instead move the bottleneck to the engineer, who must reconstruct intent, inspect unfamiliar changes, catch hidden assumptions, and decide whether the result is safe to release.

The goal is not maximum agent activity. The goal is more valuable, reliable change without a matching increase in unnecessary human supervision or future maintenance.

That requires a few simple disciplines:

1. Start with the customer's work and desired result.
2. Investigate the unknowns that could change the decision.
3. Record important product and engineering rules where they can guide later work.
4. Give agents freedom inside explicit scope and authority.
5. Verify specific claims with appropriate evidence.
6. Make the important parts easy for a person to understand.
7. Improve or remove factory mechanisms based on repeated evidence.

## One example runs through the book

The main example is task reassignment. A manager wants to assign a task to another person. The code is small, but the real behavior raises questions about membership, visibility, permissions, concurrency, audit history, and retries.

The example shows how to move from a feature request to a useful outcome, design a clear operation, delegate the work, test both allowed and denied cases, explain the result, and learn from the effort.

The runnable model is intentionally small and uses synthetic data. It demonstrates selected rules; it is not a production application.

## What is in this repository

- **Book:** thirteen short chapters that develop the model.
- **Start here:** a five-minute explanation of the whole argument.
- **Examples:** one continuous feature, one inherited-codebase path, and one customer request that may not need the requested software.
- **Templates:** optional working documents, not mandatory paperwork.
- **Research:** source notes, corrections, changes of mind, and open questions.
- **Experiments:** ways to test the claims without inventing results.
- **Diagrams:** editable source data and rendered views.

This is the research publication, not the future NestJS/Next.js starter or a deployed multi-agent system.

## How to read claims

The book keeps an important distinction:

- **Source position:** what an inspected source says.
- **Proposed:** this publication's recommendation or inference.
- **Illustrative:** a fictional example.
- **Observed locally:** a check executed in this repository.
- **Not evaluated:** a result for which no outcome evidence has been collected.

These labels protect the argument from becoming more certain as it is repeated. They should clarify the writing, not dominate it. Specific limitations appear where they change what the reader may conclude.

## Run the local checks

Open `index.html` for the complete offline reader. Markdown files remain the canonical source.

The edition uses Python 3.13, Node.js 22+, and TypeScript 5.8.3:

```bash
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
tsc -p examples/task-assignment/runnable/tsconfig.json
node --test examples/task-assignment/runnable/assignment.test.mjs
```

Rebuild the reader with `python3 scripts/build_reader.py`. Rebuilding diagrams requires Graphviz and `python3 scripts/render_diagrams.py`.

## Evidence boundary

The documentation checks, generated reader, diagrams, and small assignment model have local evidence in this repository. The broader claim—that this factory improves customer outcomes or engineering capacity—has not been established. The [experiment plan](experiments/evaluation-plan.md) describes what should be measured.

## Contribute

A useful contribution can be a counterexample, source correction, implementation result, failed experiment, or simpler mechanism. The goal is a better model, not agreement with the current one. See [CONTRIBUTING.md](CONTRIBUTING.md).

Rights and attribution are described in [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md). The original publication does not yet have a blanket reuse license.
