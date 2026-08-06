#!/bin/sh
# One-time per-machine setup for the font-size-local git filter.
# Run after cloning: ./git-filters/install.sh
set -e

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
FILTER="$REPO_ROOT/git-filters/font-size-filter.py"

git config filter.font-size-local.smudge "python3 '$FILTER' smudge"
git config filter.font-size-local.clean "python3 '$FILTER' clean"

echo "registered font-size-local filter; re-checking out settings.json..."
git checkout -- settings.json
