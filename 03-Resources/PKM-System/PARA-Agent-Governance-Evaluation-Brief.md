---
created: 2026-07-04
updated: 2026-07-04
type: resource
status: reference
tags: [PARA, Obsidian, agents, second-brain, governance]
related: [AGENTS.md, CLAUDE.md, AI Knowledge Architecture]
source: []
---

# PARA Agent Governance Evaluation Brief

> 目的：這份文件是給 Claude、Codex、Hermes 或其他 AI agents 評估用的草案。  
> 核心問題：如何讓所有 agents 在整理 Obsidian 第二大腦時，遵守同一套嚴格 PARA Method，而不是各自產生不同資料夾與 index。

---

## 1. Current Problem

目前 Obsidian vault 中，曾出現 agent 自行建立或延伸的結構，例如：

```text
claude/
01-People/
04-Admin/ 或類似 admin/gov 資料夾提案
```

問題不是單一 agent 做錯，而是 vault 缺少一套所有 agent 都會遵守的「全域治理規則」。

結果是：

- 不同 agents 會依照自己的習慣整理筆記。
- 有些 agents 會建立自己的 root folder，例如 `claude/`。
- 有些 agents 會把 logs、resources、projects 混在一起。
- 沒有統一的 index 或 README 規則。
- 沒有明確限制 top-level folders。
- 沒有機制保證 Claude / Codex 每次啟動時都讀同一份規則。

---

## 2. Decision Direction

此 vault 應嚴格採用 PARA Method。

PARA 只允許以下主要分類：

1. Projects
2. Areas
3. Resources
4. Archives

可以保留 `00-Inbox/` 作為暫存 capture layer，但它不是 PARA 核心分類，只是實務上的收件箱。

---

## 3. Proposed Allowed Top-Level Structure

建議最終 root 結構如下：

```text
SecondBrain-Onedrive/
├── AGENTS.md
├── CLAUDE.md
├── 00-Index.md
├── 00-Inbox/
├── 01-Projects/
├── 02-Areas/
├── 03-Resources/
└── 04-Archives/
```

### Allowed Top-Level Folders

只允許：

```text
00-Inbox/
01-Projects/
02-Areas/
03-Resources/
04-Archives/
```

### Forbidden Top-Level Folders

不允許建立：

```text
People/
01-People/
Admin/
04-Admin/
claude/
hermes/
codex/
agent-output/
knowledge-base/
notes/
resources/  # lowercase duplicate
projects/   # lowercase duplicate
```

除非使用者明確指示，任何 agent 不得建立新的 root-level folder。

---

## 4. PARA Classification Rules

所有 agent 在建立、搬移、整理筆記前，必須先分類。

### 4.1 Projects

路徑：

```text
01-Projects/
```

定義：

有明確目標、期限、交付成果，且正在推進中的事情。

判斷問題：

- 這件事是否有完成標準？
- 是否有期限或階段性目標？
- 是否需要行動、追蹤、交付？

範例：

```text
01-Projects/建設公司網站/
01-Projects/LINE-OneDrive-Auto-Archive/
01-Projects/AI客服導入/
```

---

### 4.2 Areas

路徑：

```text
02-Areas/
```

定義：

長期維護的責任領域，沒有明確結束日期。

判斷問題：

- 這是否是一個需要持續維護的責任？
- 是否沒有單一完成點？
- 是否需要定期 review？

範例：

```text
02-Areas/Personal Knowledge Management/
02-Areas/Finance/
02-Areas/Health/
02-Areas/Business Operations/
02-Areas/Client Relationships/
```

注意：嚴格 PARA 下，不應有 root-level `People/`。人物、客戶、合作夥伴資料應依用途放入：

```text
02-Areas/Client Relationships/
```

或如果只是參考資料：

```text
03-Resources/People/
```

---

### 4.3 Resources

路徑：

```text
03-Resources/
```

定義：

未來可能會重複參考的知識、方法、工具、案例、讀書筆記、教學、reference materials。

判斷問題：

- 這是否是一個 topic / subject / knowledge asset？
- 未來是否可能被重複查閱？
- 它是否不是現在進行中的 project，也不是持續責任 area？

範例：

```text
03-Resources/AI Agents/
03-Resources/AI Agents/Claude/
03-Resources/AI Agents/Codex/
03-Resources/PKM-System/
03-Resources/Book Notes/
03-Resources/Construction Industry/
03-Resources/Accounting/
```

---

### 4.4 Archives

路徑：

```text
04-Archives/
```

定義：

已完成、過期、不再活躍、歷史保留的資料。

判斷問題：

- 這件事是否已完成？
- 是否不再需要主動維護？
- 是否只是保留作為歷史紀錄？

