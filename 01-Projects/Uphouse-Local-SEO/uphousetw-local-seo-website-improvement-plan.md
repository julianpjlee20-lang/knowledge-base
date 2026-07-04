---
title: Uphouse 官網 Local SEO 修改清單
created: 2026-05-31
updated: 2026-05-31
type: query
tags: [seo, local-seo, website, uphouse]
sources:
  - https://uphousetw.zeabur.app/
  - https://uphousetw.zeabur.app/projects/eight
  - https://uphousetw.zeabur.app/sitemap.xml
  - https://uphousetw.zeabur.app/robots.txt
---

# Uphouse 官網 Local SEO 修改清單

## 背景

本頁整理 YouTube 影片「Local SEO / Google Business Profile / Claude Code SEO workflow」的重點，並套用到向上建設新版官網：

- 測試站：<https://uphousetw.zeabur.app/>
- 重點頁：<https://uphousetw.zeabur.app/projects/eight>
- 目標：把網站從「品牌形象頁」升級成「苗栗 / 後龍 / 高鐵特區購屋搜尋流量接收器」。

相關方向可連到 [[dankoe-creator-economy]] 的「公開內容累積資產」觀念：SEO 不是一次性投放，而是長期累積可被搜尋的內容資產。也可連到 [[高效經理人手冊]] 的流程化概念：把 SEO 變成可重複執行的網站與內容 SOP。

---

## 一句話結論

新版站的品牌質感與建案資料已經比舊站好很多，但要吃到 Google 在地流量，接下來最重要的不是再做漂亮，而是補齊：

1. 技術 SEO 基礎修正
2. 正式網域與 canonical 策略
3. 建案頁 SEO 強化
4. 苗栗 / 後龍 / 高鐵特區在地 landing pages
5. Google 商家檔案、評論、Google Maps 閉環
6. 最新消息內容中心

---

## 已檢查到的現況

### 做得好的地方

- 首頁有 H1：`向上 建設`
- 首頁 title：`向上建設 | 建築與生活的編輯式提案`
- 首頁 meta description 已設定
- 有 sitemap：`/sitemap.xml`
- 有 robots：`/robots.txt`
- 建案有獨立頁：`/projects/eight`
- 八宅頁資料完整，包含：
  - 地址
  - 坪數
  - 價格
  - 格局
  - 公設比
  - 車位
  - 交屋時間
  - 地圖
- HTML 原始碼可讀到主要內容，對 SEO 比純 CSR 好。
- 有基本 structured data：
  - 首頁：`Organization`
  - 八宅頁：`RealEstateListing`

### 明顯問題

- `robots.txt` 內 sitemap 還是 `https://example.com/sitemap.xml`，必修。
- 沒看到 canonical，正式網域上線後容易產生 Zeabur 網址與正式網域重複收錄。
- `/news` 目前幾乎是空頁，浪費內容 SEO 入口。
- Sitemap 目前頁數太少，缺少在地關鍵字 landing pages。
- 八宅頁 title 偏資料型，還沒有充分覆蓋搜尋者會打的關鍵字。
- 建案頁缺 FAQ、適合族群、生活圈、購屋決策內容。
- 尚未看到 Google 商家檔案 / Google 評論 / Google Maps 與網站的閉環。
- 八宅頁 cache header 顯示 `no-store` 類型，公開 SEO 頁不建議長期如此。

---

# 第一階段：立刻修的技術 SEO

## 1. 修正 robots.txt

目前錯誤：

```txt
Sitemap: https://example.com/sitemap.xml
```

Zeabur 測試站應改為：

```txt
Sitemap: https://uphousetw.zeabur.app/sitemap.xml
```

正式網域上線後應改為：

```txt
Sitemap: https://www.uphousetw.com/sitemap.xml
```

建議 robots：

```txt
User-agent: *
Allow: /

Disallow: /admin/
Disallow: /api/

Sitemap: https://www.uphousetw.com/sitemap.xml
```

## 2. 加上 canonical

正式上線後，每頁都要有 canonical，避免 Zeabur 測試網址與正式網址重複收錄。

