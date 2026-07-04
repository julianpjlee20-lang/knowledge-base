---
created: 2026-01-13T00:00:00
title: "10 Must-Have MCP Servers for Claude Code (2025)"
tags: [ai-development, ai-tools, claude, claude-code, development, ideas, mcp]
related:
  - "[[2026-01-18-nextjs-supabase-claude-skills-research]]"
  - "[[2025-01-22-Claude-Code-Skills-MCP-Agent-Guide]]"
  - "[[claude-md-best-practices]]"
  - "[[Claude Skills]]"
  - "[[2026-01-22-Claude-Skills-Registry]]"
---

# 10 Must-Have MCP Servers for Claude Code (2025)

## 什麼是 MCP？
MCP (Model Context Protocol) 是 Anthropic 的開放標準，讓 Claude Code 連接外部工具、API、資料庫。如同 AI 的「萬用轉接頭」，實現即時自動化而不用離開終端機。

## 十大推薦 MCP Servers

| # | Server | 用途 |
|---|--------|------|
| 1 | **GitHub** | 管理 PR、Issues、觸發 CI/CD、分析 commits |
| 2 | **Apidog** | API 規格整合、根據 OpenAPI 生成程式碼 |
| 3 | **PostgreSQL** | 直接查詢資料庫 |
| 4 | **Context7** | 即時拉取最新版本的技術文件 |
| 5 | **Sequential Thinking** | 結構化思考、複雜問題拆解 |
| 6 | **Brave Search** | 網頁搜尋、查技術文件 |
| 7 | **Puppeteer** | 瀏覽器自動化、網頁測試 |
| 8 | **File System** | 本地檔案讀寫、目錄管理 |
| 9 | **Docker** | 容器化執行、安全沙盒環境 |
| 10 | **Semgrep** | 程式碼安全掃描（2000+ 漏洞規則）|

---

## 安裝指令

### 1. GitHub MCP
```bash
# Claude Code
claude mcp add --transport http github https://api.githubcopilot.com/mcp/
```

```json
// claude_desktop_config.json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "YOUR_GITHUB_TOKEN"
      }
    }
  }
}
```

### 2. Apidog MCP
```json
{
  "mcpServers": {
    "apidog": {
      "command": "npx",
      "args": ["-y", "@anthropics/apidog-mcp-server"]
    }
  }
}
```

### 3. PostgreSQL MCP
```bash
# Claude Code
claude mcp add --transport stdio db -- npx -y @modelcontextprotocol/server-postgres \
  "postgresql://username:password@hostname:port/database"
```

```json
// claude_desktop_config.json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-postgres",
        "postgresql://username:password@hostname:port/database"
      ]
    }
  }
}
```

### 4. Context7 MCP
```bash
# Claude Code
claude mcp add context7 -- npx -y @upstash/context7-mcp
```

```json
// claude_desktop_config.json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

### 5. Sequential Thinking MCP
```bash
# Claude Code
claude mcp add sequential-thinking -- npx -y @modelcontextprotocol/server-sequential-thinking
```

```json
// claude_desktop_config.json
{
  "mcpServers": {
    "sequentialthinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

### 6. Brave Search MCP
```bash
# 需要先申請 API Key: https://brave.com/search/api
```

```json
// claude_desktop_config.json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "YOUR_BRAVE_API_KEY"
      }
    }
  }
}
```

### 7. Puppeteer MCP
```bash
# Claude Code
claude mcp add puppeteer -- npx -y @modelcontextprotocol/server-puppeteer
```

```json
// claude_desktop_config.json (npx)
{
  "mcpServers": {
    "puppeteer": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-puppeteer"]
    }
  }
}

// claude_desktop_config.json (Docker)
{
  "mcpServers": {
    "puppeteer": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "--init", "-e", "DOCKER_CONTAINER=true", "mcp/puppeteer"]
    }
  }
}
```

### 8. File System MCP
```json
// claude_desktop_config.json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/username/Desktop",
        "/Users/username/Downloads"
      ]
    }
  }
}
```

### 9. Docker MCP
```json
// claude_desktop_config.json
{
  "mcpServers": {
    "docker": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "mcp/docker"]
    }
  }
}
```

### 10. Semgrep MCP
```bash
# 安裝 Semgrep CLI
brew install semgrep
# 或
pip install semgrep
```

```json
// claude_desktop_config.json
{
  "mcpServers": {
    "semgrep": {
      "command": "uvx",
      "args": ["semgrep-mcp"]
    }
  }
}
```

---

## 設定檔位置

| 系統 | 路徑 |
|------|------|
| macOS | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| Windows | `%APPDATA%\Claude\claude_desktop_config.json` |
| Linux | `~/.config/Claude/claude_desktop_config.json` |

---

## 實用建議
- 選 2-3 個符合工作流程的 MCP 即可
- 過多 MCP 會拖慢 Claude Code 啟動速度
- 確保信任安裝的 MCP Server（特別是處理敏感資料時）
- Windows 用戶使用 npx 需加上 `cmd /c` 前綴

## 延伸資源
- [awesome-mcp-servers (GitHub)](https://github.com/wong2/awesome-mcp-servers)
- [MCP 官方文件](https://modelcontextprotocol.io)
- [Claude Code MCP 文件](https://code.claude.com/docs/en/mcp)

---

## 相關筆記

- [[2026-01-18-nextjs-supabase-claude-skills-research]]
- [[2025-01-22-Claude-Code-Skills-MCP-Agent-Guide]]
- [[claude-md-best-practices]]
- [[Claude Skills]]
- [[2026-01-22-Claude-Skills-Registry]]
