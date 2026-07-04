---
created: 2026-07-04
updated: 2026-07-04
type: resource
status: reference
tags: [PKM-System, source-links, Dropbox, governance]
related: [AI Knowledge Architecture, Dropbox Processing Workflow]
source: [Downloads/Telegram Desktop/AI-Knowledge-Architecture.md]
---

# Source Linking Rules

## Purpose

讓 Wiki note 能回到原始證據，同時避免把大量原始檔塞進 GitHub `knowledge-base`。

## Rules

1. 每一篇由 Dropbox 原始資料整理出的 note 必須保留 frontmatter `source:`。
2. `source:` 優先使用穩定、可複查的 Dropbox path。
3. Body 裡也要有 `## 原始資料來源`，列出人類可讀的來源。
4. 大型 PDF / Excel / scans 原則上留在 Dropbox，不直接放入 `knowledge-base`。
5. 如果內容是 AI 摘要，先標記 `status: draft` 或 `status: needs-triage`。
6. 涉及敏感資料時，只保留必要摘要與來源位置，不複製全文。
7. 若來源疑似重複，先更新 `00-Inbox/Duplicate Report.md`，不要直接刪檔。

## Source Format Examples

```yaml
source:
  - C:/Users/user/Dropbox/向上建設/公司資料/廠商/Example Vendor/報價單.pdf
  - Dropbox for Work/公司資料/合約/Example Contract.pdf
```

## Recommended Note Section

```md
## 原始資料來源

- `C:/Users/user/Dropbox/.../報價單.pdf`
- 摘要日期：YYYY-MM-DD
- 處理者：Hermes / Cowork / Human
```
