---
created: 2025-01-22T20:30:00
title: "Claude Code Skills, MCP & Agent 完整技術摘要"
tags: [agent, ai, ai-development, claude, claude-code, development, mcp, reference, skills]
related:
  - "[[2026-01-18-nextjs-supabase-claude-skills-research]]"
  - "[[claude-md-best-practices]]"
  - "[[Claude Skills]]"
  - "[[2026-01-22-Claude-Skills-Registry]]"
  - "[[01-CLAUDE-MD]]"
---

# Claude Code Skills, MCP & Agent 完整技術摘要

> 最後更新：2025年1月

## 目錄

1. [概覽與核心概念](#概覽與核心概念)
2. [Skills（技能）](#skills技能)
3. [MCP（Model Context Protocol）](#mcpmodel-context-protocol)
4. [Agent SDK 與 Subagents](#agent-sdk-與-subagents)
5. [Hooks（鉤子）](#hooks鉤子)
6. [整合應用範例](#整合應用範例)
7. [最佳實踐](#最佳實踐)

---

## 概覽與核心概念  

### 各元件角色定位

| 元件 | 功能 | 類比 |
|------|------|------|
| **Skills** | 可攜帶、可重用的專業知識包 | 新員工入職指南 |
| **MCP** | 連接外部工具與資料來源的通用協定 | USB-C 連接器 |
| **Subagents** | 獨立執行特定任務的子代理 | 專案團隊成員 |
| **Hooks** | 在特定時機自動觸發的腳本 | Git hooks |
| **Agent SDK** | 建構自主代理的開發框架 | 代理程式骨架 |

### 使用時機決策

```
需要教導 Claude 專業知識？ → Skills
需要連接外部系統？ → MCP
需要平行處理或隔離上下文？ → Subagents
需要自動化觸發動作？ → Hooks
需要建構自主代理應用？ → Agent SDK
```

---

## Skills（技能）

### 什麼是 Skills

Skills 是模組化的資料夾，包含指令、腳本和資源，讓 Claude 能動態載入以執行特定任務。相當於將你的專業知識打包成 Claude 可以理解和使用的格式。

### 核心特點

- **漸進式揭露**：Claude 只在需要時載入相關內容
- **跨平台可攜**：可在 Claude.ai、Claude Code、API 間共用
- **可包含執行程式**：支援 Python、Bash 腳本

### 資料夾結構

```
my-skill/
├── SKILL.md              # 必需：核心指令與元資料
├── scripts/              # 選用：可執行腳本 (Python/Bash)
├── references/           # 選用：參考文件
└── assets/               # 選用：範本、圖示等資源
```

### SKILL.md 格式

```markdown
---
name: my-skill-name
description: 清楚描述這個 Skill 做什麼以及何時使用。這是觸發機制，最多 1024 字元。
---

# 技能標題

[Claude 啟用此技能時會遵循的指令]

## 使用方式

詳細步驟說明...

## 範例

- 範例用法 1
- 範例用法 2
```

### 進階 Frontmatter 選項

```yaml
---
name: deploy
description: 部署應用程式到生產環境
context: fork                    # 在獨立上下文中執行
disable-model-invocation: true   # 只有使用者能觸發（Claude 不會自動觸發）
user-invocable: false            # 只有 Claude 能觸發（使用者不能手動觸發）
allowed-tools: Bash, Read, Write # 限制可用工具
---
```

### 設定 Skills

**方法 1：Claude.ai 網頁介面**
1. 前往 Settings > Features > Enable Skills
2. 上傳 .zip 檔案（包含 SKILL.md）

**方法 2：Claude Code CLI**
```bash
# 使用者層級（所有專案可用）
~/.claude/skills/my-skill/SKILL.md

# 專案層級（僅當前專案）
.claude/skills/my-skill/SKILL.md
```

**方法 3：透過 Plugin 安裝**
```bash
# 從 marketplace 安裝
/plugins install document-skills

# 使用
"Use the PDF skill to extract form fields from file.pdf"
```

### 實際範例：程式碼解說技能

```markdown
---
name: explain-code
description: 用視覺圖表和類比解釋程式碼。當解釋程式碼運作、教學或使用者問「這是怎麼運作的？」時使用。
---

解釋程式碼時，請遵循：

1. **先用類比**：將程式碼比喻為日常生活事物
2. **畫圖表**：用 ASCII art 展示流程、結構或關係
3. **逐步講解**：說明每個步驟發生什麼
4. **提醒陷阱**：常見錯誤或誤解是什麼？
```

### Skills vs 其他概念

| 需求 | 使用 |
|------|------|
| 連接外部資料 | MCP（連接），然後用 Skill 教如何使用 |
| 平行執行任務 | Subagents |
| 自動觸發動作 | Hooks |
| 專業知識/流程 | Skills |

---

## MCP（Model Context Protocol）

### 什麼是 MCP

MCP 是開放標準協定，讓 Claude 能連接外部工具和資料來源。就像 USB-C 讓各種裝置用同一種接口連接一樣，MCP 讓 Claude 用統一方式連接 GitHub、資料庫、API 等服務。

### 核心概念

- **MCP Server**：提供特定功能的服務（如 GitHub、Notion）
- **Tools**：Server 提供的具體操作（如 create_issue、search_docs）
- **Resources**：可用 @ 提及的資料來源

### 設定方式

#### 方法 1：CLI 指令

```bash
# 基本新增
claude mcp add <n> -- <command> [args...]

# 指定 scope
claude mcp add github --scope user -- npx -y @modelcontextprotocol/server-github

# 使用 HTTP 傳輸
claude mcp add --transport http stripe https://mcp.stripe.com

# 帶環境變數
claude mcp add github --env GITHUB_TOKEN=xxx -- npx -y @modelcontextprotocol/server-github

# JSON 格式（複雜設定）
claude mcp add-json github '{"type":"stdio","command":"npx","args":["-y","@modelcontextprotocol/server-github"],"env":{"GITHUB_PERSONAL_ACCESS_TOKEN":"ghp_xxx"}}'
```

#### 方法 2：直接編輯設定檔

**User 層級** (`~/.claude.json`)：
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_xxx"
      }
    }
  }
}
```

**Project 層級** (`.mcp.json`)：
```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "${BRAVE_API_KEY}"
      }
    }
  }
}
```

### Scope 層級

| Scope | 儲存位置 | 用途 |
|-------|----------|------|
| `local` | `~/.claude.json` (專案路徑下) | 個人實驗、敏感憑證 |
| `project` | `.mcp.json` | 團隊共享（可加入 git） |
| `user` | `~/.claude.json` | 跨專案個人工具 |

### 常用指令

```bash
# 列出所有 MCP servers
claude mcp list

