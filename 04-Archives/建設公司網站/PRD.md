# 建設公司網站 PRD（產品需求文件）

**版本**：v1.7  
**建立日期**：2026-01-30  
**更新日期**：2026-01-31  
**狀態**：草稿

---

## 1. 產品概述

### 1.1 產品名稱
建設公司官方網站（含會員系統）

### 1.2 產品目標
- 展示公司形象與工程實績
- 提供客戶專屬登入區域
- 讓客戶可查看工程進度
- 提供線上修繕申請
- 支援雙語（繁中/英文）

### 1.3 目標用戶
| 用戶類型 | 說明 |
|---------|------|
| 一般訪客 | 瀏覽公司資訊、查看作品集 |
| 潛在客戶 | 詢價、聯絡、了解服務 |
| 現有客戶 | 登入查看進度、申請修繕 |
| 管理員 | 後台管理所有內容與會員 |

### 1.4 客服管道

| 階段 | 情境 | 處理方式 |
|------|------|---------|
| 銷售前 | 潛在客戶詢價、看屋預約 | LINE / FB 導流 |
| 銷售中 | 簽約流程、付款問題 | 電話 / 1對1 |
| 施工中 | 客變需求、進度詢問 | 電話 / 1對1 |
| 交屋後 | 保固修繕 | 網站修繕申請 |
| 一般 | 投訴、建議、其他問題 | 電話 / 1對1 |

---

## 2. 功能需求

### 2.1 公開頁面（訪客可見）

| 頁面 | 功能說明 |
|-----|---------|
| 首頁 | 公司亮點、精選作品、服務概覽、CTA |
| 關於我們 | 公司介紹、理念、團隊、歷史 |
| 服務項目 | 建設服務類型、流程說明 |
| 工程實績 | 作品集展示（圖片、說明、分類篩選） |
| 最新消息 | 公司新聞、活動、部落格文章 |
| 聯絡我們 | 聯絡表單、地圖、電話、Email、社群 icon |
| 會員登入 | 客戶登入入口 |

### 2.2 會員系統（客戶登入後）

| 功能 | 說明 |
|-----|------|
| 我的專案 | 查看進行中/已完成的工程 |
| 工程進度 | 里程碑顯示（大項 + 細項 Toggle 展開），僅查看，不可發問 |
| 修繕申請 | 提交保固維修申請、查看處理狀態 |
| 個人設定 | 修改密碼、聯絡資訊 |

### 2.3 修繕申請功能

#### 申請欄位

| 欄位 | 必填 | 說明 |
|------|------|------|
| 所屬專案 | ✅ | 自動帶入 |
| 問題類型 | ✅ | 結構/管線/公設/其他（後台可增減） |
| 問題描述 | ✅ | 文字輸入 |
| 上傳照片 | ✅ | 可多張 |
| 聯絡電話 | ✅ | 自動帶入（會員資料） |

#### 修繕狀態

| 狀態 | 說明 |
|------|------|
| 處理中 | 收件到結案前 |
| 已結案 | 客戶確認滿意 |

#### 修繕流程

```
客戶提交申請
    │
    ▼
客服收到 → 派工給工務
    │
    ▼
工務處理 → 回報已處理
    │
    ▼
客服通知客戶確認
    │
    ▼
客戶確認滿意 → 結案
    │
   （不滿意）→ 重新處理
```

### 2.4 後台管理系統（自建 CMS）

| 模組 | 功能 |
|-----|------|
| 內容管理 | 編輯所有頁面文字、圖片（固定欄位） |
| 作品集管理 | 新增/編輯/刪除工程案例（對外展示用） |
| 新聞管理 | 發布/編輯/下架文章 |
| 會員管理 | 新增客戶帳號、重設密碼、停用帳號 |
| 專案管理 | 建立專案、更新進度（客戶服務用） |
| 修繕管理 | 查看申請、更新狀態、結案 |
| 統計報表 | 流量儀表板、修繕報表、PDF 匯出、Email 定期寄送 |
| 系統設定 | 網站基本資訊、下拉選單管理 |

### 2.5 內容管理功能

#### 編輯方式
- 固定欄位（非區塊編輯器）

### 2.6 作品集管理功能

