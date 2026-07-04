---
created: 2026-07-04
updated: 2026-07-04
type: resource
status: reference
tags: [PKM-System, agents, governance, PARA]
related: [CLAUDE.md]
---

# Agent Rules for This Obsidian Vault

## PARA-CORE v1

This vault follows strict PARA.

### Allowed root folders only

- `00-Inbox/`
- `01-Projects/`
- `02-Areas/`
- `03-Resources/`
- `04-Archives/`

Do not create any other top-level folders.

### Forbidden root folders

- `claude/`
- `hermes/`
- `codex/`
- `agent-output/`
- `knowledge-base/`
- `People/`
- `01-People/`
- `Admin/`
- `04-Admin/`

## Classification

Before creating or moving any note, classify it:

- `01-Projects/`: active work with a clear outcome, deadline, or deliverable.
- `02-Areas/`: ongoing responsibility with no end date.
- `03-Resources/`: reusable knowledge, references, methods, tools, examples.
- `04-Archives/`: inactive, completed, outdated, or historical material.
- `00-Inbox/`: unclear or unprocessed capture only.

If uncertain, use `00-Inbox/` and set `status: needs-triage`.

## Agent Content

- Agent resources go under `03-Resources/AI Agents/`.
- Agent logs go under `04-Archives/Agent Logs/`.
- Vault rules and PKM system docs go under `03-Resources/PKM-System/`.

## Required Frontmatter

New markdown notes should include:

```yaml
---
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: project | area | resource | archive | inbox | log
status: active | draft | reference | archived | needs-triage
tags: []
related: []
---
```

Note: governance files such as `AGENTS.md` and `CLAUDE.md` themselves use
`type: resource` so they do not trip the validator.

## Indexing

After creating or moving notes, update the nearest relevant `README.md` or index.

Required indexes:

- `00-Index.md`
- `01-Projects/README.md`
- `02-Areas/README.md`
- `03-Resources/README.md`
- `04-Archives/README.md`

## Validation

Before finishing, run the vault validator if available:

```bash
python 03-Resources/PKM-System/scripts/validate-vault.py
```

If the validator does not exist yet, state clearly that validation was skipped.

## Full Reference

Detailed rules, examples, templates, and migration plans belong under:
`03-Resources/PKM-System/`
