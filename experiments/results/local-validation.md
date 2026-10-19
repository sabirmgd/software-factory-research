# Local validation

**Latest run: October 19, 2026.** These checks cover the publication and its small teaching model. They do not establish customer value, production security, comparative agent performance, or the effectiveness of the proposed factory.

## Plain-language revision checks

| Check | Result | What it establishes |
| --- | --- | --- |
| `python3 scripts/check_docs.py` | Passed for 76 Markdown documents and 13 chapters | Local links and anchors, source-ledger shape, diagram hashes, and reader freshness |
| `python3 -m unittest discover -s tests -v` | 12 tests passed | The documentation checker rejects representative broken links, anchors, and diagrams |
| TypeScript 5.8.3 compilation of the assignment model | Passed | Static example contracts and expected-invalid type fixtures |
| `node --test examples/task-assignment/runnable/assignment.test.mjs` | 20 tests passed | In-memory allowed, denied, retry, conflict, and simulated-failure behavior |
| `bash -n scripts/publish.sh` | Passed | Shell syntax only; the script is now historical and is not the update path for the private repository |
| `python3 scripts/check_reader_browser.py` | Passed at a 390 × 844 viewport | No horizontal overflow, missing images, duplicate IDs, missing internal anchors, external requests, or browser errors |
| `git diff --check` | Passed | No new whitespace errors in the revision |

The offline reader was rebuilt after the Markdown changes. The browser inspection loaded the owned HTML directly in memory and used the locally installed Chrome binary. It did not test GitHub rendering, iOS, or the ChatGPT app.

## Inspectable evidence

The [browser result](evidence/browser-check.json) records the current reader checks. The [mobile contents sample](evidence/reader-mobile.png) and [chapter sample](evidence/reader-chapter-mobile.png) show the current narrow-screen layout.

The [model TAP output](evidence/model-tests.tap), [compiler record](evidence/typecheck.txt), and [checker test output](evidence/documentation-tests.txt) preserve the original first-edition outputs. The current revision reran those test suites successfully; timing values are not performance benchmarks.

The diagram sources and rendered outputs still match their recorded hashes. Diagrams were not regenerated because their canonical sources did not change in the plain-language revision.

## Repository boundary

The project now exists as the private GitHub repository `sabirmgd/software-factory-research`. Local checks do not replace remote GitHub Actions. Each pushed revision must be verified against its own workflow run.

Making the repository public, enabling GitHub Pages, choosing an open license, or deploying a production system remain separate decisions.

## What is not demonstrated

No comparison establishes that this process reduces total human effort, improves long-term maintainability, or creates customer benefit.

The assignment model does not implement real identity validation, durable database transactions, concurrent membership revocation, framework integration, or production behavior. Its later guest-assignment change is visible in advance and is not held-out evaluation data.

Those questions belong to the [evaluation program](../evaluation-plan.md), not to a green documentation check.