# 查看特定 server 詳情
claude mcp get github

# 移除 server
claude mcp remove github

# 在 Claude Code 內檢查狀態
/mcp
```

### 常見 MCP Servers

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"]
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/dir"]
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    },
    "sqlite": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sqlite", "path/to/db.sqlite"]
    }
  }
}
```

### MCP 與 Skills 的協作

```
MCP = 連接能力（Access）
Skills = 使用方法（Know-how）

例如：
- MCP 讓 Claude 能查詢 Notion
- Skill 教 Claude 如何準備會議摘要、該拉哪些頁面、格式標準是什麼
```

---

## Agent SDK 與 Subagents

### Agent SDK 概覽

Claude Agent SDK（原 Claude Code SDK）提供與 Claude Code 相同的工具、代理迴圈和上下文管理能力，可用 Python 或 TypeScript 程式化控制。

### 核心特點

- **終端機存取**：讓 Claude 能讀寫檔案、執行指令
- **代理迴圈**：收集上下文 → 採取行動 → 驗證結果 → 重複
- **上下文管理**：包含壓縮（compaction）功能處理長對話

### 基本使用（Python）

```python
from claude_agent_sdk import ClaudeAgent, ClaudeAgentOptions

# 基本設定
options = ClaudeAgentOptions(
    system_prompt="You are a Python code reviewer focused on security",
    cwd="/path/to/project",
    allowed_tools=["Read", "Write", "Bash", "Grep"]
)

# 建立代理
agent = ClaudeAgent(options)

# 執行任務
result = await agent.run("Review the authentication module for security issues")
```

### Subagents（子代理）

Subagents 是可以獨立執行特定任務的子代理，有獨立的上下文視窗。

#### 內建 Subagents

| 名稱 | 用途 | 工具限制 |
|------|------|----------|
| `Explore` | 搜尋、分析程式庫 | 唯讀（Read, Grep, Glob） |
| `Plan` | 規劃階段的研究 | 唯讀 |
| `General-purpose` | 複雜多步驟任務 | 完整工具存取 |

#### 建立自訂 Subagent

**檔案位置**：
- User 層級：`~/.claude/agents/my-agent.md`
- Project 層級：`.claude/agents/my-agent.md`

