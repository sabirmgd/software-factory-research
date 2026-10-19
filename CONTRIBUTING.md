# Contributing

The purpose of this repository is to improve the model, not to collect agreement. Useful contributions include counterexamples, corrections to source attribution, worked examples with clearly scoped evidence, and negative or inconclusive experiments.

## A claim should remain identifiable

Name the relevant chapter or synthesis decision. State whether you are correcting a factual attribution, challenging a proposed mechanism, or reporting an observation. Provide the context needed to interpret the claim, including constraints and alternative explanations.

Do not present a fictional example as a client result or a local unit test as proof of production security. Do not claim that a cited author endorses our adaptation. Keep proposed behavior distinct from observed behavior.

## Privacy and source material

Use synthetic or appropriately anonymized data. Do not publish secrets, private transcripts, customer information, or code you do not have permission to share. Link to third-party primary material and paraphrase appropriately rather than copying whole skills, books, or articles.

The original publication has no blanket reuse license selected. Contributors should submit only material they have the right to contribute; a broader licensing decision remains with the author. See [LICENSE](LICENSE).

## Editorial approach

Preserve the reasoning behind a change. Update the source ledger when a version-sensitive source changes. Update the question map when adding or moving a topic. Revise diagrams beside the prose they explain. Prefer deleting obsolete material to appending contradictory rules.

Keep the repository a research publication. A production starter or orchestration engine belongs in a separate implementation project unless a concrete, scoped example is needed here.

## Local checks

Run `python3 scripts/check_docs.py`, `python3 -m unittest discover -s tests -v`, and the Node example tests before submitting a change. Rebuild the reader after changing canonical Markdown. Diagram changes should update canonical graph JSON and regenerate exports. See [diagrams/README.md](diagrams/README.md).

A good pull request explains the problem with the prior text, the proposed change, the evidence, and the unresolved limitations. The issue forms provide starting points, not mandatory bureaucracy.
