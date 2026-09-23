# Maintaining this list

## Checks

```bash
make check        # rules, Contents section, GitHub stats, the list's own tests
make links        # lychee over every entry
make toc          # regenerate the Contents section
make stats        # fetch stars and last push dates for GitHub links
make stats-check  # verify the stats offline, no network
make sources      # candidates from upstream lists, as a report
```

The pre-commit hook runs the fast checks, the pre-push hook runs all of them.

## GitHub stats

Every entry that links a repository shows stars and a last-push date, for
example `- ★ 52,493 stars, last push 2026-09-23.`. `make stats` asks the GitHub
API through `gh`, writes `github-stats.json`, and rewrites only the trailing
stats segment of each line. When `gh` cannot reach GitHub, it keeps the numbers
already in the snapshot and changes nothing else.

## Weekly link check

`jobs/links.sh` checks every entry, writes `.state/links-report.md`, and with
`--open-issue` opens or updates one issue when something breaks, then closes it
when the list is clean again.

To run it weekly without a hosted runner:

```bash
mkdir -p ~/Library/LaunchAgents
sed "s|__REPO__|$PWD|g" schedule/launchd/links.plist \
  > ~/Library/LaunchAgents/nz.olitreadwell.awesome-olitreadwell.links.plist
launchctl load ~/Library/LaunchAgents/nz.olitreadwell.awesome-olitreadwell.links.plist
```

A laptop that is asleep at the scheduled hour runs the job on the next wake.

## Candidates from upstream lists

`[sources]` in `awesome.toml` names upstream readmes and the keywords to match.
`make sources` parses their tables, drops anything this list already carries,
and writes `reports/source-candidates.md`. Read that file, verify the source,
then write the entry yourself.