範例：

```text
04-Archives/Completed Projects/
04-Archives/Agent Logs/
04-Archives/Old Experiments/
04-Archives/Deprecated Systems/
```

---

### 4.5 Inbox

路徑：

```text
00-Inbox/
```

定義：

未整理、未分類、快速 capture 的暫存資料。

規則：

- 如果 agent 無法判斷分類，放入 `00-Inbox/`。
- 必須加上 `status: needs-triage`。
- 不應長期累積未處理內容。

---

## 5. Agent-Related Content Placement

### 5.1 AI Agent Resources

Claude、Codex、Hermes、OpenCode、BMAD、MCP、Skills 等工具與方法論，屬於 Resources。

應放：

```text
03-Resources/AI Agents/
```

例如：

```text
03-Resources/AI Agents/Claude/
03-Resources/AI Agents/Codex/
03-Resources/AI Agents/Hermes/
03-Resources/AI Agents/BMAD/
```

---

### 5.2 Agent Logs

Session logs、daily logs、weekly summaries、auto-sync records 通常屬於歷史紀錄。

應放：

```text
04-Archives/Agent Logs/
```

例如：

```text
04-Archives/Agent Logs/Claude/daily/
04-Archives/Agent Logs/Claude/weekly/
04-Archives/Agent Logs/Hermes/
```

除非這些 logs 是某個 active project 的一部分，才放進該 project folder。

---

### 5.3 Vault / PKM Governance

Vault rules、naming conventions、templates、agent rules、indexing policy，屬於長期參考資料。

應放：

```text
03-Resources/PKM-System/
```

例如：

```text
03-Resources/PKM-System/Vault-Rules.md
03-Resources/PKM-System/Agent-Rules.md
03-Resources/PKM-System/Naming-Conventions.md
03-Resources/PKM-System/Templates/
03-Resources/PKM-System/scripts/validate-vault.py
```

如果「維護第二大腦」本身被視為長期責任，也可另設：

```text
02-Areas/Personal Knowledge Management/
```

但具體規則與模板仍建議放在：

```text
03-Resources/PKM-System/
```

---

## 6. What To Do With Existing `claude/` Folder

目前 root-level `claude/` 不符合嚴格 PARA。

建議拆分：

### 6.1 Claude Resources

如果內容是 Claude / Claude Code 使用方法、最佳實踐、skills、MCP、agent workflow：

```text
claude/... → 03-Resources/AI Agents/Claude/
```

### 6.2 Claude Logs

如果內容是 daily logs、weekly summaries、session records、sync records：

```text
claude/daily-logs/ → 04-Archives/Agent Logs/Claude/daily/
claude/concepts/weekly-*.md → 04-Archives/Agent Logs/Claude/weekly/
claude/index.md → 04-Archives/Agent Logs/Claude/README.md
```

---

## 7. What To Do With Existing `01-People/` Folder

`01-People/` 不符合嚴格 PARA。

建議根據內容拆分：

### 7.1 Relationship Management

如果人物筆記與客戶、合作夥伴、團隊關係維護有關：

```text
01-People/... → 02-Areas/Client Relationships/
```

或：

```text
01-People/... → 02-Areas/Business Relationships/
```

### 7.2 Reference People Database

如果只是人物資料、背景、reference：

```text
01-People/... → 03-Resources/People/
```

---

## 8. Required Bootstrap Files For Agents

只把規則寫成普通 Obsidian note 不夠。不同 agents 有自己的啟動規則。

要讓 agents 每次都遵守同一套規範，root 必須有 bootstrap files。

### 8.1 `AGENTS.md`

用途：

通用 agent 入口，給 Codex、Hermes、OpenCode、其他 coding agents 讀取。

位置：

```text
AGENTS.md
```

內容應包含：

- 此 vault 採用 strict PARA。
- 只允許 `00-Inbox/`, `01-Projects/`, `02-Areas/`, `03-Resources/`, `04-Archives/`。
- 禁止建立新的 top-level folders。
- 禁止建立 `/claude`, `/01-People`, `/04-Admin`。
- 所有新增或搬移都要更新最近的 README 或 index。
- 不確定分類時放入 `00-Inbox/`。
- 結束前執行 validator。

---

### 8.2 `CLAUDE.md`

用途：

Claude Code 專用 project memory / project instructions。

位置：

```text
CLAUDE.md
```

Claude Code 從 vault root 啟動時，會自動讀取 project root 的 `CLAUDE.md`。

內容應包含：

- Read and follow `AGENTS.md`.
- This vault follows strict PARA.
- Do not create `/claude`.
- Claude resources go to `03-Resources/AI Agents/Claude/`.
- Claude logs go to `04-Archives/Agent Logs/Claude/`.
- Do not create new root folders.

