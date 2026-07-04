---
created: 2025-01-22T21:00:00
title: "PRD：LINE → OneDrive 自動歸檔服務"
tags: [automation, line, nodejs, onedrive, prd, web-development, webhook]
---

# PRD：LINE → OneDrive 自動歸檔服務

> 版本：1.0  
> 建立日期：2025-01-22  
> 狀態：規劃中

---

## 1. 產品概述

### 1.1 產品名稱
LINE to OneDrive Auto Archive Service

### 1.2 一句話描述
當使用者傳送檔案到 LINE 官方帳號時，系統自動將檔案下載並歸檔至 OneDrive，並回覆歸檔結果與檔案連結。

### 1.3 目標用戶
- 需要快速將手機檔案備份到雲端的使用者
- 希望透過 LINE 簡化檔案管理流程的工作者

### 1.4 解決的問題
| 現有痛點 | 解決方案 |
|---------|---------|
| 手動下載 LINE 檔案再上傳到雲端，步驟繁瑣 | 傳到 LINE 即自動歸檔 |
| 檔案散落在不同裝置，難以管理 | 統一歸檔到 OneDrive |
| 忘記備份重要檔案 | 自動化處理，不需記憶 |

---

## 2. 功能需求

### 2.1 核心功能

#### F1：接收 LINE 檔案
| 項目 | 規格 |
|------|------|
| 觸發方式 | 使用者傳送檔案到 LINE 官方帳號 |
| 支援類型 | 圖片、影片、音訊、文件（所有 LINE 支援的檔案類型） |
| 檔案大小 | 依 LINE 平台限制（圖片 10MB / 影片 200MB） |

#### F2：上傳至 OneDrive
| 項目 | 規格 |
|------|------|
| 目標位置 | `/LINE歸檔/` 資料夾 |
| 分類方式 | 不分類，全部放同一資料夾 |
| 檔名規則 | `{原始檔名}_{timestamp}.{副檔名}` |
| 重複處理 | 自動重新命名，不覆蓋 |

#### F3：回覆通知
| 項目 | 規格 |
|------|------|
| 成功回覆 | ✅ 已歸檔：{檔名}<br>📁 {OneDrive 連結} |
| 失敗回覆 | ❌ 歸檔失敗：{錯誤原因} |
| 回覆位置 | 同一個 LINE 聊天室 |

### 2.2 功能流程圖

```
┌─────────────────────────────────────────────────────────────┐
│                        使用者                                │
└─────────────────────────────────────────────────────────────┘
                              │
                              │ 1. 傳送檔案
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    LINE 官方帳號                             │
└─────────────────────────────────────────────────────────────┘
                              │
                              │ 2. Webhook 事件
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Webhook Server                            │
│                    (Railway)                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  a. 驗證簽章                                         │   │
│  │  b. 解析訊息類型                                     │   │
│  │  c. 下載檔案內容                                     │   │
│  │  d. 上傳到 OneDrive                                  │   │
│  │  e. 取得分享連結                                     │   │
│  │  f. 回覆 LINE 訊息                                   │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              │
                    ┌─────────┴─────────┐
                    │                   │
                    ▼                   ▼
┌─────────────────────────┐  ┌─────────────────────────┐
│      OneDrive           │  │      LINE 回覆          │
│   (Microsoft 365)       │  │                         │
│                         │  │  ✅ 已歸檔：照片.jpg    │
│  📁 LINE歸檔/           │  │  📁 https://...         │
│     └── 照片.jpg        │  │                         │
└─────────────────────────┘  └─────────────────────────┘
```

---

## 3. 技術規格

### 3.1 系統架構

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│    LINE     │────▶│   Railway   │────▶│  OneDrive   │
│  Platform   │◀────│   Server    │     │ (Graph API) │
└─────────────┘     └─────────────┘     └─────────────┘
                           │
                           │ 驗證
                           ▼
                    ┌─────────────┐
                    │  Azure AD   │
                    │ (Entra ID)  │
                    └─────────────┘