首頁：

```html
<link rel="canonical" href="https://www.uphousetw.com/" />
```

八宅頁：

```html
<link rel="canonical" href="https://www.uphousetw.com/projects/eight" />
```

建案列表：

```html
<link rel="canonical" href="https://www.uphousetw.com/projects" />
```

## 3. 決定 Zeabur 網址策略

如果 `uphousetw.zeabur.app` 只是測試站：

- 正式網域上線後，Zeabur 網址應 `noindex` 或 301 redirect 到正式網域。
- 不要讓 Google 同時收錄：
  - `https://uphousetw.zeabur.app/`
  - `https://www.uphousetw.com/`

建議正式策略：

- `www.uphousetw.com`：正式 SEO 網域
- `uphousetw.zeabur.app`：測試 / staging，不進 Google index

## 4. 公開建案頁不要 no-store

八宅頁目前觀察到 cache 類型接近：

```txt
private, no-cache, no-store, max-age=0, must-revalidate
```

公開 SEO 頁建議改成可快取或 ISR：

- 靜態產生建案頁
- 或設定 `revalidate: 3600`
- 不要讓公開建案頁長期 `no-store`

## 5. 補 Open Graph / 社群分享圖

每個建案頁建議有：

- `og:title`
- `og:description`
- `og:image`
- `og:url`
- `twitter:card`

八宅分享時應顯示「八宅」建案圖，而不是泛用 logo。

---

# 第二階段：八宅頁 SEO 強化

## 1. 修改八宅頁 title

目前 title：

```txt
八宅 — 苗栗縣後龍鎮新東路（二張犁段653-1地號） | 建案資訊 | 向上建設
```

問題：地號太長，搜尋者通常不會搜尋完整地號。

建議版本 A：

```txt
八宅｜苗栗後龍 2-3 房電梯華廈｜840萬起｜向上建設
```

建議版本 B：

```txt
八宅｜苗栗高鐵生活圈後龍建案｜2-3房平面車位｜向上建設
```

優先推薦 B，因為可吃：

- 苗栗高鐵生活圈
- 後龍建案
- 2房
- 3房
- 平面車位
- 向上建設

## 2. 修改八宅頁 meta description

建議：

```txt
八宅位於苗栗後龍新東路，鄰近苗栗高鐵站約5分鐘車程，規劃2房、3房電梯華廈，29–50坪、戶戶平面車位，總價840–1,250萬，適合首購、自住與高鐵生活圈通勤族。
```

## 3. 補「適合誰買」區塊

建議新增 H2：

```md
## 八宅適合誰？
```

內容方向：

- 苗栗首購族
- 後龍、竹南、苗栗市自住族
- 苗栗高鐵通勤族
- 竹南科學園區 / 銅鑼園區通勤族
- 想找低戶數、單純社區的人
- 想要雙陽台、對外窗、平面車位的人
- 不想住市中心，但需要高鐵與國道機能的人

## 4. 補「生活圈」區塊

建議新增 H2：

```md
## 苗栗高鐵生活圈與後龍日常機能
```

拆成：

- 高鐵：約 5 分鐘到苗栗高鐵站
- 國道：約 10 分鐘接國道 1 / 3 號
- 市區：約 10 分鐘到後龍市場、苗栗市區
- 產業：約 20 分鐘到竹南大埔、銅鑼科學園區
- 學區：後龍新港雙語國小學區
- 生活：採買、醫療、餐飲、日常補給

## 5. 補 FAQ 區塊

FAQ 對長尾 SEO 很重要。

建議新增 H2：

```md
## 八宅常見問題
```

FAQ 題目：

1. 八宅在哪裡？
2. 八宅離苗栗高鐵站多遠？
3. 八宅總價多少？
4. 八宅有哪些坪數？
5. 八宅是 2 房還是 3 房？
6. 八宅有平面車位嗎？
7. 八宅公設比多少？
8. 八宅什麼時候交屋？
9. 八宅適合首購族嗎？
10. 八宅適合竹南科學園區通勤嗎？

