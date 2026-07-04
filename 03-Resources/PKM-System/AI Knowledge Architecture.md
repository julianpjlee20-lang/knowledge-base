---
created: 2026-07-04
updated: 2026-07-04
type: resource
status: reference
tags: [PKM-System, knowledge-architecture, agents, PARA]
related: [AGENTS.md, Source Linking Rules, Dropbox Processing Workflow]
source: [Downloads/Telegram Desktop/AI-Knowledge-Architecture.md]
---

# AI Knowledge Architecture

## 一句話總結

Dropbox for Work 放公司原始資料；OneDrive Personal 用來跑 Obsidian；Obsidian 是人類閱讀與編輯 Wiki 的工具；GitHub `knowledge-base` 是正式 Wiki 與 AI 知識來源；GitHub `hermes-memory` 是所有 AI agents 的共同記憶與行為規則。

## 核心區分

```text
Dropbox = 原始資料
OneDrive = 個人同步與 Obsidian 使用
Obsidian = 人類操作介面
GitHub knowledge-base = 正式 Wiki / AI source of truth
GitHub hermes-memory = AI 行為記憶 / 跨 agent 規則
```

```text
knowledge-base = 你知道什麼
hermes-memory = AI 應該怎麼服務你
```

## 整體層級

```text
[原始檔案層]
Dropbox for Work / Local / OneDrive Personal attachments
        │
        ▼
[整理處理層]
Human / Hermes / Cowork / Claude
摘要、分類、去重、判斷、轉 Markdown、建立來源連結
        │
        ▼
[Wiki 內容層]
GitHub knowledge-base
Markdown notes / SOP / Index / Links / PARA structure
        ▲
        │ 人類使用
[Obsidian]
閱讀、編輯、雙向連結、graph、daily notes、思考介面
        │
        ▼
[AI 使用層]
Hermes / Claude Code / Cowork / ChatGPT
讀取 knowledge-base + hermes-memory
```

## Source of Truth

| 類型 | Source of truth |
|---|---|
| 公司原始檔案 | Dropbox for Work / `C:/Users/user/Dropbox` |
| 人類閱讀與編輯介面 | Obsidian on OneDrive Personal |
| 正式知識庫 / Wiki | GitHub `knowledge-base` |
| AI agents 長期規則與偏好 | GitHub `hermes-memory` |
| 程式碼專案 | 各自 GitHub repo + repo 內 `AGENTS.md` |

## Agent 使用規則

Agents should prioritize:

1. `knowledge-base` for long-term knowledge.
2. `hermes-memory` for user preferences and behavior rules.
3. Dropbox only when original evidence is needed.

Agents should not:

- directly reorganize Dropbox originals;
- directly edit a separate OneDrive-only vault;
- create their own long-term memory;
- put task logs into `hermes-memory`;
- bulk-copy raw files into `knowledge-base`.

## Data Flow — Dropbox 文件變成 Wiki

```text
Dropbox for Work 原始檔
→ Hermes / Cowork read-only review
→ 摘要 / OCR / 分類 / 去重
→ 產出 Markdown draft
→ 放入 knowledge-base/00-Inbox
→ Human review
→ 移入 02-Areas 或 03-Resources
→ 在 note 中保留 Dropbox 來源
→ git commit / push
```

## Data Flow — Obsidian 編輯 Wiki

```text
你在 Obsidian 編輯 knowledge-base working copy
→ 確認 OneDrive / Git 狀態
→ git commit / push 到 GitHub knowledge-base
→ AI agents 從 GitHub knowledge-base 讀取最新版
```

## Data Flow — AI 修改 Wiki

```text
Hermes / Cowork / Claude 修改 Markdown
→ 更新 relevant index / README
→ run validator
→ git commit
→ git push
→ Obsidian 端 pull / sync
```