```

### 3.2 技術選型

| 層級 | 技術 | 說明 |
|------|------|------|
| 執行環境 | Node.js 20+ | LINE SDK 官方支援 |
| Web 框架 | Express.js | 輕量、成熟 |
| LINE SDK | @line/bot-sdk | 官方 SDK |
| Microsoft API | @microsoft/microsoft-graph-client | 官方 SDK |
| 身份驗證 | @azure/msal-node | OAuth 2.0 |
| 部署平台 | Railway | 免費方案、自動部署 |

### 3.3 環境變數

```env
# LINE 設定
LINE_CHANNEL_ACCESS_TOKEN=    # LINE Channel Access Token
LINE_CHANNEL_SECRET=          # LINE Channel Secret

# Azure AD 設定
AZURE_CLIENT_ID=              # 應用程式（用戶端）識別碼
AZURE_CLIENT_SECRET=          # 用戶端密碼
AZURE_TENANT_ID=              # 目錄（租用戶）識別碼

# OneDrive 設定
ONEDRIVE_FOLDER_PATH=/LINE歸檔   # 歸檔資料夾路徑

# 伺服器設定
PORT=3000                     # 伺服器埠號
```

### 3.4 API 端點

| 方法 | 路徑 | 說明 |
|------|------|------|
| POST | `/webhook` | LINE Webhook 接收端點 |
| GET | `/health` | 健康檢查（保持服務不休眠） |

---

## 4. 第三方服務設定

### 4.1 LINE 官方帳號

| 項目 | 說明 |
|------|------|
| 帳號類型 | LINE Official Account（免費） |
| 必要功能 | Messaging API |
| 取得資訊 | Channel ID, Channel Secret, Channel Access Token |
| Webhook URL | `https://{railway-app}.railway.app/webhook` |

### 4.2 Azure AD（Microsoft Entra ID）

| 項目 | 說明 |
|------|------|
| 應用程式類型 | Web 應用程式 |
| 驗證流程 | Client Credentials（應用程式權限） |
| 必要權限 | `Files.ReadWrite.All`（應用程式權限） |
| 取得資訊 | Client ID, Client Secret, Tenant ID |

### 4.3 Railway

| 項目 | 說明 |
|------|------|
| 方案 | Starter（免費） |
| 限制 | 500 小時/月執行時間 |
| 部署方式 | GitHub 自動部署 |

---

## 5. 資料流程

### 5.1 檔案處理流程

```
1. LINE Webhook 觸發
   └── 事件類型：message
       └── 訊息類型：image / video / audio / file

2. 驗證請求
   └── 檢查 X-Line-Signature 簽章

3. 下載檔案
   └── GET https://api-data.line.me/v2/bot/message/{messageId}/content
   └── 回傳：Binary data + Content-Type

4. 準備上傳
   └── 產生檔名：{原始檔名}_{timestamp}.{ext}
   └── 檢查資料夾存在

5. 上傳到 OneDrive
   └── 小檔案（< 4MB）：PUT /drive/items/{parent-id}:/{filename}:/content
   └── 大檔案（≥ 4MB）：Upload Session

6. 取得分享連結
   └── POST /drive/items/{item-id}/createLink

7. 回覆 LINE
   └── POST https://api.line.me/v2/bot/message/reply
```

### 5.2 錯誤處理

| 錯誤情境 | 處理方式 |
|---------|---------|
| LINE 簽章驗證失敗 | 返回 401，不處理 |
| 檔案下載失敗 | 回覆用戶「下載失敗，請重試」 |
| OneDrive 上傳失敗 | 回覆用戶「上傳失敗」+ 錯誤原因 |
| Token 過期 | 自動重新取得 Token |

---

## 6. 安全性考量

### 6.1 驗證機制

- [x] LINE Webhook 簽章驗證（X-Line-Signature）
- [x] Azure AD OAuth 2.0 Client Credentials
- [x] 環境變數儲存敏感資訊（不寫死在程式碼）

### 6.2 權限最小化

- [x] OneDrive 僅授權 `Files.ReadWrite.All`，不授權其他權限
- [x] LINE Bot 僅需要 Messaging API，不需要其他功能

### 6.3 資料處理