#### 欄位

| 欄位 | 必填 | 說明 |
|------|------|------|
| 案名 | ✅ | 建案名稱 |
| 地點 | ✅ | 自由輸入（已完工填地址，預售填行政區+路段） |
| 類型 | ✅ | 下拉選單（後台可增減） |
| 圖集 | ✅ | 多張照片，可選一張當封面 |
| 說明 | ✅ | 段落文字，含建築特色（條列式） |
| 預計完工日期 | ✅ | 預售填預計，已完工填實際 |
| 規格數據 | ✅ | 戶數、坪數、樓層等（表格） |
| FAQ | ✅ | 常見問答（Toggle 呈現） |
| Alt 文字 | 自動 | 自動帶入「{案名} - 照片{編號}」，可手動修改 |

#### 圖片處理
- 上傳多張後，點選其中一張設為封面
- 自動壓縮，加快載入
- 自動產生不同尺寸（桌機/手機）
- 自動轉成 WebP 格式

### 2.7 新聞管理功能

#### 欄位

| 欄位 | 必填 | 說明 |
|------|------|------|
| 標題 | ✅ | 新聞標題 |
| 封面圖 | ✅ | 列表顯示用 |
| 內容 | ✅ | 文章內文 |
| 分類 | ✅ | 主題式分類（後台可增減） |
| 發布日期 | ✅ | 何時發布 |
| 狀態 | ✅ | 草稿/已發布/下架 |

#### 分類（AI SEO 優化）

| 分類 | 內容範例 | AI SEO 價值 |
|------|---------|-------------|
| 購屋知識 | 買房注意事項、貸款攻略、交屋流程 | 高 |
| 建案情報 | 新案動工、完工資訊、銷售資訊 | 高 |
| 公司消息 | 得獎、活動、公告 | 低 |

後台可新增/編輯/刪除分類。

### 2.8 系統設定功能

#### 網站基本資訊

| 欄位 | 必填 | 說明 |
|------|------|------|
| 公司名稱（中文） | ✅ | 繁中網站顯示 |
| 公司名稱（英文） | ✅ | 英文網站顯示 |
| Logo | ✅ | 網站 Logo |
| 電話 | ✅ | 公司電話 |
| Email | ✅ | 聯絡信箱 |
| 地址 | ✅ | 公司地址 |
| 營業時間 | ✅ | 例：週一至週五 9:00-18:00 |
| LINE 連結 | ✅ | 官方帳號連結 |
| Facebook 連結 | ✅ | 粉絲專頁連結 |
| Instagram 連結 | ✅ | IG 連結 |

#### 社群連結前端呈現

| 欄位 | 前端呈現 |
|------|---------|
| LINE | LINE icon，點擊跳轉 |
| Facebook | FB icon，點擊跳轉 |
| Instagram | IG icon，點擊跳轉 |

不顯示文字連結或 QR code。

#### 下拉選單管理

統一管理所有下拉選單選項：

| 選單 | 用途 |
|------|------|
| 維修類型 | 結構/管線/公設/其他 |
| 作品集類型 | 住宅/商業/室內裝修 |
| 新聞分類 | 購屋知識/建案情報/公司消息 |

後台可新增/編輯/刪除選項。

#### SEO 設定

SEO 相關設定自動產生，不需手動輸入：

| 項目 | 自動產生來源 |
|------|-------------|
| Meta Title | 「{頁面名稱} - {公司名稱}」 |
| Meta Description | 從頁面內容第一段自動摘要 |
| OG Image | 使用公司 Logo 或頁面封面圖 |
| 結構化資料 Organization | 從網站基本資訊自動產生 |
| 結構化資料 LocalBusiness | 從公司地址、電話自動產生 |
| 結構化資料 FAQPage | 從作品集 FAQ 自動產生 |
| robots.txt | 預設允許 AI 爬蟲 |
| Sitemap | 自動產生 |

### 2.9 統計報表功能

#### 後台儀表板（摘要）

| 項目 | 說明 |
|------|------|
| 本月訪客數 | 不重複訪客人數 |
| 熱門頁面 TOP 5 | 最多人瀏覽的頁面 |
| 流量來源 | Google、AI、社群、直接輸入 |
| 會員登入次數 | 客戶活躍度 |

