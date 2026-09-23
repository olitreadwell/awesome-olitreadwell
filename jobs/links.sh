#!/usr/bin/env bash
# Weekly link check. Reports to .state/, and opens or updates one issue when
# --open-issue is passed and something is broken.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"

mkdir -p .state
report=".state/links-report.md"
open_issue=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --open-issue) open_issue=true; shift ;;
    *) echo "unknown argument: $1" >&2; exit 2 ;;
  esac
done

if ! command -v lychee >/dev/null 2>&1; then
  echo "links: lychee is not installed, skipping" >&2
  exit 0
fi

set +e
lychee --config lychee.toml --format markdown --output "$report" readme.md
status=$?
set -e

broken="$(grep -c '^|' "$report" 2>/dev/null || true)"
echo "links: report written to $report (lychee exit $status)"

if [[ "$status" -eq 0 ]]; then
  echo "links: every link resolved"
  if [[ "$open_issue" == true ]] && command -v gh >/dev/null 2>&1; then
    gh issue list --search "Link check in:title" --state open --json number --jq '.[].number' \
      | while read -r number; do
          [[ -n "$number" ]] && gh issue close "$number" --comment "Link check is clean again."
        done
  fi
  exit 0
fi

if [[ "$open_issue" == true ]] && command -v gh >/dev/null 2>&1; then
  existing="$(gh issue list --search "Link check in:title" --state open --json number --jq '.[0].number')"
  if [[ -n "$existing" ]]; then
    gh issue comment "$existing" --body-file "$report"
  else
    gh issue create --title "Link check: broken links found" --body-file "$report" --label "report"
  fi
fi

exit 1
