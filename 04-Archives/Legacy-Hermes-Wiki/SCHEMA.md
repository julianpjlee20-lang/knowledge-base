---
title: LLM Wiki Schema
description: 知識庫結構定義與頁面規範
version: 1.0
created: 2026-05-29
updated: 2026-05-30
---

# LLM Wiki Schema

## 資料夾結構

```
wiki/
├── index.md           # Wiki 首頁（所有頁面索引）
├── log.md             # 變更記錄
├── SCHEMA.md          # 本檔案（結構定義）
├── README.md          # 說明文件
│
├── concepts/          # 概念頁面（-概念.md）
├── entities/          # 實體頁面（-實體.md）
├── comparisons/       # 比較分析頁面（-比較.md）
├── queries/           # 查詢結果存檔
├── raw/               # 原始資料（截圖、PDF 等）
└── archives/          # 已封存頁面
```

## 頁面 Frontmatter

```yaml
---
title: 頁面標題
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: concept | entity | comparison | query | raw
tags: [tag1, tag2]
sources: [url1, url2]
---
```

## 命名規範

- 檔案名稱使用 kebab-case：`machine-learning-intro.md`
- 內部連結使用雙括號：`[[machine-learning-intro]]`
- 避免空白和特殊字元

## 同步狀態

- ✅ 2026-05-30 重新初始化完成
- 同步目標：GitHub + Obsidian 雙向同步