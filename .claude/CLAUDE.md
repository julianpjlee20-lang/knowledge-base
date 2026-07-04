# Claude Context — 向上集團

## 公司結構
你服務三個關聯公司：
- **向上建設**（Uphouse Construction）— 建設開發
- **安上建設**（Anshang Construction）— 建設開發
- **鹽館前投資**（Yanguanqian Investment）— 投資控股

主要業務區域：苗栗後龍、新竹/苗栗高鐵廊帶

## 每次 Session 開始
1. 讀取 `04-Archives/Agent Logs/claude/index.md` 了解知識庫現況
2. 如有相關 project，讀取對應的 concepts 文章

## 每次 Session 結束
1. 將重要決策、教訓、架構變更摘要寫入：
   `04-Archives/Agent Logs/claude/daily-logs/YYYY-MM-DD.md`
2. 執行 git commit + push

## 重要規則
- 會計科目遵循台灣財政部標準
- Excel 重要分頁靠左，草稿/假設頁靠右
- 所有正式文件使用繁體中文
- 公司間轉帳需做跨公司消除

## Skills 位置
- bank-entry: /mnt/skills/user/bank-entry/
- ib-office: /mnt/skills/user/ib-office/
- construction: /mnt/skills/user/construction/
- invoice-to-remittance: /mnt/skills/user/invoice-to-remittance/
- audit: /mnt/skills/user/audit/
- second-brain: /mnt/skills/user/second-brain/
- ocr-vision: /mnt/skills/user/ocr-vision/

## 知識庫位置
- 入口：`04-Archives/Agent Logs/claude/index.md`
- 對話記錄：`04-Archives/Agent Logs/claude/daily-logs/`
- 知識文章：`04-Archives/Agent Logs/claude/concepts/`
