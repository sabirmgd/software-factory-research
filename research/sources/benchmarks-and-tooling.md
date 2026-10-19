# Benchmarks and tooling

## Different tools answer different questions

Dependency-cruiser validates configured dependency rules in JavaScript/TypeScript. ArchUnit targets architecture checks in Java. Import Linter expresses import contracts in Python. Their configurations and guarantees are not interchangeable. [S18](index.md#s18) [S25](index.md#s25) [S26](index.md#s26)

TypeScript can constrain representable declarations; Nest provides runtime authorization mechanisms. Neither automatically establishes the complete product policy or covers every possible entry point. Our route-inventory and deny-by-default design requires implementation and tests. [S16](index.md#s16) [S17](index.md#s17)

StrykerJS offers mutation testing to examine whether tests detect introduced changes. It is a test-quality probe, not a complete correctness proof. [S22](index.md#s22)

## SlopCodeBench

The inspected repository presents a benchmark for code erosion under iterative specification refinement. We borrow the idea of sequential change and retained correctness. We do not copy its metrics into production gates or repeat unverified dataset counts and performance results. It is separate from HumanLayer. [S19](index.md#s19)

## Unresolved tool name

“Slop Scan” was mentioned in the conversation but not reliably identified. No invented URL or recommendation is supplied. Similar names must be evaluated as distinct projects.

## Publication tooling

GitHub supports Mermaid in Markdown. This repository also provides rendered images so comprehension does not depend on a particular viewer. The publishing script follows the documented GitHub CLI repository-creation interface; it requires actual authentication and does not imply that a read-only connector can publish. [S21](index.md#s21) [S24](index.md#s24)