---

### 8.3 `00-Index.md`

用途：

人類與 agents 的 vault navigation index。

位置：

```text
00-Index.md
```

內容應包含：

- PARA folder links
- active projects index
- active areas index
- key resource categories
- archive entry points
- link to `AGENTS.md`, `CLAUDE.md`, and `03-Resources/PKM-System/Vault-Rules.md`

---

## 9. How To Ensure Claude / Codex Read The Rules

### 9.1 Claude Code

啟動時必須從 vault root 開啟：

```bash
cd /c/Users/user/OneDrive/SecondBrain-Onedrive
claude
```

或更強制：

```bash
cd /c/Users/user/OneDrive/SecondBrain-Onedrive
claude --append-system-prompt-file AGENTS.md
```

注意：不要使用 `--bare`，因為 `--bare` 會跳過 `CLAUDE.md` 等 project context。

---

### 9.2 Codex

Codex 啟動時也應從 vault root 開啟：

```bash
cd /c/Users/user/OneDrive/SecondBrain-Onedrive
codex exec "Read AGENTS.md first and follow strict PARA. Then do this task: <task>"
```

建議建立 wrapper script，避免每次手動提醒。

例如：

```bash
#!/usr/bin/env bash
set -euo pipefail
cd "/c/Users/user/OneDrive/SecondBrain-Onedrive"
codex exec "Read AGENTS.md first and follow strict PARA. Do not create new top-level folders. User task: $*"
```

以後使用：

```bash
sbcodex "整理 inbox"
```

---

### 9.3 Hermes / Other Agents

任何 agent 都應以 vault root 作為工作目錄，並先讀：

```text
AGENTS.md
00-Index.md
03-Resources/PKM-System/Vault-Rules.md
```

若工具允許設定 workdir，應設定為：

```text
C:/Users/user/OneDrive/SecondBrain-Onedrive
```

---

## 10. Required Frontmatter

所有新 markdown notes 應包含：

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

### Type Rules

- `project`: belongs under `01-Projects/`
- `area`: belongs under `02-Areas/`
- `resource`: belongs under `03-Resources/`
- `archive`: belongs under `04-Archives/`
- `inbox`: belongs under `00-Inbox/`
- `log`: usually belongs under `04-Archives/Agent Logs/`, unless attached to an active project

---

## 11. Indexing Rules

Every major PARA folder should have a README:

```text
01-Projects/README.md
02-Areas/README.md
03-Resources/README.md
04-Archives/README.md
```

Optional:

```text
00-Inbox/README.md
```

When adding or moving notes, agents should update the nearest relevant README or index.

Examples:

- New active project → update `01-Projects/README.md`
- New resource category → update `03-Resources/README.md`
- New AI agent resource → update `03-Resources/AI Agents/README.md`
- New archived agent log folder → update `04-Archives/Agent Logs/README.md`

---

## 12. Naming Rules

### Dated Notes

Use:

```text
YYYY-MM-DD-topic.md
```

Example:

```text
2026-07-04-agent-governance-review.md
```

### Evergreen Notes

Use clear topic names:

```text
PARA-Method.md
Vault-Rules.md
Claude-Code-Best-Practices.md
```

### Avoid

Avoid vague or agent-specific names:

```text
notes.md
new.md
summary.md
claude-output.md
agent-result.md
```

---

## 13. Validation Requirement

Prompt rules are not enough. Agents may still make mistakes.

建議建立 validator：

```text
03-Resources/PKM-System/scripts/validate-vault.py
```

Validator 應檢查：

- 是否有非法 root-level folders。
- 是否出現 `claude/`, `01-People/`, `04-Admin/`。
- 是否有 markdown notes 缺少 frontmatter。
- 是否有新增 note 但沒有更新相應 README。
- 是否有 Resources / Projects / Areas / Archives 混放。

每個 agent 任務結束前應執行：

```bash
python 03-Resources/PKM-System/scripts/validate-vault.py
```

或在 Windows/Git Bash 環境：

```bash
python 03-Resources/PKM-System/scripts/validate-vault.py
```

---

## 14. Proposed Final Structure