每題回答控制在 60–120 字，語氣要清楚，不要太廣告。

## 6. 補 FAQ schema

八宅頁可加 `FAQPage` structured data，讓 Google 更容易理解頁面內容。

## 7. 補內部連結

八宅頁應內連到：

- `/projects`：建案列表
- `/contact`：預約賞屋
- `/miaoli-hsr-projects`：苗栗高鐵特區建案
- `/houlong-projects`：後龍建案
- `/first-time-buyer-miaoli`：苗栗首購指南
- `/news/...`：相關文章

---

# 第三階段：建立 Local SEO Landing Pages

YouTube 影片的「zipper matrix」重點是：

> 地區 × 需求 × 產品 = 可排名頁面

向上建設不該只靠首頁與建案頁，應建立一批在地搜尋頁。

## 第一批必做頁面

### 1. 苗栗建案頁

URL：

```txt
/miaoli-projects
```

SEO title：

```txt
苗栗建案推薦｜高鐵生活圈與質感住宅｜向上建設
```

內容重點：

- 苗栗買房區域概覽
- 苗栗高鐵生活圈
- 後龍、竹南、頭份比較
- Uphouse 建案導流
- FAQ

### 2. 後龍建案頁

URL：

```txt
/houlong-projects
```

SEO title：

```txt
後龍建案推薦｜苗栗高鐵旁 2-3 房電梯華廈｜向上建設
```

內容重點：

- 後龍生活圈
- 苗栗高鐵站
- 新東路與二張犁生活環境
- 八宅導流
- 首購 / 自住族分析

### 3. 苗栗高鐵特區建案頁

URL：

```txt
/miaoli-hsr-projects
```

SEO title：

```txt
苗栗高鐵特區建案｜高鐵通勤、自住首購住宅選擇｜向上建設
```

內容重點：

- 高鐵通勤優勢
- 國道與園區通勤
- 自住與置產需求
- 八宅 / 未來建案連結

### 4. 竹南建案頁

URL：

```txt
/zhunan-projects
```

SEO title：

```txt
竹南建案推薦｜科學園區通勤與苗栗高鐵生活圈｜向上建設
```

內容重點：

- 竹南科學園區通勤族
- 竹南 vs 後龍 vs 苗栗高鐵生活圈
- 適合族群
- 導到八宅與聯絡頁

### 5. 苗栗首購指南

URL：

```txt
/first-time-buyer-miaoli
```

SEO title：

```txt
苗栗首購族買房指南｜預算、地段、格局與車位怎麼看
```

內容重點：

- 首購預算
- 2房 / 3房選擇
- 平面車位
- 公設比
- 交屋時間
- 交通與生活圈

### 6. 苗栗 2-3 房建案頁

URL：

```txt
/miaoli-2-3-bedroom-homes
```

SEO title：

```txt
苗栗 2房 3房建案推薦｜首購與自住小家庭住宅｜向上建設
```

內容重點：

- 2房適合誰
- 3房適合誰
- 坪數與總價帶
- 八宅 A/B 戶型導流

## 每個 Landing Page 必備結構

```md
# H1：主要關鍵字

## 這個地區 / 需求適合誰？
## 買房前要注意什麼？
## 向上建設目前可了解的建案
## 生活圈 / 交通 / 學區 / 採買
## 常見問題 FAQ
## 預約賞屋 CTA
```

每頁都要：

- 1 個 H1
- 多個 H2
- 800–1,500 字以上
- 內部連結 3–6 個
- CTA：預約賞屋 / 聯絡我們
- FAQ schema
- canonical
- sitemap 收錄

---

# 第四階段：最新消息改成內容 SEO 中心

目前 `/news` 太空，應改成「在地購屋內容中心」，而不是只放公司公告。

## 第一批文章題目

