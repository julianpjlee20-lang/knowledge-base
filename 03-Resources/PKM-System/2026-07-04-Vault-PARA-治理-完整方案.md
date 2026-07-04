---
created: 2026-07-04
updated: 2026-07-04
type: resource
status: reference
tags: [PARA, Obsidian, claude-code, cowork, governance, plan]
related: [AGENTS.md, CLAUDE.md]
---

# Vault PARA 治理 — 完整討論結論與實施方案

> 目標:讓 AI agents 整理 Obsidian Second Brain 時嚴格遵守同一套 strict PARA 規則,
> 規則只維護一份(`AGENTS.md`),不需要手動同步多個系統。
> Vault 位置:`C:\Users\user\OneDrive\SecondBrain-Onedrive`

---

## 1. 核心結論(TL;DR)

1. **單一真相來源**:所有規則只寫在 `AGENTS.md`;`CLAUDE.md` 用 `@AGENTS.md` import + 冗餘核心禁令。
2. **Claude Code 全自動**:從 vault root 啟動即自動載入,改 `AGENTS.md` 自動生效,零手動同步。
3. **Cowork 直連 vault 資料夾**即可讀寫檔案,不需要 MCP;規則需開場提一句(半自動)。
4. **網頁對話介面(claude.ai)永遠碰不到本機 vault**,不論任何設定。它負責討論規劃、產出檔案,由使用者手動搬入。
5. **instructions 是 context,不是硬性 enforcement**;真正防呆靠 hook + validator(後續階段)。

---

## 2. 三個環境的能力與分工(最終定案)

| 能力 | 網頁對話(claude.ai) | Cowork desktop | Claude Code |
|---|---|---|---|
| 讀 vault 檔案 | ❌(除非上傳) | ✅(資料夾加入工作區) | ✅ |
| 直接寫入/修改 vault | ❌ | ✅ | ✅ |
| 自動遵守 PARA 規則 | ❌ | ⚠️ 開場提一句 | ✅ 全自動(CLAUDE.md) |
| 更新 AGENTS.md 後 | — | — | ✅ 自動生效 |
| 適合的工作 | 討論、規劃、研究、產檔 | 日常筆記、輕整理 | 大整理、遷移、validator |

### `n:` 快速記錄的實際行為

- `n:` 是 user preferences 裡的**指示**,不等於寫入**管道**。
- 在 **Claude Desktop / Cowork**(有 Obsidian MCP 或本機檔案存取)→ 一句話直接落地 vault。
- 在**網頁對話** → 只能格式化筆記 + 產 md 檔供下載,需手動放入 `00-Inbox/`。
- 結論:`n:` 完整體驗留在本機工具使用。

### 已否決的方案

- **OneDrive MCP**:社群 server 多為本機 stdio,雲端 Cowork 連不到;自建遠端 HTTP 版
  成本高(Azure 註冊 + 部署維護),且仍需 preferences 觸發才會去讀 → 殺雞用牛刀,否決。
- **微軟官方 OneDrive MCP**:綁 Agent 365 / Copilot 授權,個人情境不適用。
- **為 Cowork 同步規則到 preferences**:非必要,Cowork 直連資料夾即可。
- **Git push 路徑**(經 second-brain repo):需交付 token,憑證進對話紀錄,不建議。

---

## 3. 檔案架構

```text
SecondBrain-Onedrive/           ← 從這裡啟動 Claude Code
├── AGENTS.md                   ← 唯一真相來源(短、硬、核心規則)
├── CLAUDE.md                   ← @AGENTS.md import + 冗餘禁令,永遠不用改
├── 00-Index.md
├── 00-Inbox/
├── 01-Projects/
├── 02-Areas/
├── 03-Resources/
│   └── PKM-System/             ← 詳細規則、範例、模板、validator、本文件
└── 04-Archives/
```

設計原則(採納外部 agent 回饋後定案):

- `CLAUDE.md` 不只放一行 import,**補 3–5 條核心禁令作冗餘**——import 失敗時仍有底線。
- `AGENTS.md` 要**短、硬**,只放核心規則;長篇論述放 `03-Resources/PKM-System/`,
  因為規則檔越長、模型遵循率越低。
- 硬規則帶版本號(`PARA-CORE v1`),核心規則變動時 +1,方便追蹤。
- 治理檔本身也要有 frontmatter(`type: resource`),避免被自己的 validator 判違規。
- frontmatter 範例必須包在 yaml code block 內,避免污染 Obsidian 解析。

---

## 4. 最終版 `CLAUDE.md`(放 vault root)

見 vault root 的 `CLAUDE.md`。

## 5. 最終版 `AGENTS.md`(放 vault root)

見 vault root 的 `AGENTS.md`。

---

## 6. Claude Code 啟動與正確性保證

Claude Code 沒有「連結 vault」的概念,行為完全取決於**啟動時的當前工作目錄(cwd)**,
從 cwd 遞迴向上尋找並自動載入 `CLAUDE.md`。

### 保證 cwd 正確(由弱到強)

