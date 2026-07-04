---
created: 2026-07-04
updated: 2026-07-04
type: resource
status: reference
tags: [PKM-System, agents, governance, PARA, knowledge-base]
related: [CLAUDE.md, 00-Index.md, README.md]
---

# AGENTS.md — knowledge-base

## Role

This repository is Andy's formal Wiki / `knowledge-base` and the AI knowledge source of truth.
It is also opened by Obsidian as the human reading and editing interface.

This repo stores **what Andy knows**: Markdown knowledge pages, SOPs, indexes, summaries, project/area/resource/archive notes, and source links.
It is **not** the durable cross-agent memory repo.

## Source-of-Truth Boundaries

| Information type | Source of truth |
|---|---|
| Company raw/original files | Dropbox for Work / `C:/Users/user/Dropbox` |
| Human reading/editing interface | Obsidian on OneDrive Personal: `C:/Users/user/OneDrive/SecondBrain-Onedrive` |
| Formal Wiki / AI knowledge | GitHub `knowledge-base`: `https://github.com/julianpjlee20-lang/knowledge-base.git` |
| AI behavior memory and user preferences | GitHub `agents-memory`: `https://github.com/julianpjlee20-lang/agents-memory.git` |
| Code projects | Their own GitHub repos + repo-local `AGENTS.md` |

## PARA-CORE v2

### Allowed top-level folders only

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

## What Belongs Here

- Long-term Wiki pages
- Company/business knowledge summaries
- SOPs and workflows meant for humans and AI to read
- Project, area, resource, and archive notes
- Indexes and maps of content
- Markdown summaries of raw files with stable source links

## What Does Not Belong Here

- AI behavior memory or durable user preferences → put in `agents-memory`
- Bulk raw PDFs / Excel / scans → keep in Dropbox and link sources
- Agent-private long-term memory → use `agents-memory`
- Short-lived task logs, PR numbers, issue status, commit logs → do not store as durable Wiki unless intentionally archived

## Dropbox / Original File Rules

- Dropbox for Work / `C:/Users/user/Dropbox` is the raw company file layer.
- Agents may read Dropbox only when original evidence is needed.
- Do **not** delete, move, rename, or reorganize Dropbox originals without explicit approval.
- Prefer creating Markdown summaries in this repo with source paths.
- If duplicates are found, create/update `00-Inbox/Duplicate Report.md` first; do not clean originals automatically.

## Obsidian / OneDrive Rules

- Obsidian is the human interface, not a separate AI source of truth.
- This local vault is a Git working copy of `knowledge-base`.
- AI changes should be made in this repo, validated, then committed/pushed when appropriate.
- Do not create a separate OneDrive-only knowledge structure outside this repo.

## Note Standard

New Markdown knowledge notes should include:

```yaml
---
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: project | area | resource | archive | inbox | log
status: active | draft | reference | archived | needs-triage
tags: []
related: []
source: []
---
```

Recommended body:

```md
# Title

## 摘要

## 重點

## 判斷 / 結論

## 原始資料來源

## 相關頁面
```

## Classification

- `00-Inbox/`: unclear, unprocessed, AI drafts, processing queues.
- `01-Projects/`: active work with a clear outcome, deadline, or deliverable.
- `02-Areas/`: ongoing responsibility with no end date.
- `03-Resources/`: reusable knowledge, references, SOPs, vendors, tools, concepts.
- `04-Archives/`: inactive, completed, outdated, or historical material.

If uncertain, use `00-Inbox/` and set `status: needs-triage`.

## Indexing

After creating or moving important notes, update at least one relevant index:

- root `index.md` when present, or root `00-Index.md` for Obsidian navigation
- folder `README.md`
- a relevant MOC / map-of-content note

## Validation

Before finishing structural work, run:

```bash
python 03-Resources/PKM-System/scripts/validate-vault.py
```

If the validator cannot run, state clearly why validation was skipped.

## Related Governance Docs

- `03-Resources/PKM-System/AI Knowledge Architecture.md`
- `03-Resources/PKM-System/Source Linking Rules.md`
- `03-Resources/PKM-System/Dropbox Processing Workflow.md`
