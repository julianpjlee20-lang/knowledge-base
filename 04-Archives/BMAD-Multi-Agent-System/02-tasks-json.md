---
created: 2025-01-24
title: "tasks.json - 任務定義結構"
tags: [ai-development, bmad, claude, claude-code, config, json, project]
related:
  - "[[2026-01-18-nextjs-supabase-claude-skills-research]]"
  - "[[2025-01-22-Claude-Code-Skills-MCP-Agent-Guide]]"
  - "[[claude-md-best-practices]]"
  - "[[Claude Skills]]"
  - "[[2026-01-22-Claude-Skills-Registry]]"
---

# tasks.json - 任務定義結構

這是多 Agent 協調的核心檔案，定義所有任務及其依賴關係。

## 完整範例

```json
{
  "projectName": "BMAD Multi-Agent Demo",
  "version": "1.0.0",
  "lastUpdated": "2025-01-24T10:00:00Z",
  "teamVelocity": 25,
  "currentSprint": 1,
  "agents": {
    "analyst": { "status": "idle", "currentTask": null },
    "pm": { "status": "idle", "currentTask": null },
    "architect": { "status": "idle", "currentTask": null },
    "sm": { "status": "idle", "currentTask": null },
    "dev": { "status": "idle", "currentTask": null },
    "qa": { "status": "idle", "currentTask": null }
  },
  "phases": [
    {
      "id": "phase-1",
      "name": "Analysis",
      "status": "pending",
      "owner": "analyst",
      "tasks": ["TASK-001"]
    },
    {
      "id": "phase-2", 
      "name": "Planning",
      "status": "blocked",
      "owner": "pm",
      "dependencies": ["phase-1"],
      "tasks": ["TASK-002", "TASK-003"]
    },
    {
      "id": "phase-3",
      "name": "Architecture",
      "status": "blocked",
      "owner": "architect",
      "dependencies": ["phase-2"],
      "tasks": ["TASK-004"]
    },
    {
      "id": "phase-4",
      "name": "Implementation",
      "status": "blocked",
      "owner": "sm",
      "dependencies": ["phase-3"],
      "tasks": ["TASK-005", "TASK-006", "TASK-007"]
    }
  ],
  "tasks": [
    {
      "id": "TASK-001",
      "title": "建立產品簡報 (Product Brief)",
      "description": "分析專案需求，產出 product-brief.md",
      "phase": "phase-1",
      "assignedAgent": "analyst",
      "status": "pending",
      "priority": "high",
      "dependencies": [],
      "blocks": ["TASK-002"],
      "output": "docs/product-brief.md",
      "acceptanceCriteria": [
        "包含 Executive Summary",
        "明確 Problem Statement",
        "定義 Target Audience",
        "設定 Success Metrics"
      ]
    },
    {
      "id": "TASK-002",
      "title": "建立產品需求文件 (PRD)",
      "description": "根據 product brief 產出詳細 PRD",
      "phase": "phase-2",
      "assignedAgent": "pm",
      "status": "blocked",
      "priority": "high",
      "dependencies": ["TASK-001"],
      "blocks": ["TASK-003", "TASK-004"],
      "input": "docs/product-brief.md",
      "output": "docs/prd.md",
      "acceptanceCriteria": [
        "定義 Functional Requirements",
        "定義 Non-Functional Requirements",
        "拆分 Epics 和 Stories",
        "完成優先級排序 (MoSCoW)"
      ]
    },
    {
      "id": "TASK-003",
      "title": "建立 UX 設計文件",
      "description": "設計使用者介面和流程",
      "phase": "phase-2",
      "assignedAgent": "pm",
      "status": "blocked",
      "priority": "medium",
      "dependencies": ["TASK-001"],
      "blocks": ["TASK-004"],
      "input": "docs/product-brief.md",
      "output": "docs/ux-design.md",
      "acceptanceCriteria": [
        "完成 User Flow",
        "建立 Wireframes",
        "定義 Design System",
        "確保 WCAG 2.1 AA 合規"
      ]
    },
    {
      "id": "TASK-004",
      "title": "建立系統架構文件",
      "description": "設計技術架構和資料模型",
      "phase": "phase-3",
      "assignedAgent": "architect",
      "status": "blocked",
      "priority": "high",
      "dependencies": ["TASK-002", "TASK-003"],
      "blocks": ["TASK-005"],
      "input": ["docs/prd.md", "docs/ux-design.md"],
      "output": "docs/architecture.md",
      "acceptanceCriteria": [
        "完成系統架構圖",
        "定義資料模型 (Data Models)",
        "設計 API 規格",
        "選定技術棧並說明理由",
        "對應 NFR 需求"
      ]
    },
    {
      "id": "TASK-005",
      "title": "Sprint 規劃",
      "description": "將 PRD 拆解為 Sprint stories",
      "phase": "phase-4",
      "assignedAgent": "sm",
      "status": "blocked",
      "priority": "high",
      "dependencies": ["TASK-004"],
      "blocks": ["TASK-006"],
      "input": ["docs/prd.md", "docs/architecture.md"],
      "output": "docs/sprint-status.yaml",
      "acceptanceCriteria": [
        "所有 Stories 已估點",
        "Sprint 1 已規劃",
        "Story 檔案已建立在 docs/stories/"
      ]
    },
    {
      "id": "TASK-006",
      "title": "實作 Story STORY-001",
      "description": "實作第一個 User Story",
      "phase": "phase-4",
      "assignedAgent": "dev",
      "status": "blocked",
      "priority": "high",
      "dependencies": ["TASK-005"],
      "blocks": ["TASK-007"],
      "input": "docs/stories/STORY-001.md",
      "output": "src/",
      "acceptanceCriteria": [
        "程式碼完成且通過 lint",
        "單元測試覆蓋率 >80%",
        "符合架構設計"
      ]
    },
    {
      "id": "TASK-007",
      "title": "程式碼審查",
      "description": "審查所有完成的程式碼",
      "phase": "phase-4",
      "assignedAgent": "qa",
      "status": "blocked",
      "priority": "high",
      "dependencies": ["TASK-006"],
      "blocks": [],
      "input": "src/",
      "acceptanceCriteria": [
        "程式碼品質符合標準",
        "無安全性漏洞",
        "測試充分",
        "文件完整"
      ]
    }
  ]
}
```

## 欄位說明

### Task 物件

| 欄位 | 類型 | 說明 |
|------|------|------|
| id | string | 唯一識別碼 |
| title | string | 任務標題 |
| assignedAgent | string | 負責的 Agent |
| status | string | pending/blocked/in-progress/done/failed |
| dependencies | array | 依賴的任務 ID 列表 |
| blocks | array | 完成後會解除阻擋的任務 |
| input | string/array | 輸入檔案 |
| output | string | 輸出檔案 |
| acceptanceCriteria | array | 驗收條件 |

---

## 相關筆記

- [[2026-01-18-nextjs-supabase-claude-skills-research]]
- [[2025-01-22-Claude-Code-Skills-MCP-Agent-Guide]]
- [[claude-md-best-practices]]
- [[Claude Skills]]
- [[2026-01-22-Claude-Skills-Registry]]