1. 苗栗高鐵特區適合自住嗎？
2. 後龍買房適合哪些族群？
3. 苗栗首購族買房前要注意什麼？
4. 苗栗 2 房與 3 房怎麼選？
5. 苗栗高鐵站周邊生活機能整理
6. 後龍、竹南、頭份買房怎麼選？
7. 苗栗建案看屋 checklist
8. 小戶數社區有什麼優缺點？
9. 電梯華廈 vs 透天，苗栗買房怎麼選？
10. 平面車位為什麼重要？

## 文章頁標準結構

每篇文章應包含：

- SEO title
- meta description
- H1
- 目錄
- 3–6 個 H2
- 在地關鍵字
- 內部連結到八宅 / 建案列表 / 聯絡頁
- FAQ
- Article schema
- 作者 / 更新日期

## 內容語氣

不要寫成 AI 官腔，應該像「在地建商寫給買房者的實用指南」。

原則：

- 少空話
- 多具體地點
- 多決策比較
- 多 FAQ
- 多真實購屋情境

---

# 第五階段：Google Business Profile 閉環

YouTube 影片最重視 Google 商家檔案，因為 Local SEO 不只靠網站，也靠 Google Maps。

## 網站要補的 Google 商家元素

### 1. Footer 加 Google 商家連結

文字：

```txt
在 Google 地圖查看向上建設
```

### 2. 聯絡頁加 Google Maps / 導航

聯絡頁不只要表單，還要有：

- 公司地址
- 電話
- 營業時間
- Google Maps iframe
- Google 商家檔案連結
- LINE / Facebook / Instagram

### 3. 建案頁加導航 CTA

八宅頁可加：

```txt
查看八宅基地位置 / 開啟 Google 地圖導航
```

### 4. Google 商家貼文連回網站

每週 2–3 則 Google 商家貼文，連回：

- 八宅頁
- 建案列表
- 文章頁
- 聯絡頁

貼文主題：

- 八宅基地位置
- 2房 / 3房差異
- 苗栗高鐵生活圈
- 平面車位
- 小戶數社區
- 預約賞屋

---

# 第六階段：評論機制

Local SEO 排名很吃評論數與評論速度。

## 新增回饋頁

URL：

```txt
/feedback
```

表單問題：

1. 這次賞屋 / 洽詢體驗滿意度 1–5 分？
2. 有沒有想補充的地方？
3. 是否願意留下 Google 評論？

## 評論分流邏輯

- 4–5 分：導向 Google 評論連結
- 1–3 分：送到內部客服，不直接導 Google

## 評論目標

- 第一目標：至少 10 則 Google 評論
- 第二目標：每月穩定新增 3–8 則
- 所有評論都要回覆

## 評論回覆範例

```txt
謝謝您的回饋，也很高興八宅的 2-3 房格局、平面車位與苗栗高鐵生活圈位置符合您的需求。向上建設會持續把每個建案當成長期作品來看待。
```

自然帶入：

- 八宅
- 苗栗
- 後龍
- 苗栗高鐵生活圈
- 2房 / 3房
- 平面車位

---

# 第七階段：Schema / 結構化資料

## 首頁 Organization schema 強化

目前已有 Organization，但可補：

- `sameAs`：Facebook、Instagram、Google Maps
- `telephone`
- `email`
- `address`
- `areaServed`：苗栗、後龍、竹南、頭份

## 八宅 RealEstateListing schema 強化

補充：

- `priceRange`
- `floorSize`
- `numberOfRooms`
- `address`
- `geo`
- `image`
- `offers`

## FAQPage schema

所有：

- 建案頁
- Local SEO landing pages
- 購屋指南文章

都應加入 FAQ schema。

## BreadcrumbList schema

每頁加麵包屑：

首頁 > 建案 > 八宅

或：

首頁 > 最新消息 > 苗栗高鐵特區適合自住嗎？

---

# 第八階段：CTA 與轉換率

SEO 帶來流量後，要讓人留下名單。

## 每頁都應有 CTA

CTA 文字建議：

- 預約賞屋
- 了解八宅格局
- 詢問最新銷售資訊
- 取得建案資料
- 加 LINE 洽詢

## 表單欄位建議

不要太長，基本即可：

- 姓名
- 電話
- Email（選填）
- 想了解的建案
- 需求說明

