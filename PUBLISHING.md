# Publishing and repository status

## Current status

This project is already published as a **private** repository:

`https://github.com/sabirmgd/software-factory-research`

The local `main` branch tracks `origin/main`. Normal updates should use the existing Git workflow: review the change, run the checks, commit, and push without force.

Publishing the offline reader as a public website is a separate decision. GitHub Pages is not enabled by this repository.

## Before pushing an update

Run the documented checks from the repository root:

```bash
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
tsc -p examples/task-assignment/runnable/tsconfig.json
node --test examples/task-assignment/runnable/assignment.test.mjs
```

Rebuild the offline reader after changing Markdown:

```bash
python3 scripts/build_reader.py
python3 scripts/check_docs.py
```

The checks cover local documentation integrity and the small teaching model. They do not prove customer value, production security, or the effectiveness of the complete factory.

## Updating the existing private repository

Confirm the destination before pushing:

```bash
git remote -v
gh repo view sabirmgd/software-factory-research
```

Then use an ordinary push from `main`:

```bash
git push origin main
```

Do not force-push or change repository visibility as part of a normal documentation update.

## Historical initial-publication helper

`scripts/publish.sh` was created before this repository existed. It was designed to create a new public repository and deliberately refuses an existing target or repository with remotes.

It is retained as historical evidence of the prepared package. It is **not** the supported update path for the current private repository.

## Rights and attribution

The repository's private visibility does not settle reuse rights. See [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md). Choosing an open license or making the repository public remains an explicit author decision.
