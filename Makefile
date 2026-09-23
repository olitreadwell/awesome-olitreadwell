SHELL := /bin/bash
.DEFAULT_GOAL := check

.PHONY: check check-fast list-check toc toc-check stats stats-check sources \
	export export-check submission-check compliance-audit links links-diff \
	test fix hooks-install

check: list-check toc-check stats-check export-check test

check-fast: list-check toc-check

list-check:
	uv run --project . python -m awesome_list.cli.run_list_check

toc:
	uv run --project . python -m awesome_list.cli.run_toc

toc-check:
	uv run --project . python -m awesome_list.cli.run_toc --check

stats:
	uv run --project . python -m awesome_list.cli.run_stats

stats-check:
	uv run --project . python -m awesome_list.cli.run_stats --check

sources:
	uv run --project . python -m awesome_list.cli.run_sources

test:
	uv run --project . pytest

export:
	uv run --project . python -m awesome_list.cli.run_export

export-check:
	uv run --project . python -m awesome_list.cli.run_export --check

submission-check:
	uv run --project . python -m awesome_list.cli.run_submission_check

compliance-audit:
	uv run --project . python -m awesome_list.cli.run_compliance_audit

links:
	uv run --project . python -m awesome_list.cli.run_links

links-diff:
	uv run --project . python -m awesome_list.cli.run_links --diff

hooks-install:
	git config core.hooksPath .githooks
