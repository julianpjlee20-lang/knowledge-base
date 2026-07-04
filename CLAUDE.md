---
created: 2026-07-04
updated: 2026-07-04
type: resource
status: reference
tags: [PKM-System, claude-code, governance]
related: [AGENTS.md]
---

@AGENTS.md

# Claude Code Instructions

This Obsidian vault follows strict PARA.
The imported `AGENTS.md` rules are mandatory for all Claude Code work in this vault.

## Cross-Agent Memory Source of Truth

This repository is Andy's knowledge-base / Obsidian vault, not the durable memory repo.

Before making durable assumptions about Andy, read:

- `/opt/data/hermes-memory/AGENTS.md`
- `/opt/data/hermes-memory/MEMORY.md`

GitHub source of truth:

- `https://github.com/julianpjlee20-lang/hermes-memory`

When updating durable user preferences, identity, agent behavior, or environment facts, update and push the `hermes-memory` repo. Do not create a separate Claude-only memory inside this knowledge-base repo.

## Core Non-Negotiables (redundant safety, in case the import fails)

- Do not create new top-level folders.
- Do not create `claude/`, `hermes/`, `codex/`, `01-People/`, or `04-Admin/`.
- Allowed root folders only: `00-Inbox/`, `01-Projects/`, `02-Areas/`,
  `03-Resources/`, `04-Archives/`.
- If unsure where a note belongs, put it in `00-Inbox/` with `status: needs-triage`.
- After creating or moving notes, update the nearest relevant `README.md` or index.

Full rules and detailed governance live in `AGENTS.md` and `03-Resources/PKM-System/`.