- [x] 檔案僅在記憶體中暫存，不寫入伺服器磁碟
- [x] 處理完成後立即釋放記憶體
- [x] 不記錄檔案內容，僅記錄 metadata（檔名、大小、時間）

---

## 7. 監控與維運

### 7.1 日誌記錄

```javascript
// 記錄格式
{
  timestamp: "2025-01-22T10:30:00Z",
  event: "file_archived",
  userId: "U1234567890",      // LINE User ID（雜湊處理）
  fileType: "image",
  fileSize: 1024000,
  fileName: "photo.jpg",
  status: "success",
  duration: 2500              // 處理時間（ms）
}
```

### 7.2 健康檢查

- 端點：`GET /health`
- 用途：外部服務定時呼叫，避免 Railway 免費方案休眠
- 建議：使用 UptimeRobot（免費）每 5 分鐘 ping 一次

### 7.3 告警機制

| 情境 | 通知方式 |
|------|---------|
| 服務異常 | UptimeRobot Email 通知 |
| 連續失敗 | LINE 回覆用戶錯誤訊息 |

---

## 8. 實作計畫

### 8.1 里程碑

| 階段 | 項目 | 預估時間 |
|------|------|---------|
| **Step 1** | 建立 LINE 官方帳號 + Messaging API | 15 分鐘 |
| **Step 2** | 設定 Azure AD 應用程式 | 15 分鐘 |
| **Step 3** | 開發 Webhook Server | 30 分鐘 |
| **Step 4** | 部署到 Railway | 10 分鐘 |
| **Step 5** | 設定 LINE Webhook URL + 測試 | 10 分鐘 |
| **總計** | | **約 1.5 小時** |

### 8.2 專案結構

```
line-onedrive-archive/
├── src/
│   ├── index.js              # 進入點
│   ├── config.js             # 環境變數設定
│   ├── line/
│   │   ├── webhook.js        # Webhook 處理
│   │   ├── client.js         # LINE API Client
│   │   └── validator.js      # 簽章驗證
│   ├── onedrive/
│   │   ├── auth.js           # Azure AD 驗證
│   │   ├── client.js         # Graph API Client
│   │   └── upload.js         # 檔案上傳
│   └── utils/
│       ├── logger.js         # 日誌
│       └── filename.js       # 檔名處理
├── .env.example              # 環境變數範本
├── package.json
├── railway.json              # Railway 部署設定
├── PRD.md                    # 本文件
└── README.md                 # 使用說明
```

---

## 9. 未來擴充（Phase 2）

以下功能不在 MVP 範圍，未來可考慮：

| 功能 | 說明 |
|------|------|
| 📁 自訂分類規則 | 按檔案類型、日期自動分類 |
| 🏷️ 自動標籤 | 用 AI 辨識圖片內容並加標籤 |
| 🔍 搜尋功能 | 在 LINE 中搜尋已歸檔的檔案 |
| 📊 統計報表 | 每週/每月歸檔統計 |
| 👥 多用戶支援 | 不同用戶歸檔到不同資料夾 |
| ☁️ 多雲端支援 | 支援 Google Drive、Dropbox |

---

## 10. 附錄

### A. LINE 檔案類型對照

| LINE 訊息類型 | Content-Type | 預設副檔名 |
|--------------|--------------|-----------|
| image | image/jpeg | .jpg |
| image | image/png | .png |
| video | video/mp4 | .mp4 |
| audio | audio/m4a | .m4a |
| file | 依檔案而定 | 原始副檔名 |

### B. Microsoft Graph API 參考

- [OneDrive API 文件](https://docs.microsoft.com/graph/api/resources/onedrive)
- [上傳大檔案](https://docs.microsoft.com/graph/api/driveitem-createuploadsession)
- [建立分享連結](https://docs.microsoft.com/graph/api/driveitem-createlink)

### C. LINE Messaging API 參考

- [Webhook Events](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)
- [Get Content](https://developers.line.biz/en/reference/messaging-api/#get-content)
- [Reply Message](https://developers.line.biz/en/reference/messaging-api/#send-reply-message)

---

## 變更記錄

| 版本 | 日期 | 變更內容 |
|------|------|---------|
| 1.0 | 2025-01-22 | 初版建立 |