```text
SecondBrain-Onedrive/
├── AGENTS.md
├── CLAUDE.md
├── 00-Index.md
├── 00-Inbox/
│   └── README.md
├── 01-Projects/
│   └── README.md
├── 02-Areas/
│   ├── README.md
│   ├── Personal Knowledge Management/
│   ├── Business Operations/
│   └── Client Relationships/
├── 03-Resources/
│   ├── README.md
│   ├── AI Agents/
│   │   ├── README.md
│   │   ├── Claude/
│   │   ├── Codex/
│   │   └── Hermes/
│   ├── PKM-System/
│   │   ├── Vault-Rules.md
│   │   ├── Agent-Rules.md
│   │   ├── Naming-Conventions.md
│   │   ├── Templates/
│   │   └── scripts/
│   ├── Book Notes/
│   └── People/
└── 04-Archives/
    ├── README.md
    ├── Agent Logs/
    │   ├── README.md
    │   └── Claude/
    │       ├── daily/
    │       └── weekly/
    ├── Completed Projects/
    └── Deprecated Systems/
```

---

## 15. Agent Evaluation Questions

請評估以下問題：

1. 這套 strict PARA folder structure 是否合理？
2. 是否應保留 `00-Inbox/`？如果保留，它的治理規則是否足夠？
3. `01-People/` 應搬到 `02-Areas/Client Relationships/` 還是 `03-Resources/People/`？是否需要拆分？
4. 現有 `claude/` folder 應如何拆分到 `03-Resources/AI Agents/Claude/` 與 `04-Archives/Agent Logs/Claude/`？
5. `AGENTS.md` 與 `CLAUDE.md` 是否足以讓 agents 每次遵守規則？
6. 是否需要 wrapper scripts，例如 `sbclaude`、`sbcodex`，強制從 vault root 啟動？
7. Validator 應檢查哪些項目？
8. 是否應將 `03-Ideas/` rename 為 `03-Resources/`？如果要改，如何避免破壞 Obsidian links？
9. 現有 `05-Archive/` 是否應 rename 為 `04-Archives/`？如何處理既有 links？
10. 是否應先建立 governance files，再進行搬移？

---

## 16. Recommended Migration Order

建議不要直接大搬移。先建立治理層，再逐步整理。

### Phase 1 — Governance First

1. 建立 `AGENTS.md`
2. 建立 `CLAUDE.md`
3. 建立 `00-Index.md`
4. 建立 `03-Resources/PKM-System/Vault-Rules.md`
5. 建立 `03-Resources/PKM-System/Agent-Rules.md`
6. 建立 validator script 草案

### Phase 2 — Create PARA Indexes

1. 建立 `01-Projects/README.md`
2. 建立 `02-Areas/README.md`
3. 建立 `03-Resources/README.md`
4. 建立 `04-Archives/README.md`

### Phase 3 — Migrate Agent-Specific Folders

1. 拆分 `claude/`
2. 搬移 Claude resources
3. 搬移 Claude logs
4. 移除 root-level `claude/`

### Phase 4 — Resolve Non-PARA Folders

1. 分析 `01-People/` 內容
2. 拆到 `02-Areas/Client Relationships/` 或 `03-Resources/People/`
3. 移除 root-level `01-People/`

### Phase 5 — Rename Existing Folders If Needed

目前 vault 似乎有：

```text
03-Ideas/
05-Archive/
```

若要嚴格 PARA，建議改成：

```text
03-Resources/
04-Archives/
```

但 rename 前必須評估 Obsidian wikilinks、外部引用、Git history、agent scripts 是否會受影響。

---

## 17. Non-Negotiable Rules

以下規則建議作為最終硬性規則：

1. This vault follows strict PARA.
2. No new top-level folders unless explicitly approved by the user.
3. Do not create `/claude`, `/hermes`, `/codex`, `/agent-output`.
4. Do not create `/01-People`.
5. Do not create `/04-Admin` if strict PARA is required.
6. Agent resources go under `03-Resources/AI Agents/`.
7. Agent logs go under `04-Archives/Agent Logs/`.
8. Vault rules go under `03-Resources/PKM-System/`.
9. If uncertain, use `00-Inbox/` with `status: needs-triage`.
10. Update relevant README/index after creating or moving notes.
11. Run validator before finishing.

---

## 18. Short Version For Agents

If you are an AI agent reading this, follow this summary:

```text
This vault uses strict PARA.
Allowed root folders: 00-Inbox, 01-Projects, 02-Areas, 03-Resources, 04-Archives.
Do not create new root folders.
Do not create claude/, hermes/, codex/, 01-People/, or 04-Admin/.
Classify every note before moving or creating it.
Projects = active outcomes.
Areas = ongoing responsibilities.
Resources = reusable knowledge/reference.
Archives = inactive or historical material.
Inbox = unclear/unprocessed capture only.
Agent resources belong in 03-Resources/AI Agents/.
Agent logs belong in 04-Archives/Agent Logs/.
Vault rules belong in 03-Resources/PKM-System/.
If unsure, put it in 00-Inbox with status: needs-triage.
Update README/index after changes.
Run validator before finishing.
```
