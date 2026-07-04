---
created: 2026-07-04
updated: 2026-07-04
type: resource
status: reference
tags: [PKM-System, claude-code, governance, knowledge-base]
related: [AGENTS.md]
---

@AGENTS.md

# Claude Code Instructions

This repository is Andy's formal `knowledge-base` Wiki and Obsidian human interface.
The imported `AGENTS.md` rules are mandatory for all Claude Code work in this repo.

## Core Fallback Rules

- Use strict PARA top-level folders only: `00-Inbox/`, `01-Projects/`, `02-Areas/`, `03-Resources/`, `04-Archives/`.
- Do not create root folders such as `claude/`, `hermes/`, `codex/`, `People/`, `01-People/`, `Admin/`, or `04-Admin/`.
- Do not delete, move, or rename Dropbox originals.
- Keep raw company files in Dropbox; create Markdown summaries with source links here.
- Put AI behavior memory and durable user preferences in `hermes-memory`, not this repo.
- If unsure where a note belongs, put it in `00-Inbox/` with `status: needs-triage`.
- Update the relevant index/README when adding important pages.

## Memory Repo

For durable cross-agent preferences and behavior rules, use:

- GitHub: `https://github.com/julianpjlee20-lang/hermes-memory`
- Local Windows path: `C:/Users/user/hermes-memory`