#### 修繕報表（摘要）

| 項目 | 說明 |
|------|------|
| 本月修繕件數 | 總共幾件 |
| 處理中件數 | 尚未結案 |
| 已結案件數 | 客戶確認完成 |
| 平均處理天數 | 從提交到結案 |
| 依類型統計 | 結構/管線/公設/其他 各幾件 |

#### PDF / Email 報表

| 頁次 | 內容 |
|------|------|
| 第 1 頁 | 摘要（流量 + 修繕） |
| 第 2 頁之後 | 完整數據 |

#### 完整數據包含

| 類別 | 項目 |
|------|------|
| 流量 | 訪客數、瀏覽量、平均停留時間、跳出率、新/回訪客 |
| 來源 | 流量來源、搜尋關鍵字、來源網站 |
| 頁面 | 熱門頁面、進入頁面、離開頁面 |
| 用戶 | 裝置類型、地區、瀏覽器 |
| 會員 | 登入次數、活躍度 |
| 修繕 | 件數、狀態、處理天數、類型統計 |

#### 報表發送

| 功能 | 說明 |
|------|------|
| 手動匯出 | 後台點擊下載 PDF |
| 定期寄送 | 每週/每月自動寄 Email 給指定收件人 |

---

## 3. 非功能需求

### 3.1 設計規範
- **風格**：現代簡約（白底、大量留白）
- **響應式**：支援桌機、平板、手機
- **語言**：繁體中文 / English 切換

### 3.2 效能需求
- 首頁載入 < 3 秒
- 圖片自動壓縮優化
- CDN 加速靜態資源

### 3.3 安全需求
- HTTPS 加密
- 會員密碼雜湊儲存
- 防 SQL Injection / XSS
- 定期備份

### 3.4 SEO 需求

#### 傳統 SEO（自動產生）
- Meta 標籤自動產生
- Sitemap 自動產生
- robots.txt 預設允許 AI 爬蟲

#### AI SEO（自動產生）
- 結構化資料（JSON-LD）：Organization、LocalBusiness、FAQPage
- 允許 AI 爬蟲（GPTBot、PerplexityBot）
- 內容撰寫規範（參考 CMS 後台操作手冊）

---

## 4. 技術規格

### 4.1 技術選型

| 項目 | 選擇 | 說明 |
|------|------|------|
| 前端框架 | Next.js 14 | App Router |
| 後台管理 | 自建 CMS | 配合公司需求客製 |
| 資料庫 | PostgreSQL | 託管於 Railway（新加坡） |
| 圖片儲存 | Cloudflare R2 | CDN 加速、免流量費 |
| 部署 | Vercel + Railway | 前端 Vercel、後端 Railway |
| 認證 | NextAuth.js | Email + 密碼，保留社群登入彈性 |
| 多語系 | next-intl | 繁中 / English（第一版） |
| 流量分析 | Google Analytics 4 | 串接 API 產出報表 |

### 4.2 會員機制

| 項目 | 說明 |
|------|------|
| 註冊方式 | 邀請制（後台建立帳號，寄發邀請信） |
| 登入方式 | Email + 密碼（未來可加 Google/FB/IG） |
| 權限隔離 | 每位客戶只能看到自己的專案資料 |

### 4.3 費用預估

| 項目 | 月費 |
|------|------|
| Vercel（前端） | 免費 ~ $20 |
| Railway（後端 + DB） | $10 ~ $25 |
| Cloudflare R2（圖片） | 免費 ~ $5 |
| **合計** | **$10 ~ $50/月** |

---

## 5. 資料庫設計

### 5.1 資料表清單

| 資料表 | 用途 |
|--------|------|
| users | 管理員帳號 |
| members | 客戶會員 |
| projects | 專案 |
| project_members | 專案 ↔ 會員關聯 |
| project_milestones | 工程里程碑（大項） |
| milestone_tasks | 里程碑細項（Toggle 展開） |
| repair_requests | 維修申請 |
| repair_images | 維修照片 |
| content_blocks | CMS 頁面內容 |
| portfolios | 作品集 |
| portfolio_images | 作品集圖片 |
| portfolio_faqs | 作品集 FAQ |
| posts | 新聞文章 |
| site_settings | 網站基本資訊 |
| dropdown_options | 下拉選單統一管理 |

