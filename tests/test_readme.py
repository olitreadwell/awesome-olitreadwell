"""Invariants for this list. The rules live in the engine; these are the ones
that matter most for this readme, kept close to it."""

from __future__ import annotations

from pathlib import Path

from awesome_list.config.load_list_config import load_list_config
from awesome_list.github.github_stats import github_repo_slug
from awesome_list.parse.parse_readme import parse_readme
from awesome_list.rules.run_rules import run_rules

ROOT = Path(__file__).resolve().parents[1]


def document() -> tuple[object, str, object]:
    config = load_list_config(ROOT / "awesome.toml")
    text = (ROOT / config.readme).read_text(encoding="utf-8")
    return parse_readme(text, vocabulary=config.tags), text, config


def test_no_rule_errors() -> None:
    parsed, text, config = document()
    violations = run_rules(
        parsed, text, config.tags, file=config.readme, entry_sections=config.sections
    )
    errors = [violation.render() for violation in violations if violation.severity == "error"]

    assert errors == []


# Eleven links in the Visual Studio Code sections have no description yet. The
# words have to come from Oli, so the gate warns instead of failing, and this
# number must not grow. They are listed in docs/migration.md.
UNDESCRIBED_ENTRIES = 11


def test_entry_descriptions_that_still_need_a_human() -> None:
    """Missing descriptions are warnings, and this test keeps the count honest."""
    parsed, text, config = document()
    violations = run_rules(
        parsed, text, config.tags, file=config.readme, entry_sections=config.sections
    )
    missing = [
        violation.message
        for violation in violations
        if violation.rule == "entry-grammar" and "has no description" in violation.message
    ]

    assert len(missing) == UNDESCRIBED_ENTRIES, missing


def test_entry_count_does_not_shrink() -> None:
    parsed, _text, _config = document()

    assert len(parsed.entries) >= 55


def test_no_duplicate_urls() -> None:
    parsed, _text, _config = document()
    urls = [entry.url for entry in parsed.entries]

    assert len(urls) == len(set(urls))


def test_every_github_entry_is_in_the_stats_snapshot() -> None:
    parsed, _text, _config = document()
    snapshot = (ROOT / "github-stats.json").read_text(encoding="utf-8")

    for entry in parsed.entries:
        slug = github_repo_slug(entry.url)
        if slug is not None:
            assert slug in snapshot, entry.url
