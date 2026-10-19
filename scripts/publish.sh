#!/usr/bin/env bash
# Publish only this prepared tree. No tokens are read from files or printed.
set -euo pipefail
ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET='sabirmgd/software-factory-research'
PUBLIC=false
DRY_RUN=false
for arg in "$@"; do
  case "$arg" in
    --public) PUBLIC=true ;;
    --dry-run) DRY_RUN=true ;;
    *) printf 'Usage: bash scripts/publish.sh --public [--dry-run]\n' >&2; exit 2 ;;
  esac
done
if [[ "$PUBLIC" != true ]]; then
  printf 'No action taken. Pass --public explicitly to publish this research book.\n' >&2; exit 2
fi
for binary in python3 node tsc git; do
  command -v "$binary" >/dev/null || { printf 'Missing prerequisite: %s\n' "$binary" >&2; exit 1; }
done
cd "$ROOT"
[[ -f README.md && -f research/sources/manifest.json && -f book/13-limits-and-open-questions.md ]] || {
  printf 'This is not the expected prepared research repository.\n' >&2; exit 1;
}
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
tsc -p examples/task-assignment/runnable/tsconfig.json
node --test examples/task-assignment/runnable/assignment.test.mjs
if [[ "$DRY_RUN" == true ]]; then
  printf '\nLocal checks passed. No GitHub login or remote state was checked.\nWould create PUBLIC %s and push this tree. No Git or GitHub writes performed.\n' "$TARGET"
  exit 0
fi
command -v gh >/dev/null || { printf 'GitHub CLI is required. Install gh, then run gh auth login.\n' >&2; exit 1; }
export GH_HOST=github.com
# A container's read connector is not a substitute for this local authentication.
gh auth status --hostname github.com >/dev/null 2>&1 || {
  printf 'Authenticate locally first: gh auth login --hostname github.com\n' >&2; exit 1;
}
LOGIN="$(gh api --hostname github.com user --jq .login)"
[[ "$LOGIN" == sabirmgd ]] || {
  printf 'Refusing to publish: authenticated account is %s, expected sabirmgd.\n' "$LOGIN" >&2; exit 1;
}
if CHECK="$(gh api --hostname github.com "repos/$TARGET" 2>&1)"; then
  printf 'Refusing to overwrite or append to existing %s. Inspect it and use a reviewed update workflow.\n' "$TARGET" >&2; exit 1
else
  if [[ "$CHECK" != *'(HTTP 404)'* ]]; then
    printf 'Cannot establish that the target is available. Check authentication/network before retrying. No repository creation attempted.\n' >&2; exit 1
  fi
fi
# Never accidentally add files to a surrounding repository.
if TOP="$(git rev-parse --show-toplevel 2>/dev/null)"; then
  [[ "$(cd "$TOP" && pwd)" == "$ROOT" ]] || {
    printf 'Refusing to operate inside a different parent Git repository. Extract this package separately.\n' >&2; exit 1;
  }
  [[ -z "$(git remote)" ]] || {
    printf 'Existing remotes detected. Inspect them; this script only publishes a new independent repository.\n' >&2; exit 1;
  }
  [[ "$(git branch --show-current)" == main ]] || {
    printf 'Use the main branch before publishing; the script will not rename existing branches.\n' >&2; exit 1;
  }
else
  git init -b main
fi
# Set identity only locally and only when it is missing.
if ! git config user.name >/dev/null; then git config user.name "$LOGIN"; fi
if ! git config user.email >/dev/null; then
  ID="$(gh api --hostname github.com user --jq .id)"
  git config user.email "${ID}+${LOGIN}@users.noreply.github.com"
fi
git add -- .
if ! git diff --cached --quiet; then git commit -m 'Publish Beyond Code Generation research book'; fi
if ! git rev-parse --verify HEAD >/dev/null 2>&1; then
  printf 'No commit available to publish.\n' >&2; exit 1
fi
if ! gh repo create "$TARGET" --public --description 'A living research book on customer outcomes, human judgment, bounded agents, and maintainable change.' --source "$ROOT" --remote origin --push; then
  printf 'Publishing did not fully complete. A remote may already have been created. Inspect gh repo view and git remote -v before retrying; do not delete or force-push blindly.\n' >&2; exit 1
fi
printf '\nPublished: https://github.com/%s\nGitHub Actions must be checked remotely; this script does not claim that remote CI passed.\n' "$TARGET"
