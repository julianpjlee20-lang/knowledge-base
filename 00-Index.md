---
created: 2026-07-04
updated: 2026-07-04
type: resource
status: reference
tags: [PKM-System, index, PARA]
related: [AGENTS.md, CLAUDE.md]
---

# 00-Index — Vault 入口

本 vault 遵循 **strict PARA**。規則單一真相來源:[[AGENTS.md]](Claude Code 由 root 自動載入)。

## 資料夾結構

| 資料夾 | 用途 |
|---|---|
| `00-Inbox/` | 未分類、未處理的原始捕捉。不確定就先丟這裡並標 `status: needs-triage`。 |
| `01-Projects/` | 有明確產出、期限或交付物的進行中工作。 |
| `02-Areas/` | 無結束日期的持續責任(行政、提醒、維運）。 |
| `03-Resources/` | 可重用的知識、參考、方法、工具、範例。含 `PKM-System/`(vault 治理)。 |
| `04-Archives/` | 已完成、過期、歷史材料。含 `Agent Logs/`(agent 日誌、graphify 輸出）。 |

## 治理文件

- vault root `AGENTS.md` — 核心規則(PARA-CORE v1）
- vault root `CLAUDE.md` — Claude Code 指令(import AGENTS.md + 冗餘禁令)
- `03-Resources/PKM-System/` — 完整方案、外部評估、後續 validator/hook 規劃

## 各區索引

- `01-Projects/README.md`
- `02-Areas/README.md`
- `03-Resources/README.md`
- `04-Archives/README.md`
