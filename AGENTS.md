# Agent instructions

This repository is one person's curated list. The rules it follows live in the
engine at <https://github.com/olitreadwell/awesome-list-template>, and
`readme.md` is the only source of truth for entries.

## Before you change anything

```bash
uv sync --group dev
make hooks-install
make check
```

## Rules

- Every entry is `- [Name](https://example.com/) - What it is.` with a capital
  and a closing period. This list does not use tags.
- Do not write entry text with a model. The descriptions are Oli's words, and
  the twelve entries without one are waiting for him, not for you.
- Run `make toc` after moving a heading, and never hand-edit Contents lines.
- Give every GitHub link its stars and last-push date with `make stats`. Never
  hand-write a stars number. `make stats-check` verifies the snapshot offline.
- `make sources` writes `reports/source-candidates.md`. Candidates are not
  entries, and nothing in that report belongs in the readme until a human
  writes it.
- `civic-tech.md` is a raw link list kept for reference. It is not checked and
  it is not part of the list contract.

## Layout

- `readme.md` holds the list, the Contents section, and the prose.
- `tests/test_readme.py` holds the invariants for this particular list.
- `jobs/links.sh` is the weekly link check, run by launchd from
  `schedule/launchd/links.plist`.
- `docs/maintaining.md` covers the day to day, `docs/migration.md` records what
  the engine changed and what it left alone.