1. **wrapper script `sbclaude`**:
   ```bash
   #!/usr/bin/env bash
   cd "/c/Users/user/OneDrive/SecondBrain-Onedrive" && claude "$@"
   ```
2. **專屬捷徑(建議)**:把 wrapper 綁成桌面捷徑 / 開始選單 / VS Code task,
   「開 vault 的 Claude Code」變成一個按鈕,不靠記憶。
3. 不建議全域改 shell `claude` 指令——會影響其他專案(ERP、Hermes 等)的使用。

注意事項:

- **不要**使用 `--bare`(會跳過 CLAUDE.md 等 project context)。
- 不需要 `--append-system-prompt-file`。

### 驗證規則已載入(三層)

1. **每次開場問一句(10 秒)**:
   「你現在載入了哪些 vault 規則?列出 PARA 的 allowed root folders。」
   答得出五個資料夾 = CLAUDE.md 生效。
2. **首次設定驗證 import**:
   「AGENTS.md 裡的 forbidden root folders 有哪些?」
   - 答得出完整清單(含 hermes/、codex/、agent-output/)= `@AGENTS.md` import 成功
   - 只答得出 CLAUDE.md 本體那幾條 = import 失敗,只有冗餘禁令在起作用
3. **客觀證據**:留意啟動畫面 / `/context` 是否列出已載入 `CLAUDE.md`。

---

## 7. 防護層次(instructions ≠ enforcement)

`CLAUDE.md` / `@AGENTS.md` 是 context 注入:模型會讀、通常遵守,
但**不是作業系統層級的強制禁止**。完整防護分三層:

```text
第一層:CLAUDE.md + AGENTS.md   → 讓模型「知道」規則(context)      ← 本階段
第二層:PreToolUse hook          → 動作前「攔截」違規(真 enforcement) ← 最終目標
第三層:validate-vault.py        → 事後「稽核」漏網(safety net)
```

- **hook** 比 validator 更符合「不想手動」的需求:`PreToolUse` 可在 Claude Code
  實際建立資料夾之前用程式碼攔截(例如發現要建 `01-People/` 直接擋下);
  `SessionStart` hook 可檢查 cwd 是否在 vault 內。
- 第一階段先做第一層即可;hook 設定格式需查最新 Claude Code 文件再實作,避免過時寫法。

---

## 8. 維護流程

1. 需要調整規則 → **只編輯 `AGENTS.md`**。
2. 改**細節/範例**(99% 情況)→ 完成,Claude Code 下次 session 自動生效。
3. 改**核心硬規則**(極少數)→ `PARA-CORE v1` 版本號 +1。
4. `CLAUDE.md` 永遠不用動。
5. Cowork 直連資料夾操作,無需為它同步任何東西。

---

## 9. 實施 Checklist

- [x] 將 `CLAUDE.md` 放入 vault root
- [x] 將 `AGENTS.md` 放入 vault root
- [ ] 開新 Claude Code session,執行 import 驗證(第 6 節第 2 項)
- [ ] (選用)建立 `sbclaude` wrapper + 桌面捷徑
- [x] 確認 Cowork 已連結 vault 資料夾
- [x] 本文件歸檔至 `03-Resources/PKM-System/`

## 10. 後續待辦(非本階段)

- [ ] `validate-vault.py` validator(檢查:非法 root folder、缺 frontmatter、
      分類混放、README 未更新)
- [ ] Claude Code hooks(`SessionStart` 檢查 cwd、`PreToolUse` 攔截違規資料夾)
- [ ] 詳細規則文件(Vault-Rules.md / Naming-Conventions.md / Templates)入 PKM-System
- [x] 既有資料夾遷移:`claude/`、`01-People/`、`03-Ideas/`→`03-Resources/`、
      `05-Archive/`→`04-Archives/`(2026-07-04 由 Cowork 完成,見遷移紀錄)
- [x] 各 PARA folder 建立 README.md

---

## 附錄:2026-07-04 遷移紀錄(Cowork 執行)

實際資料夾對應:

| 舊(遷移前) | 新(strict PARA) |
|---|---|
| `02-Projects/` | `01-Projects/` |
| `04-Admin/` | `02-Areas/` |
| `03-Ideas/` | `03-Resources/` |
| `05-Archive/` | `04-Archives/` |
| `claude/` | `04-Archives/Agent Logs/claude/` |
| `graphify-out/` | `04-Archives/Agent Logs/graphify-out/` |
| `01-People/`(空殼) | `04-Archives/_legacy-01-People/` |
| `00-Inbox/` | 不變 |

備註:

- 遷移採**資料夾整體 mv**,保留內部相對結構,故 534 條 wikilink 與 `[[agents/...]]`
  路徑式連結均不受影響(Obsidian 使用預設 shortest-path 解析)。
- OneDrive 對 `.git` 內部檔案有 unlink 權限限制,遷移後的 git commit 需在本機 Windows 端手動完成。
- 舊 `.claude/CLAUDE.md`(向上集團業務 context)仍指向舊路徑 `claude/index.md`,
  該檔未被本次遷移改動,路徑已失效,建議手動更新為
  `04-Archives/Agent Logs/claude/index.md` 或改寫為新結構。
