---
created: 2026-01-12T00:00:00
title: "Claude Code 創作者的工作流程完整解析"
tags: [ai-development, claude, claude-code, ideas, mcp, personal-development, programming, workflow]
related:
  - "[[2026-01-18-nextjs-supabase-claude-skills-research]]"
  - "[[2025-01-22-Claude-Code-Skills-MCP-Agent-Guide]]"
  - "[[claude-md-best-practices]]"
  - "[[Claude Skills]]"
  - "[[多元興趣與創作者經濟]]"
---

# Claude Code 創作者的工作流程完整解析

## 影片摘要

這部影片揭露了 Claude Code 創作者 Boris 的完整開發工作流程。儘管他稱之為「基本設置」，實際上他同時運行五個 Claude 實例，使用可直接發送到 Slack 的 MCP 伺服器，自訂 AI 子代理來審查程式碼，以及一個叫做 Ralph Wiggum 的插件，能讓 Claude 自動運行數小時。

## 核心工作流程

### 1. 計畫模式（Plan Mode）
這是最重要的習慣。按 Shift+Tab 兩次進入計畫模式，在此模式下 Claude 只能讀取程式碼，不能寫入。透過來回對話直到雙方都確認沒有需要澄清的事項，才開始實作。Boris 表示：「有了好的計畫，切換到自動接受模式後，Claude 通常能一次完成整個實作。」

### 2. Claude.md 檔案
這是存放在專案根目錄的記憶檔案，記錄專案的規則、模式和偏好設定，包括架構、關鍵檔案、開發指南、設計系統等。Boris 的特殊做法是在團隊成員的 PR 中標記 Claude，請它將學習心得加入 claude.md，讓專案記憶持續進化。

### 3. 自訂斜線指令
Boris 為每個重複性任務建立自訂指令，最常用的是 commit-push-PR。在 `.claude/commands/` 資料夾建立 markdown 檔案，可以使用反引號嵌入終端指令，節省代幣並加速執行。

### 4. 權限管理
使用 `/permissions` 預先允許安全的操作，保持工作流程順暢。切記不要使用 `dangerously skip permissions`，而是逐一評估並添加安全的權限規則。

### 5. 自訂 AI 子代理
在 `.claude/agents/` 建立專門的代理，如程式碼簡化器、應用程式驗證器等。這些代理在 Claude 完成任務後執行特定的審查或優化工作。

### 6. Hooks 自動化
使用 post-tool-use hook 在 Claude 編輯程式碼後自動執行 lint 等格式化工具，避免 CI 失敗。

### 7. MCP 伺服器整合
連接 Slack、Jira、BigQuery、Sentry 等外部工具，將 Claude Code 從單純的編碼助手轉變為整個開發生態系統的介面。

### 8. Stop Hooks 驗證循環
當 Claude 表示完成任務時，啟動驗證代理檢查工作是否真正完成，創建無需人工監督的回饋循環。

### 9. Ralph Wiggum 插件
這個以辛普森家庭角色命名的插件讓 Claude 持續循環工作直到真正成功。有報導稱有人用它運行 3 個月自動建構了一個程式語言，另一位工程師用 $297 API 成本完成了價值 $50,000 的合約。但影片作者實測後認為目前還不夠成熟，花了 $10 但結果不完美。

## 最重要的心得

Boris 強調獲得優質結果的關鍵是：**給 Claude 一個驗證工作的方法**。無論是執行測試套件、bash 指令、或在瀏覽器中測試 UI，這個回饋循環能讓最終結果品質提升 2-3 倍。


## 來源

- YouTube: https://www.youtube.com/watch?v=JUTx6MxOjhE

---

## 相關筆記

- [[2026-01-18-nextjs-supabase-claude-skills-research]]
- [[2025-01-22-Claude-Code-Skills-MCP-Agent-Guide]]
- [[claude-md-best-practices]]
- [[Claude Skills]]
- [[多元興趣與創作者經濟]]
