# Beyond Code Generation
## Designing a software factory around customer outcomes, human judgment, and maintainable change

**A living research book by Sabir Moglad, developed through AI-assisted inquiry and editorial synthesis.** First research edition · October 17, 2026.

> How can we deliver more valuable, reliable change without requiring a proportional increase in human supervision—or accumulating a proportional increase in future maintenance?

This repository preserves an engineer's investigation: the questions behind the framework, differences among the sources, changes of mind, proposed mechanisms, concrete examples, and experiments that could prove us wrong. It is not a transcript, a universal methodology, or a claim that autonomous software engineering has been solved.

**[Start reading](READING-GUIDE.md)** · **[Explore the questions](research/questions-and-coverage.md)** · **[Follow one feature](examples/task-assignment/README.md)** · **[Inspect the sources](research/sources/index.md)**

![The proposed three-loop operating model.](diagrams/rendered/02-three-loops.png)

*Customer value determines what is worthwhile. Engineering delivery makes a bounded change. Factory learning improves the next iteration. The model is proposed; its outcome claims remain to be evaluated.*

## The argument

Make important human judgment reusable through current contracts, examples, and executable constraints. Let agents act within explicit authority. Connect claims to inspectable evidence. Use Make Clear to reduce the work of reconstructing understanding. Let customer reality change the plan, including the decision to build less software.

The influences include Dex Horthy/HumanLayer, Matt Pocock, Poteto's PStack, Robert C. Martin, and John Ousterhout. The comparison preserves their differences and distinguishes their source positions from our adaptations. No endorsement by those authors is implied.

## What is here

The **book** develops the argument in 13 chapters. **Research** preserves the questions, source notes, corrections, and evolution of the ideas. **Examples** demonstrate one continuous feature, adoption in an inherited codebase, and a customer request that may not need the requested software. **Templates** provide optional working artifacts. **Diagrams** include editable sources and rendered images. **Experiments** define hypotheses and evidence collection without inventing results. The **archive** preserves the earlier implementation handoff as historical material.

This is the publication repository, not the eventual NestJS/Next.js application starter. The runnable example is an intentionally limited in-memory model, not a production application.

## Evidence status

Source-backed descriptions link to a dated source ledger. Proposed practices are labeled as synthesis. Fictional examples use synthetic data. Local documentation and example checks are recorded separately from customer or factory experiments. No client productivity improvement, return on investment, or production deployment is claimed.

The original local Make Clear implementation and the specific interview transcript discussed in the conversation were not retrieved for this edition. Their limits are documented rather than filled with invented detail.

## Read or run locally

Open `index.html` for an offline, phone-friendly reading edition. Markdown files remain the canonical prose. The reader is generated with `python3 scripts/build_reader.py` and has no external assets or tracking.

Use Python 3.13, Node.js 22+, and TypeScript 5.8.3 for the checks used in this edition. Rebuilding the reader also needs `python3 -m pip install -r requirements-docs.txt`.

```bash
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
tsc -p examples/task-assignment/runnable/tsconfig.json
node --test examples/task-assignment/runnable/assignment.test.mjs
```

To rebuild diagrams, install Graphviz and run `python3 scripts/render_diagrams.py`. See [the diagram guide](diagrams/README.md) for the source-of-truth and rendering policy.

## Publish this prepared repository

See [PUBLISHING.md](PUBLISHING.md). `bash scripts/publish.sh --public` creates a new repository under the authenticated `sabirmgd` account and pushes these files after local checks. It requires an authenticated GitHub CLI, refuses an existing target, and does not overwrite a repository. Preparing this package did not create the remote repository.

## Contribute a useful challenge

Bring a counterexample, a source correction, an implementation experience with evidence, or a bounded experiment. See [CONTRIBUTING.md](CONTRIBUTING.md). The goal is a better model, not agreement with the current one.

## Rights and attribution

A blanket reuse license has not been chosen for the original publication. See [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md). Referenced projects retain their own licenses; their source code and full articles are not vendored here.
