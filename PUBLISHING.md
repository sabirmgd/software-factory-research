# Publishing the prepared repository

**Current delivery status: complete source package prepared locally; GitHub repository not created by this chat.** The connected account was confirmed, but the exposed integration provides read actions, not repository creation or commits. No authenticated GitHub CLI was available in the preparation environment. The prepared workflow and local checks do not imply remote GitHub Actions have run.

## Publish with your authenticated tools

Extract the ZIP into its own directory, not inside an unrelated Git repository. Use Python 3.13, Node.js 22+, TypeScript 5.8.3, Git, and the GitHub CLI (`gh`). The reader and diagrams are already built, so Graphviz and the reader's Python dependency are needed only when editing/regenerating them.

Authenticate the CLI with your `sabirmgd` account using `gh auth login --hostname github.com`. Complete authentication in the GitHub CLI/browser; do not paste a token into a chat or repository file. Confirm `gh auth status` and normal Git push authentication.

From the extracted `software-factory-research` directory run:

```bash
bash scripts/publish.sh --public
```

This reruns documentation checks, checker tests, TypeScript compilation, and the teaching-model tests. It verifies the authenticated account, refuses an accessible existing target, initializes a local repository if needed, commits the source, and creates `sabirmgd/software-factory-research` as a public repository. It does not force-push, overwrite an existing repository, choose a reuse license, enable Pages, or grant permissions to integrations.

A 404 can mean a missing or inaccessible repository. The script treats it only as permission to attempt creation through your authenticated account; GitHub remains authoritative about name availability. Other lookup errors stop the script.

## Inspect before publishing

Read the rights notice and confirm you are comfortable publishing the content. Client examples are fictional, source positions are attributed, and the historical drafts have correction notices. The original local Make Clear skill and unseen Codex material are not included.

To run the local checks without writing a Git repository or contacting GitHub:

```bash
bash scripts/publish.sh --public --dry-run
```

The dry run does not validate remote authentication, repository availability, creation, or push. A successful dry run is not a successful publication.

## Existing target or partial failure

The script refuses an existing target or remotes rather than guessing whether to overwrite. Inspect the existing repository and publish through a reviewed commit or pull request. If GitHub creation succeeds but pushing fails, the script reports the partial state; inspect `gh repo view` and `git remote -v` before resolving the authentication or network failure.

## After publication

Open the repository and inspect its workflow runs. The documentation CI has read-only repository permissions and no deployment action. Markdown and PNGs are immediately available to readers; `index.html` can be opened locally. Publishing a website through GitHub Pages is a separate repository setting and is not performed by this script.

The CLI operation is documented in the [source ledger](research/sources/index.md#s24). Choosing an open reuse license remains the author's decision, recorded in [LICENSE](LICENSE).
