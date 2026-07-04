---
created: 2026-01-18T00:00:00
title: "Next.js + Supabase + Claude Code Skills 研究整理"
tags: [ai-development, backend, claude, claude-code, nextjs, projects, research, supabase, web-development]
related:
  - "[[2025-01-22-Claude-Code-Skills-MCP-Agent-Guide]]"
  - "[[claude-md-best-practices]]"
  - "[[Claude Skills]]"
  - "[[2026-01-22-Claude-Skills-Registry]]"
  - "[[01-CLAUDE-MD]]"
---

# Next.js + Supabase + Claude Code Skills 研究整理

> 整理日期：2026-01-18

---

## 一、高星 GitHub Repo 總覽

### 核心框架 (60k+ Stars)

| Repo | Stars | 說明 |
|------|-------|------|
| [supabase/supabase](https://github.com/supabase/supabase) | ~96k ⭐ | 開源 Firebase 替代方案，Postgres 開發平台 |

### Next.js SaaS Starter Templates

| Repo | Stars | 技術棧 | Supabase 支援 |
|------|-------|--------|--------------|
| [vercel/nextjs-subscription-payments](https://github.com/vercel/nextjs-subscription-payments) | ~7.6k ⭐ | Next.js + Supabase + Stripe | ✅ 完整支援 (Auth + DB + RLS) |
| [nextjs/saas-starter](https://github.com/nextjs/saas-starter) | - | Next.js + Postgres + Drizzle + Stripe | ❌ 通用 Postgres（可連 Supabase DB） |

> ⚠️ `vercel/nextjs-subscription-payments` 已於 2025/01/23 封存，官方建議改用 `nextjs/saas-starter`

---

## 二、技術棧比較

### vercel/nextjs-subscription-payments (已封存)

| 項目 | 技術 |
|------|------|
| Framework | Next.js |
| Auth | ✅ Supabase Auth |
| Database | ✅ Supabase (PostgreSQL) |
| Payments | Stripe Checkout + Customer Portal |
| Security | ✅ Row Level Security (RLS) |

### nextjs/saas-starter (活躍維護)

| 項目 | 技術 |
|------|------|
| Framework | Next.js |
| Auth | 自建 JWT + Cookie |
| Database | 通用 Postgres |
| ORM | Drizzle |
| Payments | Stripe |
| UI | shadcn/ui |

#### 內建 Auth 功能
- ✅ Email/Password 註冊登入
- ✅ JWT Token 管理
- ✅ Cookie-based Session
- ✅ 路由保護 (middleware)
- ✅ RBAC (Owner / Member 角色)

---

## 三、Authentication 方案比較

| 方案 | 優點 | 缺點 |
|------|------|------|
| **自建 (saas-starter)** | 完全掌控、無依賴 | 需自己維護安全性 |
| **Supabase Auth** | 功能完整、OAuth 整合 | 綁定 Supabase |
| **NextAuth.js** | 彈性高、50+ providers | 設定較複雜 |
| **Clerk** | UI 美觀、功能強大 | 付費 |

### 選擇建議

| 情境 | 建議 |
|------|------|
| 內部工具 / B2B | 自建 Auth 夠用 |
| 面向消費者 (B2C) | NextAuth.js（社群登入） |
| 台灣市場 | NextAuth.js（LINE 登入必備） |

---

## 四、Claude Code Skills 資源

| Repo | 說明 |
|------|------|
| [Nice-Wolf-Studio/claude-code-supabase-skills](https://github.com/Nice-Wolf-Studio/claude-code-supabase-skills) | Supabase API skills |
| [laguagu/claude-code-nextjs-skills](https://github.com/laguagu/claude-code-nextjs-skills) | Next.js 16 + AI SDK |
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | Skills 資源整理 |

---

## 五、參考資料

- [Supabase 官方文件](https://supabase.com/docs)
- [Next.js 官方文件](https://nextjs.org/docs)
- [NextAuth.js 官方文件](https://authjs.dev/)
- [Drizzle ORM 文件](https://orm.drizzle.team/)
---
created: 2026-01-18T00:00:00
category: Projects
tags: [projects, nextjs, supabase, claude-code, backend, research]
---

# Next.js + Supabase + Claude Code Skills 研究整理

> 整理日期：2026-01-18

---

## 一、高星 GitHub Repo 總覽

### 核心框架 (60k+ Stars)

| Repo | Stars | 說明 |
|------|-------|------|
| [supabase/supabase](https://github.com/supabase/supabase) | ~96k ⭐ | 開源 Firebase 替代方案，Postgres 開發平台 |

### Next.js SaaS Starter Templates

| Repo | Stars | 技術棧 | Supabase 支援 |
|------|-------|--------|--------------|
| [vercel/nextjs-subscription-payments](https://github.com/vercel/nextjs-subscription-payments) | ~7.6k ⭐ | Next.js + Supabase + Stripe | ✅ 完整支援 (Auth + DB + RLS) |
| [nextjs/saas-starter](https://github.com/nextjs/saas-starter) | - | Next.js + Postgres + Drizzle + Stripe | ❌ 通用 Postgres（可連 Supabase DB） |

> ⚠️ `vercel/nextjs-subscription-payments` 已於 2025/01/23 封存，官方建議改用 `nextjs/saas-starter`

---

## 二、技術棧比較

### vercel/nextjs-subscription-payments (已封存)

| 項目 | 技術 |
|------|------|
| Framework | Next.js |
| Auth | ✅ Supabase Auth |
| Database | ✅ Supabase (PostgreSQL) |
| Payments | Stripe Checkout + Customer Portal |
| Security | ✅ Row Level Security (RLS) |
| 特色 | Stripe Webhooks → Supabase 自動同步 |

### nextjs/saas-starter (活躍維護)

| 項目 | 技術 |
|------|------|
| Framework | Next.js |
| Auth | 自建 JWT + Cookie |
| Database | 通用 Postgres |
| ORM | Drizzle |
| Payments | Stripe |
| UI | shadcn/ui |

#### 內建 Auth 功能

```
✅ Email/Password 註冊登入
✅ JWT Token 管理
✅ Cookie-based Session
✅ 路由保護 (middleware)
✅ RBAC (Owner / Member 角色)
✅ Team/Organization 管理
```

#### 適用的 Postgres 服務

- Vercel Postgres
- Neon (Serverless)
- Supabase (僅當 DB)
- Railway
- AWS RDS

---

## 三、Supabase 功能整合分析

### nextjs/saas-starter + Supabase 結合可行性

| 功能 | 原本 (saas-starter) | 可加入 (Supabase) |
|------|---------------------|-------------------|
| Database | Postgres + Drizzle | ✅ 可直接連 Supabase Postgres |
| Auth | 自建 JWT + Cookie | 🔄 可替換為 Supabase Auth |
| Realtime | ❌ 無 | ➕ 可加入 |
| Storage | ❌ 無 | ➕ 可加入 |
| Edge Functions | ❌ 無 | ➕ 可加入 |

### 整合策略建議

**方案 A：最小改動（推薦）**
```
保留 Drizzle ORM → 連接 Supabase Postgres
                 → 只加入 Storage / Realtime 功能
                 → 保留原有 JWT Auth
```

**方案 B：完整 Supabase 化**
```
移除 Drizzle → 改用 supabase-js client
            → 替換為 Supabase Auth
            → 等於重寫大部分程式碼
```

### ⚠️ 潛在挑戰

| 問題 | 說明 |
|------|------|
| ORM 衝突 | Drizzle vs supabase-js client |
| Auth 整合 | 原有 JWT vs Supabase Auth 需選擇 |
| Schema 同步 | Drizzle migrations vs Supabase migrations |
| Type 生成 | Drizzle 自動生成 vs Supabase CLI |

---

## 四、Authentication 方案比較

### 各方案對比

| 方案 | 優點 | 缺點 |
|------|------|------|
| **自建 (saas-starter)** | 完全掌控、無依賴 | 需自己維護安全性 |
| **Supabase Auth** | 功能完整、OAuth 整合 | 綁定 Supabase |
| **NextAuth.js (Auth.js)** | 彈性高、50+ providers | 設定較複雜 |
| **Clerk** | UI 美觀、功能強大 | 付費、第三方依賴 |

### NextAuth.js vs 自建 Auth 功能對比

| 功能 | saas-starter 自建 | NextAuth.js |
|------|------------------|-------------|
| Email/Password | ✅ | ✅ |
| OAuth (Google, GitHub 等) | ❌ 需自己寫 | ✅ 50+ providers |
| Magic Link | ❌ 需自己寫 | ✅ 內建 |
| LINE 登入 | ❌ | ✅ 有 provider |
| JWT Session | ✅ | ✅ |
| Drizzle 整合 | ✅ 原生 | ✅ 有 adapter |

### 選擇建議

| 情境 | 建議 |
|------|------|
| 內部工具 / B2B | 自建 Auth 夠用 |
| 面向消費者 (B2C) | 建議 NextAuth.js（社群登入） |
| 台灣市場 | NextAuth.js（LINE 登入必備） |
| MVP 快速驗證 | 先用自建，之後再換 |

---

## 五、Claude Code Skills 資源

### Supabase 相關 Skills

| Repo | 說明 |
|------|------|
| [Nice-Wolf-Studio/claude-code-supabase-skills](https://github.com/Nice-Wolf-Studio/claude-code-supabase-skills) | 完整 Supabase API skills（Auth、Storage、Realtime、Edge Functions） |

### Next.js 相關 Skills

| Repo | 說明 |
|------|------|
| [laguagu/claude-code-nextjs-skills](https://github.com/laguagu/claude-code-nextjs-skills) | Next.js 16 + AI SDK + pgvector + Ralph Loop |
| [wsimmonds/claude-nextjs-skills](https://github.com/wsimmonds/claude-nextjs-skills) | 針對 Next.js evals 優化 |

### 綜合 Skills 集合

| Repo | 說明 |
|------|------|
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | Claude Skills 資源整理 |
| [VoltAgent/awesome-claude-skills](https://github.com/VoltAgent/awesome-claude-skills) | Claude Skills 集合 |
| [lodetomasi/agents-claude-code](https://github.com/lodetomasi/agents-claude-code) | 100+ 專業 AI agents（含 supabase-specialist） |

---

## 六、選擇決策樹

```
需要完整 Supabase 功能？
├── 是 → vercel/nextjs-subscription-payments (已封存但可用)
│        或其他 Supabase 原生 starter
│
└── 否 → nextjs/saas-starter
         │
         ├── 只需 Email/Password？
         │   └── 保持自建 Auth ✅
         │
         ├── 需要 OAuth 社群登入？
         │   └── 整合 NextAuth.js
         │
         └── 需要 Realtime/Storage？
             └── 加入部分 Supabase 功能
```

---

## 七、參考資料

- [Supabase 官方文件](https://supabase.com/docs)
- [Next.js 官方文件](https://nextjs.org/docs)
- [NextAuth.js 官方文件](https://authjs.dev/)
- [Drizzle ORM 文件](https://orm.drizzle.team/)

---

## 相關筆記

- [[2025-01-22-Claude-Code-Skills-MCP-Agent-Guide]]
- [[claude-md-best-practices]]
- [[Claude Skills]]
- [[2026-01-22-Claude-Skills-Registry]]
- [[01-CLAUDE-MD]]
