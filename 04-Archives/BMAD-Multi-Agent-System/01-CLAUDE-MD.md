---
created: 2025-01-24
title: "CLAUDE.md - 多 Agent 協調規則"
tags: [ai-development, bmad, claude, claude-code, config, project]
related:
  - "[[2026-01-18-nextjs-supabase-claude-skills-research]]"
  - "[[2025-01-22-Claude-Code-Skills-MCP-Agent-Guide]]"
  - "[[claude-md-best-practices]]"
  - "[[Claude Skills]]"
  - "[[2026-01-22-Claude-Skills-Registry]]"
---

# CLAUDE.md - 多 Agent 協調規則

本專案使用 BMAD Method 的多 Agent 協調系統，所有 Agent 必須遵守以下規則。

## 🎯 核心概念

每個 Agent 代表不同的敏捷角色，透過共享的 `tasks.json` 協調工作進度。

## 👥 Agent 角色定義

| Agent | 角色 | Phase | 職責 |
|-------|------|-------|------|
| analyst | Business Analyst | Phase 1 | 產品探索、需求分析、建立 Product Brief |
| pm | Product Manager | Phase 2 | 建立 PRD、定義需求、優先級排序 |
| architect | System Architect | Phase 3 | 系統設計、技術選型、API 規格 |
| sm | Scrum Master | Phase 4 | Sprint 規劃、Story 拆分、進度追蹤 |
| dev | Developer | Phase 4 | 實作功能、撰寫測試、程式碼品質 |
| qa | QA Engineer | Phase 4 | 程式碼審查、測試驗證、品質把關 |

## 📋 Task 狀態定義

- `pending` - 等待執行，dependencies 已滿足
- `blocked` - 被其他任務阻擋，dependencies 未完成
- `in-progress` - 正在執行中
- `done` - 已完成
- `failed` - 執行失敗，需要介入

## 🚀 Agent 啟動流程

每次 Agent 啟動或收到新指令時，必須執行以下步驟：

### Step 1: 讀取任務狀態
```
讀取 .claude/tasks/tasks.json
```

### Step 2: 判斷可執行任務
檢查符合以下條件的任務：
1. `assignedAgent` 等於當前 Agent
2. `status` 為 `pending` 或 `blocked`
3. 所有 `dependencies` 中的任務 `status` 都是 `done`

### Step 3: 更新狀態開始執行
```json
{
  "status": "in-progress",
  "startedAt": "ISO-8601 timestamp",
  "owner": "agent-terminal-id"
}
```

### Step 4: 執行任務
根據 Agent 角色執行對應工作

### Step 5: 完成任務更新狀態
```json
{
  "status": "done",
  "completedAt": "ISO-8601 timestamp",
  "output": "實際輸出路徑"
}
```

## ⏳ 等待模式

當沒有可執行任務時，Agent 應進入等待模式：

```
🔄 [Agent Name] 等待中...

📋 我負責的任務：
- TASK-XXX: [任務名稱]
  狀態: blocked
  等待: TASK-YYY (in-progress by dev)

⏰ 下次檢查：2 分鐘後
```

每 2 分鐘重新讀取 tasks.json 檢查狀態變化。

## 🔒 衝突避免規則

1. **單一所有權**：任務一旦有 owner 且 status 為 in-progress，其他 Agent 不得接手
2. **原子更新**：更新 tasks.json 時確保完整性
3. **先讀後寫**：每次寫入前先讀取最新狀態

## 📄 文件輸出位置

| 文件類型 | 路徑 |
|----------|------|
| Product Brief | docs/product-brief.md |
| PRD | docs/prd.md |
| UX Design | docs/ux-design.md |
| Architecture | docs/architecture.md |
| Sprint Status | docs/sprint-status.yaml |
| Stories | docs/stories/STORY-XXX.md |
| Source Code | src/ |

## 📊 範例工作流程

```
Terminal 1 (Analyst):
[讀取 tasks.json] → [TASK-001 可執行] → [建立 product-brief.md] → [更新 status: done]
                                                                          ↓
Terminal 2 (PM):                                                     [解除阻擋]
[讀取 tasks.json] → [等待 TASK-001...] ────────────────────────→ [TASK-002 可執行] → [建立 prd.md]
                                                                          ↓
Terminal 3 (Architect):                                              [解除阻擋]
[讀取 tasks.json] → [等待 TASK-002, TASK-003...] ──────────────→ [TASK-004 可執行] → [建立 architecture.md]
                                                                          ↓
Terminal 4 (Dev):                                                    [解除阻擋]
[讀取 tasks.json] → [等待 TASK-005...] ───────────────────────→ [TASK-006 可執行] → [實作程式碼]
                                                                          ↓
Terminal 5 (QA):                                                     [解除阻擋]
[讀取 tasks.json] → [等待 TASK-006...] ───────────────────────→ [TASK-007 可執行] → [程式碼審查]
```

## ⚠️ 注意事項

1. **永遠先讀取 tasks.json**：每次執行前確認最新狀態
2. **立即更新狀態**：開始和完成任務時立即寫入
3. **保持冪等性**：相同任務重複執行應產生相同結果
4. **紀錄輸出**：任務產出必須寫入指定路徑

---

## 相關筆記

- [[2026-01-18-nextjs-supabase-claude-skills-research]]
- [[2025-01-22-Claude-Code-Skills-MCP-Agent-Guide]]
- [[claude-md-best-practices]]
- [[Claude Skills]]
- [[2026-01-22-Claude-Skills-Registry]]