### 5.2 資料表結構

#### users（管理員）

```sql
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  name VARCHAR(100) NOT NULL,
  role VARCHAR(50) DEFAULT 'admin',
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

#### members（客戶會員）

```sql
CREATE TABLE members (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  name VARCHAR(100) NOT NULL,
  phone VARCHAR(20),
  
  invited_by UUID REFERENCES users(id),
  invited_at TIMESTAMPTZ,
  first_login_at TIMESTAMPTZ,
  
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

#### projects（專案）

```sql
CREATE TABLE projects (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(255) NOT NULL,
  location TEXT,
  type_id UUID REFERENCES dropdown_options(id),
  
  status VARCHAR(50) DEFAULT 'in_progress',
  progress_percent INT DEFAULT 0,
  expected_completion DATE,
  actual_completion DATE,
  
  is_public BOOLEAN DEFAULT false,
  cover_image_url TEXT,
  description TEXT,
  specs JSONB,
  
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

#### project_members（專案 ↔ 會員關聯）

```sql
CREATE TABLE project_members (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  project_id UUID REFERENCES projects(id) ON DELETE CASCADE,
  member_id UUID REFERENCES members(id) ON DELETE CASCADE,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  
  UNIQUE(project_id, member_id)
);
```

#### project_milestones（工程里程碑）

```sql
CREATE TABLE project_milestones (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  project_id UUID REFERENCES projects(id) ON DELETE CASCADE,
  
  title VARCHAR(255) NOT NULL,
  sort_order INT DEFAULT 0,
  status VARCHAR(50) DEFAULT 'pending',
  completed_at TIMESTAMPTZ,
  
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

#### milestone_tasks（里程碑細項）

```sql
CREATE TABLE milestone_tasks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  milestone_id UUID REFERENCES project_milestones(id) ON DELETE CASCADE,
  
  title VARCHAR(255) NOT NULL,
  sort_order INT DEFAULT 0,
  status VARCHAR(50) DEFAULT 'pending',
  completed_at TIMESTAMPTZ,
  
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

#### repair_requests（維修申請）

```sql
CREATE TABLE repair_requests (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  project_id UUID REFERENCES projects(id) ON DELETE CASCADE,
  member_id UUID REFERENCES members(id) ON DELETE CASCADE,
  repair_type_id UUID REFERENCES dropdown_options(id),
  
  description TEXT NOT NULL,
  contact_phone VARCHAR(20) NOT NULL,
  status VARCHAR(50) DEFAULT 'pending',
  
  submitted_at TIMESTAMPTZ DEFAULT NOW(),
  completed_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

#### repair_images（維修照片）

```sql
CREATE TABLE repair_images (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  repair_request_id UUID REFERENCES repair_requests(id) ON DELETE CASCADE,
  image_url TEXT NOT NULL,
  sort_order INT DEFAULT 0,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

#### content_blocks（CMS 頁面內容）

```sql
CREATE TABLE content_blocks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  
  page VARCHAR(100) NOT NULL,
  block_key VARCHAR(100) NOT NULL,
  
  content_zh TEXT,
  content_en TEXT,
  
  updated_by UUID REFERENCES users(id),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  
  UNIQUE(page, block_key)
);
```

#### portfolios（作品集）

```sql
CREATE TABLE portfolios (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  
  name_zh VARCHAR(255) NOT NULL,
  name_en VARCHAR(255),
  
  location_zh TEXT,
  location_en TEXT,
  
  type_id UUID REFERENCES dropdown_options(id),
  
  description_zh TEXT,
  description_en TEXT,
  
  specs JSONB,
  
  completion_date DATE,
  cover_image_url TEXT,
  
  is_published BOOLEAN DEFAULT false,
  sort_order INT DEFAULT 0,
  
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

#### portfolio_images（作品集圖片）

```sql
CREATE TABLE portfolio_images (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  portfolio_id UUID REFERENCES portfolios(id) ON DELETE CASCADE,
  
  image_url TEXT NOT NULL,
  alt_zh VARCHAR(255),
  alt_en VARCHAR(255),
  sort_order INT DEFAULT 0,
  
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

#### portfolio_faqs（作品集 FAQ）

```sql
CREATE TABLE portfolio_faqs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  portfolio_id UUID REFERENCES portfolios(id) ON DELETE CASCADE,
  
  question_zh TEXT NOT NULL,
  question_en TEXT,
  answer_zh TEXT NOT NULL,
  answer_en TEXT,
  
  sort_order INT DEFAULT 0,
  
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

#### posts（新聞文章）

```sql
CREATE TABLE posts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  
  title_zh VARCHAR(255) NOT NULL,
  title_en VARCHAR(255),
  
  content_zh TEXT NOT NULL,
  content_en TEXT,
  
  category_id UUID REFERENCES dropdown_options(id),
  cover_image_url TEXT,
  
  status VARCHAR(50) DEFAULT 'draft',
  published_at TIMESTAMPTZ,
  
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

#### site_settings（網站基本資訊）

```sql
CREATE TABLE site_settings (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  
  setting_key VARCHAR(100) UNIQUE NOT NULL,
  value_zh TEXT,
  value_en TEXT,
  
  updated_by UUID REFERENCES users(id),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

#### dropdown_options（下拉選單統一管理）

```sql
CREATE TABLE dropdown_options (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  
  category VARCHAR(100) NOT NULL,
  
  name_zh VARCHAR(100) NOT NULL,
  name_en VARCHAR(100),
  
  sort_order INT DEFAULT 0,
  is_active BOOLEAN DEFAULT true,
  
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### 5.3 ER 關係圖

```
users (管理員)
  │
  ├── invited → members (客戶)
  │                │
  │                └── project_members ──┐
  │                │                     │
  │                └── repair_requests ──┼── projects
  │                                      │      │
  └── updated_by → content_blocks        │      ├── project_milestones
                   site_settings         │      │      └── milestone_tasks
                                         │      │
                                         │      └── (權限隔離)

dropdown_options ← 被多個資料表參照（類型、分類）

portfolios
  ├── portfolio_images
  └── portfolio_faqs

repair_requests
  └── repair_images
```

---

## 6. 頁面架構

```
首頁
├── 關於我們
│   ├── 公司介紹
│   ├── 經營團隊
│   └── 公司沿革
├── 服務項目
│   ├── 住宅建設
│   ├── 商業建設
│   └── 室內裝修
├── 工程實績
│   ├── [依分類篩選]
│   └── [個別案例頁]
├── 最新消息
│   ├── [依分類篩選]
│   └── [文章頁]
├── 聯絡我們
└── 會員專區（登入後）
    ├── 我的專案
    ├── 工程進度
    ├── 修繕申請
    └── 個人設定
```

---

## 7. 時程規劃（6 週）

| 週次 | 工作項目 |
|-----|---------|
| Week 1 | 環境建置、設計稿確認、資料庫建立 |
| Week 2 | 公開頁面開發、多語系設定 |
| Week 3 | 自建 CMS 後台開發 |
| Week 4 | 會員系統開發、權限控制 |
| Week 5 | 修繕功能、統計報表 |
| Week 6 | 測試、修正、上線部署 |

---

## 8. 待確認事項

- [ ] 公司名稱與 Logo
- [ ] 網域名稱
- [ ] 現有素材（照片、文案）
- [ ] 會員數量預估

---

## 9. 未來功能

以下功能暫不開發，保留未來擴充：

| 功能 | 說明 |
|------|------|
| 文件下載 | 客戶下載合約、設計圖等文件 |
| A/B Testing | 內容版本測試、轉換率追蹤 |
| AI 輔助編輯 | 後台內容編輯 AI 建議 |
| 維修派工指派 | 記錄指派給哪位工務 |
| 維修內部備註 | 客服/工務內部備註（客戶看不到） |
| 客戶滿意度回饋 | 結案時客戶填寫滿意度 |
| 社群登入 | Google / Facebook / Instagram 登入 |

---

## 10. 相關文件

- [CMS 後台操作手冊](CMS後台操作手冊.md)

---

**文件結束**
