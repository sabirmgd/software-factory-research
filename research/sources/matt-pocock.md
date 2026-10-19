# Matt Pocock

## What was inspected

The repository README, prototype skill, and to-spec skill support this edition's descriptions. Other named skills from the conversation are not treated as fully inspected here. [S05–S07](index.md#s05)

## Mechanisms worth separating

The prototype skill chooses the artifact from the question: explore logic/state or compare interface variants. It marks the code as disposable, exposes relevant state, and captures the question and verdict separately from production changes. [S06](index.md#s06)

The inspected `to-spec` skill synthesizes existing context and includes implementation and testing decisions. It also checks test seams with the user. Its own instructions contain both a broad no-interview framing and this specific check; the precise file is more informative than a simplified slogan. [S07](index.md#s07)

## Our adaptation

We use prototypes where experience will answer a question better than more prose. We preserve shared domain language and composition of small practices. We do not require an interview or prototype for every change, and we do not assume a specification remains accurate after implementation without maintenance.

## Caution

Skill names, locations, and invocation rules can evolve. The current repository should be inspected before installing or composing it. Our publication does not include a tested installation procedure or a complete audit of every skill in the project.
