# Local preparation validation

**Status: executed local checks. Date: October 17, 2026.** These observations concern the research publication and its small teaching model. They do not establish customer value, production security, comparative agent performance, or the effectiveness of the proposed factory.

## Environment

Python 3.13.5, Node.js v22.16.0, TypeScript 5.8.3, Graphviz 2.42.4, markdown-it-py 4.2.0, and Playwright 1.57.0 with the available Chromium binary. The repository's public CI is configured separately and has **not** run on GitHub.

## Executed checks

| Check | Actual result | Scope and limit |
|---|---|---|
| `python3 scripts/check_docs.py` | Passed for 75 Markdown documents and 13 substantive chapters | Local link/anchor integrity, source-ledger shape, diagram hashes, reader freshness; not external URL availability or factual proof |
| `python3 -m unittest discover -s tests -v` | 12 tests passed | Checker behavior including broken-link, missing-anchor, and invalid-diagram fixtures |
| `tsc -p examples/task-assignment/runnable/tsconfig.json` | Exit 0 with 3 expected-invalid declaration fixtures | Static example contracts only; no actual Nest route discovery or request authentication |
| `node --test examples/task-assignment/runnable/assignment.test.mjs` | 20 tests passed, 0 failed or skipped | Synchronous in-memory behavior, denial, retries, stale revision, simulated failure, and the known guest extension |
| `python3 scripts/render_diagrams.py` | 8 diagrams rendered, with SVG/PNG and Mermaid/DOT exports | Graphviz executed; an independent Mermaid renderer and GitHub rendering were not exercised |
| `bash -n scripts/publish.sh` | Passed | Shell syntax, not remote authorization or publishing |
| `bash scripts/publish.sh --public --dry-run` | Passed local checks; no Git/GitHub writes | Does not inspect remote state, create a repository, or push commits |
| YAML parse of workflow and issue forms | Four YAML files parsed; workflow has read-only contents permission | Structural inspection, not GitHub's remote workflow execution |
| `python3 scripts/check_reader_browser.py` | 390-pixel document width at a 390-pixel viewport; no broken images, duplicate IDs, missing internal anchors, script errors, or external requests | Chromium in-memory rendering; not a test of the ChatGPT iOS app or GitHub |

## Inspectable evidence

The [model TAP output](evidence/model-tests.tap), [compiler record](evidence/typecheck.txt), [checker test output](evidence/documentation-tests.txt), and [browser result](evidence/browser-check.json) preserve the executed checks' outputs. Timing values in test logs are environment-specific and are not performance benchmarks.

The [mobile reader sample](evidence/reader-mobile.png) and [chapter sample](evidence/reader-chapter-mobile.png) show the generated content at a narrow viewport. Representative diagrams and reader views were visually inspected for readable labels, clipping, and layout. Diagrams have captions that distinguish proposals from the limited executable model.

The preparation browser blocks navigation to local `file:` URLs. The generated HTML was therefore loaded directly into an in-memory browser document for layout inspection. No browser policy was changed. Normal file opening on a user's device was not tested here.

## Corrections made during validation

The initial graph layout was too wide for the intended phone reading path, so the diagram generator was changed to favor vertical layouts. The README's example commands were reordered to compile before running Node tests. The offline reader rewrites internal links and embeds assets so no network request is needed for the text or diagrams. Freshness checks cover distributable source and evidence files, not just chapter prose.

## What is still not demonstrated

No repository was created on GitHub and no remote workflow, Pages site, or production deployment was executed. No comparison establishes that this process reduces human effort, improves long-term maintainability, or creates customer benefit. The task-assignment model does not implement real identity validation, durable transactions, concurrent membership revocation, framework integration, or browser behavior. The later feature is visible in advance and is not held-out evaluation data.

Those questions belong to the [evaluation program](../evaluation-plan.md), not to a green documentation check. Preserve this distinction when describing the publication to others.
