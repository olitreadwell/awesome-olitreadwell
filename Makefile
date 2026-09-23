SHELL := /bin/bash
.DEFAULT_GOAL := check

.PHONY: check check-fast list-check toc toc-check stats stats-check sources test links fix hooks-install

check: list-check toc-check stats-check test

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

links:
	lychee --config lychee.toml readme.md

hooks-install:
	git config core.hooksPath .githooks