## 建議新增「建案資料索取」CTA

例如：

```txt
索取八宅完整格局與銷售資料
```

這比單純「聯絡我們」更有動機。

---

# 第九階段：照片與真實信任感

影片提到 Google 商家與網站照片會提高信任。

## 應補照片類型

- 基地現況
- 周邊街景
- 苗栗高鐵站距離
- 工程進度
- 建材 / 設備
- 格局圖
- 採光 / 陽台示意
- 接待中心
- 團隊照片
- 施工細節

## 原則

- 少用 stock photo
- 多用真實照片
- 每張圖要有 alt text

Alt 範例：

```txt
八宅苗栗後龍建案基地現況
八宅2房格局示意圖
苗栗高鐵生活圈後龍新東路周邊環境
```

---

# 第十階段：執行順序

## P0：今天就該修

1. 修 `robots.txt` sitemap URL
2. 加 canonical
3. 決定 Zeabur staging 與正式網域策略
4. 八宅頁 title / meta 改成搜尋導向
5. `/news` 至少先放 3 篇文章，不要空頁
6. 八宅頁補 FAQ
7. sitemap 收錄所有有效頁面

## P1：一週內完成

1. 八宅頁補適合族群
2. 八宅頁補生活圈
3. 八宅頁補 FAQ schema
4. 聯絡頁補 Google Maps / Google 商家連結
5. 建立 `/feedback` 評論引導頁
6. 新增 3–5 篇在地文章

## P2：兩週內完成

1. 建立 `/miaoli-projects`
2. 建立 `/houlong-projects`
3. 建立 `/miaoli-hsr-projects`
4. 建立 `/first-time-buyer-miaoli`
5. 建立 `/miaoli-2-3-bedroom-homes`
6. 每頁補 FAQ、內部連結、CTA、schema

## P3：長期固定執行

1. 每週 1–2 篇在地購屋文章
2. 每週 2–3 則 Google 商家貼文
3. 每月穩定新增 Google 評論
4. 每月檢查 Search Console 關鍵字
5. 每月補強已經有曝光但排名不高的頁面

---

# 驗收清單

## 技術 SEO

- [ ] robots.txt sitemap URL 正確
- [ ] 每頁 canonical 正確
- [ ] sitemap 包含所有重要頁面
- [ ] staging 網域不與正式網域重複收錄
- [ ] 建案頁可被 Google 讀取，不是純 CSR
- [ ] 重要頁面不是 no-store
- [ ] 有 Open Graph 圖片

## 頁面 SEO

- [ ] 每頁只有一個 H1
- [ ] title 包含主要關鍵字
- [ ] meta description 有地區、產品、CTA
- [ ] 每頁至少 800 字以上
- [ ] 每頁有 3–6 個內部連結
- [ ] 每頁有 FAQ
- [ ] 每頁有 CTA

## Local SEO

- [ ] Google 商家檔案已最佳化
- [ ] 網站連到 Google Maps / 商家檔案
- [ ] Google 商家貼文固定連回網站
- [ ] 有 `/feedback` 評論引導頁
- [ ] Google 評論至少 10 則
- [ ] 每月穩定新增評論

## 內容 SEO

- [ ] `/news` 不是空頁
- [ ] 至少 10 篇在地購屋文章
- [ ] 文章內連到建案頁與聯絡頁
- [ ] 文章有 Article schema
- [ ] 文章有 FAQ schema

---

# 最後判斷

這個新版站已經有不錯的品牌與資料基礎。接下來真正能提升 Google 流量的，不是再美化首頁，而是把網站改造成：

> 苗栗 / 後龍 / 苗栗高鐵生活圈購屋需求的內容入口 + Google 商家流量接收器。

最先要做的 5 件事：

1. 修 robots / canonical / 正式網域策略
2. 強化八宅頁 title、meta、FAQ、生活圈、適合族群
3. 新增 5 個 Local SEO landing pages
4. 讓 `/news` 變成在地購屋指南
5. 串起 Google 商家檔案與評論機制