**格式**：
```markdown
---
name: code-reviewer
description: 程式碼審查代理，專注於品質和安全性
tools: Read, Grep, Glob
disallowedTools: Write, Edit
permissionMode: default
---

你是專業的程式碼審查員。審查時請：

1. 檢查安全漏洞
2. 評估程式碼品質
3. 提供改善建議

報告格式：
- 🔴 嚴重問題
- 🟡 建議改善
- 🟢 良好實踐
```

#### Subagent 進階選項

```yaml
---
name: safe-researcher
description: 受限的研究代理
tools: Read, Grep, Glob, Bash           # 白名單
disallowedTools: Write, Edit            # 黑名單
permissionMode: bypassPermissions       # 跳過權限檢查（謹慎使用）
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate-command.sh"
---
```

#### 使用 Subagent

```bash
# 透過 /agents 指令建立
/agents

# 在對話中 Claude 會自動委派任務
"I'll delegate this security review to the code-reviewer agent..."

# 恢復先前的 subagent
"Continue the previous security review work"
```

### 長時間運行代理的最佳實踐

1. **初始化代理**：第一個 session 設置環境
2. **進度追蹤**：使用 `claude-progress.txt` 記錄狀態
3. **增量進展**：每個 session 做漸進式改善
4. **Git 整合**：用 commit 追蹤變更

---

## Hooks（鉤子）

### 什麼是 Hooks

Hooks 是在 Claude Code 特定生命週期事件時自動執行的 shell 指令，類似 Git hooks。

### Hook 事件類型

| 事件 | 觸發時機 | 用途 |
|------|----------|------|
| `UserPromptSubmit` | 使用者提交 prompt 後 | 驗證、日誌、上下文注入 |
| `PreToolUse` | 工具執行前 | 阻擋危險指令、修改參數 |
| `PostToolUse` | 工具成功執行後 | 格式化、測試、日誌 |
| `PermissionRequest` | 權限對話框出現時 | 自動批准/拒絕 |
| `Stop` | Claude 完成回應時 | 通知、自動 commit |
| `SubagentStop` | Subagent 完成時 | 日誌、清理 |
| `SessionStart` | Session 開始時 | 載入上下文、環境設定 |
| `Notification` | Claude 發送通知時 | 自訂通知 |

### 設定位置

```bash
# User 層級
~/.claude/settings.json

# Project 層級
.claude/settings.json

# Local 層級（不加入 git）
.claude/settings.local.json
```

### 基本設定格式

```json
{
  "hooks": {
    "EventName": [
      {
        "matcher": "ToolPattern",
        "hooks": [
          {
            "type": "command",
            "command": "your-command-here"
          }
        ]
      }
    ]
  }
}
```

### Matcher 語法

```json
// 精確匹配
"matcher": "Write"

// 多工具匹配
"matcher": "Write|Edit|MultiEdit"

// 匹配所有
"matcher": "*"

// 正規表示式
"matcher": "Bash.*"
```

### 實用範例

#### 1. 自動格式化（PostToolUse）

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "prettier --write $CLAUDE_FILE_PATHS"
          }
        ]
      }
    ]
  }
}
```

#### 2. 阻擋危險指令（PreToolUse）

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "if echo \"$CLAUDE_COMMAND\" | grep -E '(rm -rf|sudo)'; then echo 'Blocked' && exit 1; fi"
          }
        ]
      }
    ]
  }
}
```

#### 3. 自動執行測試（PostToolUse）

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "npm test -- --findRelatedTests $CLAUDE_FILE_PATHS"
          }
        ]
      }
    ]
  }
}
```

#### 4. 自動權限批准（PermissionRequest）

```json
{
  "hooks": {
    "PermissionRequest": [
      {
        "matcher": "Read|Grep|Glob",
        "hooks": [
          {
            "type": "command",
            "command": "echo '{\"decision\": \"allow\"}'"
          }
        ]
      }
    ]
  }
}
```

#### 5. 完成通知（Stop）

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "osascript -e 'display notification \"Claude 完成了！\" with title \"Claude Code\"'"
          }
        ]
      }
    ]
  }
}
```

### Hook 回傳值控制

```json
// 允許繼續
{ "decision": "allow" }

// 阻擋並顯示錯誤
{ "decision": "block", "reason": "不允許的操作" }

// 修改工具輸入（PreToolUse v2.0.10+）
{ "toolInput": { "modified": "parameters" } }
```

### 環境變數

