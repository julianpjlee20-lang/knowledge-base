---
created: 2025-01-24
title: "BMAD Multi-Agent Task System"
tags: [ai-development, automation, bmad, claude, claude-code, multi-agent, project]
related:
  - "[[2026-01-18-nextjs-supabase-claude-skills-research]]"
  - "[[2025-01-22-Claude-Code-Skills-MCP-Agent-Guide]]"
  - "[[claude-md-best-practices]]"
  - "[[Claude Skills]]"
  - "[[2026-01-22-Claude-Skills-Registry]]"
---

# BMAD Multi-Agent Task System

基於 BMAD Method 的多 Agent 任務協調系統，讓多個 Claude Code 終端機同時工作，自動根據任務依賴判斷執行順序。

## 🎯 核心概念

```
┌─────────────────────────────────────────────────────────────────────┐
│                    BMAD Multi-Agent Workflow                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  Terminal 1        Terminal 2        Terminal 3        Terminal 4    │
│  (Analyst)         (PM)              (Architect)       (Dev)         │
│      │                │                   │               │          │
│      ▼                │                   │               │          │
│  [執行中]           [等待]             [等待]          [等待]        │
│  TASK-001            │                   │               │          │
│      │                │                   │               │          │
│      ▼                ▼                   │               │          │
│   [完成] ─────→ [解除阻擋]              │               │          │
│                  TASK-002               │               │          │
│                      │                   │               │          │
│                      ▼                   ▼               │          │
│                   [完成] ─────────→ [解除阻擋]          │          │
│                                     TASK-004            │          │
│                                         │               │          │
│                                         ▼               ▼          │
│                                      [完成] ─────→ [解除阻擋]      │
│                                                     TASK-006       │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

## 📁 專案結構

```
project/
├── CLAUDE.md                      # 全域協調規則
├── .claude/
│   ├── agents/
│   │   ├── analyst.md             # Business Analyst
│   │   ├── pm.md                  # Product Manager
│   │   ├── architect.md           # System Architect
│   │   ├── sm.md                  # Scrum Master
│   │   ├── dev.md                 # Developer
│   │   └── qa.md                  # QA / Code Reviewer
│   ├── tasks/
│   │   └── tasks.json             # 共享任務狀態
│   └── commands/
│       └── check-tasks.md         # 檢查任務狀態指令
└── docs/
    ├── product-brief.md           # Phase 1 輸出
    ├── prd.md                     # Phase 2 輸出
    ├── ux-design.md               # Phase 2 輸出
    ├── architecture.md            # Phase 3 輸出
    ├── sprint-status.yaml         # Phase 4 輸出
    └── stories/                   # User Stories
        └── STORY-XXX.md
```

## 🚀 快速開始

### 1. 開啟多個終端機

建議開啟 4-6 個終端機，每個代表不同的 Agent：

```bash
# 所有終端機都 cd 到專案目錄
cd your-project
```

### 2. 在每個終端機啟動 Claude Code

```bash
claude
```

### 3. 指定 Agent 角色

**Terminal 1 - Analyst:**
```
你是 analyst agent，請讀取 .claude/tasks/tasks.json 並開始你的工作
```

**Terminal 2 - PM:**
```
你是 pm agent，請讀取 .claude/tasks/tasks.json 並開始你的工作
```

**Terminal 3 - Architect:**
```
你是 architect agent，請讀取 .claude/tasks/tasks.json 並開始你的工作
```

**Terminal 4 - Dev:**
```
你是 dev agent，請讀取 .claude/tasks/tasks.json 並開始你的工作
```

**Terminal 5 - QA (等到開發完成才會開始):**
```
你是 qa agent，請讀取 .claude/tasks/tasks.json 並開始你的工作
```

## 📋 Agent 角色說明

| Agent | Phase | 職責 | 等待誰 |
|-------|-------|------|--------|
| **analyst** | Phase 1 | 建立 Product Brief | 無（第一個執行） |
| **pm** | Phase 2 | 建立 PRD、UX Design | analyst |
| **architect** | Phase 3 | 系統架構設計 | pm |
| **sm** | Phase 4 | Sprint 規劃、Story 拆分 | architect |
| **dev** | Phase 4 | 實作程式碼 | sm |
| **qa** | Phase 4 | 程式碼審查 | **所有 dev 任務** |

## 🔗 相關檔案

- [[01-CLAUDE-MD|CLAUDE.md - 協調規則]]
- [[02-tasks-json|tasks.json - 任務定義]]
- [[agents/analyst|Analyst Agent]]
- [[agents/pm|PM Agent]]
- [[agents/architect|Architect Agent]]
- [[agents/sm|Scrum Master Agent]]
- [[agents/dev|Developer Agent]]
- [[agents/qa|QA Agent]]

---

## 相關筆記

- [[2026-01-18-nextjs-supabase-claude-skills-research]]
- [[2025-01-22-Claude-Code-Skills-MCP-Agent-Guide]]
- [[claude-md-best-practices]]
- [[Claude Skills]]
- [[2026-01-22-Claude-Skills-Registry]]
