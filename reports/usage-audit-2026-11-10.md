# Usage audit, 10 November 2026

Scope: this Mac and the local Codex session store. Read-only evidence, used to
choose which entries belong in `readme.md`.

## Sources

- Homebrew: `brew list --formula`, `brew list --cask`, `brew tap`.
- Applications: `/Applications` and `mdfind` for VS Code and Windsurf.
- Editors: `code --list-extensions`, `~/.vscode/extensions`.
- Shell: `~/.zsh_history`, `~/.local/bin`, `~/code`.
- Codex: 1,100 JSONL files under `~/.codex/sessions`, 1,111 session records.
- Existing Oli notes: `~/Library/Mobile Documents/com~apple~CloudDocs/oli`
  and `~/Library/Mobile Documents/com~apple~CloudDocs/career`.
- Upstream sources: GitHub repository metadata and each project's own page.

## Codex evidence

Top working directories:

| Directory | Sessions |
| --- | ---: |
| `~/code/open-data/uk-open-data-lab-private` | 304 |
| `~/code/open-data/usa-open-data-lab-private` | 245 |
| `~/code/open-data/nz-open-data-lab-private` | 131 |
| `~/code/open-data` | 81 |
| `~/Library/Mobile Documents/com~apple~CloudDocs/career` | 81 |
| `~/code/tech-for-good` | 65 |
| `~/code` | 63 |

Command volume in the session files:

| Signal | Count |
| --- | ---: |
| `exec_command` calls | 95,037 |
| User messages | 4,334 |
| `gh` first token | 1,835 |
| `python3` first token | 2,890 |
| `node` first token | 3,451 |
| `npm` first token | 3,093 |
| `uv` first token | 123 |
| `osxphotos` first token | 74 |

The open-data labs are the centre of gravity. The list previously had one NZ
data link and no open-data section.

Skill and workflow references in the session text, including pasted skill
documents:

| Route | Mentions |
| --- | ---: |
| `caveman` | 3,284 |
| `tdd` | 1,420 |
| `code-review` | 1,218 |
| `writing-for-agents` | 1,190 |
| `research` | 1,185 |
| `prototype` | 1,180 |
| `codebase-design` | 1,178 |
| `diagnosing-bugs` | 1,163 |
| `domain-modeling` | 1,161 |
| `frontend-audit` | 692 |
| `clarity` | 114 |
| `retro` | 69 |

These counts are inflated by skill text pasted into sessions. They are useful
as a ranking, not as a precise usage count.

## Editor and app evidence

- VS Code is not installed: `/Applications/Visual Studio Code.app` is absent,
  `mdfind` finds no bundle, and `code --list-extensions` prints nothing.
- Orca, Devin, Claude, iTerm, Lite XL, Raycast, Rectangle, 1Password,
  Tailscale, Brave, Firefox, Chrome, darktable and Ollama are installed.
- Windsurf has no standalone app, but `~/.codeium` and Devin logs include the
  Windsurf extension. It was kept in the list because it may still be used
  through Devin.

## Research: Addy Osmani and Matt Pocock

### Addy Osmani

Repository: <https://github.com/addyosmani/agent-skills>

- Description: "Production-grade engineering skills for coding agents."
- Relevant skills: `source-driven-development`, `context-engineering`,
  `documentation-and-adrs`, `test-driven-development`,
  `code-review-and-quality`, `browser-testing-with-devtools`.
- Used here for source hierarchy, recording the migration decision, and keeping
  the readme as the single source of truth.

Repository: <https://github.com/addyosmani/clarity>

- Description: "Clarity - an Agent skill for clearer writing."
- Used in the Codex sessions for LinkedIn and landing-page rewrites.

### Matt Pocock

Repository: <https://github.com/mattpocock/skills>

- Description: "Skills for Real Engineers. Straight from my .agents directory."
- Installed locally, including `retro`, `writing-for-agents`, `tdd`,
  `code-review`, `domain-modeling`, `codebase-design`, `to-spec`,
  `to-tickets`, `implement` and `setup-matt-pocock-skills`.
- Used here for the retro lens: turn repeated work into a better environment,
  not a one-off manual fix. The list changes follow that rule.

## Actions taken

| Action | Entry | Evidence |
| --- | --- | --- |
| Added | Codex CLI | 1,100 local sessions; primary agent in the logs |
| Added | Claude Code | Installed cask; 3,590 mentions in session text |
| Added | mattpocock/skills | Installed; `retro` runs across the repo fleet |
| Added | addyosmani/clarity | Installed; used for writing rewrites |
| Added | uv, Ruff, mise, GitHub CLI, Playwright | Installed and present in command history |
| Added | data.govt.nz, data.gov.uk, Data.gov, Stats NZ, ONS | Most Codex work is open data |
| Added | darktable, ExifTool, osxphotos | Installed; photography sessions and commands |
| Added | 1Password, Tailscale | Installed system-wide |
| Moved | WikiNewZealand/new-zealand-data | Belongs with open data, not Wellington |
| Removed | Visual Studio Code section | No app, no extensions, no session evidence |
| Kept | Windsurf | Extension may still be used through Devin |

## Not added yet

These are real candidates, but they need Oli's own one-line description or a
decision that they belong in a public list:

- iTerm2, Lite XL, Raycast, Rectangle, Espanso.
- Brave, Firefox, Chrome, Surfshark, qBittorrent, Adblock Plus.
- Docker, PostgreSQL, Redis, SQLite.
- ffmpeg, dupeguru, Mixxx, IINA.
- AgentsView, Anarlog, opencode, llmfit.
- Open data APIs and connectors built in the private labs.

## Follow-up

- Refresh the GitHub stats snapshot after adding repositories.
- Decide whether Windsurf stays as "My IDE" now that Devin is the installed
  app.
- Replace any copied upstream description with Oli's own words when he has
  time. The readme rule still says the descriptions are his.
