---
created: 2026-07-04
updated: 2026-07-04
type: resource
status: reference
tags: [PKM-System, Dropbox, workflow, processing]
related: [AI Knowledge Architecture, Source Linking Rules, Dropbox Processing Queue, Duplicate Report]
source: [Downloads/Telegram Desktop/AI-Knowledge-Architecture.md]
---

# Dropbox Processing Workflow

## Goal

把 Dropbox for Work 原始資料整理成可讀、可搜尋、可被 AI 使用的 Markdown Wiki note，同時保留原始證據與避免破壞原始檔。

## Non-Negotiables

- Dropbox originals are read-only by default.
- No deletion, move, rename, or dedupe cleanup without explicit human approval.
- Create Wiki summaries with source links instead of copying raw files.
- Process in small batches; do not do one big migration.

## Workflow

1. Select a small Dropbox source folder.
2. Add the source to `00-Inbox/Dropbox Processing Queue.md`.
3. Inventory files read-only.
4. Detect duplicates by filename, hash, then semantic similarity if needed.
5. Record duplicate candidates in `00-Inbox/Duplicate Report.md`.
6. Create Markdown drafts in `00-Inbox/`.
7. Use standard frontmatter with `source:`.
8. Human review.
9. Move approved notes to `02-Areas/` or `03-Resources/`.
10. Update `00-Index.md` / relevant folder `README.md`.
11. Run validator.
12. Commit and push after review.

## First Pilot Recommendation

Start with one small vendor or SOP folder before processing contracts or finance-heavy folders.
