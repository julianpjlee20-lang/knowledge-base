---
created: 2026-04-06
category: Ideas
tags: [ideas, AI, ClaudeCode, 自動化, 會計, 案例]
---

# Claude Code 案例：零員工稅理士管理 60 家顧問客戶

一位日本公認會計師使用 Claude Code、MCP、排程任務與 API 整合，在沒有員工的情況下管理 60 家顧問客戶。

## 核心系統
- 每晚 21:00 自動為 60 家公司做分錄（5hr → 50min）
- 14 類會計科目用兩階段邏輯判斷（關鍵字字典 + Claude API fallback）
- 7 類排除規則避免錯帳
- MCP 串接 freee、Gmail、Calendar、Notion、Slack

## 可提煉的核心觀念
1. AI 不只是聊天工具，而是可作為業務總控台
2. 真正的價值不在寫程式，而在定義業務規則與判斷邊界
3. 高風險流程一定要先定義排除規則，再談自動化
4. 關鍵字字典 + LLM fallback 是很實用的雙層架構
5. CLAUDE.md / Skills / 排程 / MCP 結合後形成可持續放大的系統能力
6. 專業人士的優勢不在技術，而在現場知識與風險判斷能力
