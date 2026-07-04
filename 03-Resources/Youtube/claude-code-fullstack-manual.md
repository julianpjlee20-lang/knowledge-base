# 🧠 Claude Code 全端應用開發操作手冊
（以 Next.js + Prisma + Neon DB + Clerk 為範例）

> 本手冊依你提供的逐字稿整理，重點化成可執行的步驟、常用指令與最佳實踐，方便你直接照表操課。

---

## 目錄
- [專案概述](#專案概述)
- [開發環境設定](#開發環境設定)
  - [安裝 Node.js](#安裝-nodejs)
  - [安裝 Claude Code 與 IDE 外掛](#安裝-claude-code-與-ide-外掛)
- [建立 Next.js 專案](#建立-nextjs-專案)
- [Claude Code 常用指令速查](#claude-code-常用指令速查)
- [權限與設定](#權限與設定)
- [建議的開發工作流程](#建議的開發工作流程)
- [Git 與分支策略](#git-與分支策略)
- [整合 Clerk 身分驗證](#整合-clerk-身分驗證)
- [設定 Prisma + Neon DB](#設定-prisma--neon-db)
- [以「看板」功能作為第一個特性範例](#以看板功能作為第一個特性範例)
- [Claude Code 進階技巧](#claude-code-進階技巧)
  - [自訂 Slash Commands](#自訂-slash-commands)
  - [設計靈感導入與主題更新](#設計靈感導入與主題更新)
  - [同時運行多個代理人](#同時運行多個代理人)
  - [Hooks（事件觸發）](#hooks事件觸發)
  - [自訂 Sub-Agents](#自訂-sub-agents)
- [最佳實踐總結](#最佳實踐總結)

---

## 專案概述
**目標：** 建立一個具備登入系統的全端 CRM 網站。  
**技術架構：**
- **Next.js** — 前端與伺服器框架
- **Prisma** — ORM，連接資料庫
- **Neon DB (Postgres)** — 雲端資料庫（Serverless、可免費建立多個 DB）
- **Clerk** — 使用者認證
- **Claude Code** — AI 輔助開發（CLI + IDE 外掛）

---

## 開發環境設定

### 安裝 Node.js
```bash
node -v   # 檢查版本是否 >= 18
```
若版本過低，請至 https://nodejs.org 下載安裝新版。

### 安裝 Claude Code 與 IDE 外掛
```bash
npm install -g claude-code
```
IDE 推薦：**Cursor**（原生整合 Claude）、或 **VS Code / Windsurf**。  
安裝 **Claude Code Extension** 外掛以啟用：選取文字感知、Diff 檢視、標籤分頁感知等能力。

---

## 建立 Next.js 專案
```bash
npx create-next-app@latest
cd <project_name>
npm run dev
```
開啟瀏覽器：`http://localhost:3000`。  
在 IDE 內將此終端機命名為 **Server**，方便識別。

---

## Claude Code 常用指令速查
| 指令/操作 | 說明 |
|---|---|
| `?` | 顯示常用指令速覽 |
| `/` | 所有命令清單（命令選單） |
| `@<檔名>` | 附加檔案/資料夾為上下文（Context） |
| `Shift + Tab` | 切換「計畫模式（Plan）」與「自動編輯模式（Auto-accept edit）」 |
| `/init` | 掃描專案、產生 `claude.md` 總覽 |
| `/clear` | 清空對話上下文 |
| `/compact` | 將上一輪對話壓縮後帶入新會話 |
| `claude` | 互動式執行（CLI） |
| `claude -r` / `claude -` | 復原/續接前一次對話 |

> **建議：** 建立專案後先執行 `/init`，讓模型理解結構；功能開發使用 **Plan 模式**先產出計畫，再執行。

---

## 權限與設定
Claude Code 執行檔案操作時會詢問許可。兩種策略：

1. **快速模式（較少詢問）**
   ```bash
   claude --dangerously-skip-permissions
   ```

2. **安全設定模式（建議）**
   - 專案層設定：`.cloud/settings.local`
   - 全域層設定：`~/.claude/`
   - 可建立 **allow** / **deny** 規則（例如預設禁止刪檔）。

> 專案層設定可隨程式碼一同版控（GitHub），團隊共享一致規範。

---

## 建議的開發工作流程

1. **初始化骨架**
   - 建立 `Dashboard`、`Settings` 等核心頁面
   - 規劃固定側邊欄（Sidebar）與路由結構
2. **執行 `/init` 建立 `claude.md`**
3. **使用 Plan 模式撰寫提示**
   - 例：建立頁面、元件結構、路由與導航
4. **審查變更**
   - 透過 Git 面板檢視新增/修改（U/M）、使用 diff 決定 Stage/Revert
5. **頻繁 Commit**
   - 每次成功一輪工作就提交，以便出錯時回退
6. **完成後 `/clear`** 清空上下文，避免舊脈絡干擾新任務

---

## Git 與分支策略

- 每個功能建立 **feature branch**
- 測試穩定後 **Merge** 回 `main`
- 在終端或 IDE 內檢視分支：
  ```bash
  git status
  git switch -c feature/auth   # 建立新分支
  git switch main              # 回到主分支
  git merge feature/auth       # 合併
  ```
- 以一致格式撰寫 Commit 訊息（可請 AI 生成並模仿你的風格）

---

## 整合 Clerk 身分驗證

1. 於 [Clerk Dashboard](https://clerk.com) 建立應用並取得 API Keys  
2. 新增 `.env.local`：
   ```bash
   NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_************************
   CLERK_SECRET_KEY=sk_************************
   ```
3. 於 Next.js **根組件外層**加入 Clerk Provider（確保整站被保護）
4. 重新啟動開發伺服器：
   ```bash
   # 停止後再重啟
   Ctrl + C
   npm run dev
   ```
> 常見問題：登入元件跑到導航列外側，多源於 Layout/Provider 包覆層級錯誤。請檢查 `app/layout.tsx` 結構。

---

## 設定 Prisma + Neon DB

### 安裝與初始化
```bash
npm install prisma --save-dev
npx prisma init
```

### 建立 Neon DB 並設定連線
1. 登入 https://neon.tech 建立專案
2. 取得連線字串，加入 `.env`：
   ```bash
   DATABASE_URL="postgresql://<user>:<pass>@<host>/<db>?sslmode=require"
   ```

### 建立 Schema 與資料表
- 在 `prisma/schema.prisma` 定義模型，例如：
  ```prisma
  datasource db {
    provider = "postgresql"
    url      = env("DATABASE_URL")
  }

  generator client {
    provider = "prisma-client-js"
  }

  model User {
    id        String   @id @default(cuid())
    email     String   @unique
    createdAt DateTime @default(now())
    updatedAt DateTime @updatedAt
  }
  ```
- 推送到資料庫：
  ```bash
  npx prisma db push
  ```

> Neon（Serverless Postgres）優點：啟動/釋放按需計費、適合多專案與 AI 代理（含 PGVector）。

---

## 以「看板」功能作為第一個特性範例

**需求：**
- 新增 `Kanban` 頁面並列在 Sidebar
- 支援新增/編輯/拖曳卡片
- 以 API Routes 或 Server Actions 接後端（範例以 API Routes）

**Schema（示意）**
```prisma
model Board {
  id        String   @id @default(cuid())
  name      String
  columns   Column[]
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
}

model Column {
  id        String   @id @default(cuid())
  title     String
  order     Int
  board     Board    @relation(fields: [boardId], references: [id])
  boardId   String
  cards     Card[]
}

model Card {
  id        String   @id @default(cuid())
  title     String
  description String?
  order     Int
  column    Column   @relation(fields: [columnId], references: [id])
  columnId  String
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
}
```
推送：
```bash
npx prisma db push
```

**前端頁面（重點）**
- `app/(protected)/kanban/page.tsx`：載入使用者、抓取 Board/Column/Card，提供拖曳（如 `@dnd-kit`）
- `app/api/cards/*`：CRUD API（新增卡片、更新排序、改變 column 等）

> 提示：先以「假資料（dummy JSON）」快速成形 UI，確認體驗後再接資料庫。

---

## Claude Code 進階技巧

### 自訂 Slash Commands
建立資料夾 `.claude/commands/`，新增如 `design-mode.md`，內容可規範：
- 僅用 **dummy JSON** 作為資料來源
- 先產出 UI，暫不連後端
- 建立/更新色彩主題與元件風格

使用方式：在對話輸入 `/design-mode` 觸發。

### 設計靈感導入與主題更新
- 從 Dribbble/Pinterest 擷取參考圖，貼到對話並附上說明
- 讓 Claude 依配色更新 `tailwind.config.ts` / 全域 CSS / 元件 Token

### 同時運行多個代理人
- 於 IDE 左側面板開多個 Claude 視窗
- 一個跑前端、另一個處理資料庫/後端

### Hooks（事件觸發）
- 例：**回應結束時** 播放音效提示「Your agent has finished」
- 例：**破壞性指令前**（刪檔、`sudo`、drop table）強制人工確認
- 例：**提交前** 自動跑 Lint/Prettier/Test

### 自訂 Sub-Agents
- 以表單引導建立子代理（如「React/Next.js 產線等級審查員」）
- 在主代理描述中詳述何時呼叫子代理（如完成大型變更後自動審查/補測試）

---

## 最佳實踐總結

| 主題 | 建議 |
|---|---|
| 開發節奏 | 小步快跑 → Commit → 測試 → Merge |
| Context 管理 | 常用 `/clear` 與精準 `@檔案` 供給上下文 |
| 記憶 | `#` 新增「專案記憶」：如避免重複啟動 `npm run dev` |
| 變更審查 | 善用 Git 面板 Stage/Revert、保持整潔提交歷史 |
| 安全性 | 以設定檔管理 allow/deny、重要操作前加 Hook |
| 文檔化 | 讓 `.claude/` 與專案 README 一起版控，團隊共享 |

---

### Appendix：常用指令彙整
```bash
# Claude Code（CLI）
claude                     # 互動模式
claude -r                  # 繼續前一次會話
claude --dangerously-skip-permissions

# Next.js
npx create-next-app@latest
npm run dev

# Prisma
npm install prisma --save-dev
npx prisma init
npx prisma db push

# Git
git switch -c feature/<name>
git switch main
git merge feature/<name>
```

---

> 如需將此手冊轉為 PDF 或加入你的 Notion 模板，我可再幫你輸出對應格式與風格。