| 變數 | 說明 |
|------|------|
| `$CLAUDE_FILE_PATHS` | 操作的檔案路徑 |
| `$CLAUDE_TOOL_NAME` | 使用的工具名稱 |
| `$CLAUDE_PROJECT_DIR` | 專案根目錄絕對路徑 |
| `$CLAUDE_WORKING_DIR` | 當前工作目錄 |
| `$CLAUDE_SESSION_ID` | 當前 session ID |

### Prompt-based Hooks

除了 command hooks，還可以用 LLM 評估：

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "prompt",
            "prompt": "評估這個指令是否安全：{{command}}"
          }
        ]
      }
    ]
  }
}
```

---

## 整合應用範例

### 範例 1：文件處理工作流

```
Skills: PDF 處理技能（格式化、摘要標準）
  ↓
MCP: Google Drive 連接（存取檔案）
  ↓
Hooks: PostToolUse 自動備份到指定資料夾
```

### 範例 2：程式碼審查 Pipeline

```yaml
# .claude/agents/code-reviewer.md
---
name: code-reviewer
description: 安全與品質審查
tools: Read, Grep, Glob
---

審查重點：
1. 安全漏洞
2. 效能問題
3. 最佳實踐

# .claude/settings.json hooks
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "eslint $CLAUDE_FILE_PATHS && npm test"
      }]
    }]
  }
}
```

### 範例 3：研究代理

```python
from claude_agent_sdk import ClaudeAgent

# 主代理
main_agent = ClaudeAgent(
    system_prompt="研究協調者",
    subagents=[
        {"name": "web-researcher", "tools": ["WebSearch", "WebFetch"]},
        {"name": "data-analyst", "tools": ["Read", "Bash"]},
        {"name": "report-writer", "tools": ["Write"]}
    ]
)

# 執行
result = await main_agent.run("""
研究「2025 AI 趨勢」：
1. 搜尋最新資料
2. 分析關鍵趨勢
3. 撰寫摘要報告
""")
```

---

## 最佳實踐

### Skills 最佳實踐

1. **SKILL.md 保持精簡**：500 行以內，詳細內容放 references/
2. **描述要完整**：description 是觸發關鍵，要涵蓋「做什麼」和「何時用」
3. **漸進式揭露**：主要指令 → 參考文件 → 腳本
4. **測試導向**：用不同 Claude instance 測試效果

### MCP 最佳實踐

1. **安全第一**：敏感憑證用環境變數
2. **適當 Scope**：團隊共用用 project，個人用 user
3. **監控用量**：用 `/context` 檢查上下文消耗
4. **按需啟用**：用 @ 提及切換，減少不必要的上下文

### Agent 最佳實踐

1. **最小權限**：每個 subagent 只給必要的工具
2. **隔離上下文**：複雜任務用 subagent 避免污染主對話
3. **進度追蹤**：長任務用檔案記錄狀態
4. **錯誤處理**：設定 hooks 攔截危險操作

### Hooks 最佳實踐

1. **從簡單開始**：先做 PostToolUse formatter
2. **精確 Matcher**：避免 `*` 匹配太多
3. **處理超時**：預設 60 秒，複雜任務要調整
4. **日誌調試**：加 `--debug` 排查問題

---

## 快速參考卡

### 常用指令

```bash
# MCP
claude mcp add <n> -- <command>
claude mcp list
claude mcp remove <n>
/mcp

# Agents
/agents

# Skills
/skill-name

# 除錯
claude config list
CLAUDE_DEBUG=1 claude
```

### 設定檔位置

| 類型 | User 層級 | Project 層級 |
|------|-----------|--------------|
| MCP | `~/.claude.json` | `.mcp.json` |
| Hooks | `~/.claude/settings.json` | `.claude/settings.json` |
| Skills | `~/.claude/skills/` | `.claude/skills/` |
| Agents | `~/.claude/agents/` | `.claude/agents/` |

### 相關資源

- [Claude Code 官方文件](https://code.claude.com/docs)
- [Agent Skills 規範](https://agentskills.io)
- [MCP 協定](https://modelcontextprotocol.io)
- [Anthropic Skills Repository](https://github.com/anthropics/skills)

---

*本文件整理自 Anthropic 官方文件與社群資源，如有更新請以官方為準。*

---

## 相關筆記

- [[2026-01-18-nextjs-supabase-claude-skills-research]]
- [[claude-md-best-practices]]
- [[Claude Skills]]
- [[2026-01-22-Claude-Skills-Registry]]
- [[01-CLAUDE-MD]]
