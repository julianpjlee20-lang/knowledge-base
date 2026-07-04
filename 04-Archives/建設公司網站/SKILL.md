# Premium Web Design — UI/UX Best Practices

針對高端品牌網站（建設、房地產、奢侈品）的設計原則。

## 適用場景

- 建設公司 / 房地產
- 奢侈品牌
- 高單價服務（遊艇、豪車、精品酒店）
- 需要傳達「質感」的品牌官網

---

## 🎯 核心設計原則

### 1. 沉浸式視覺 (Immersive Visuals)

```
✅ DO:
- Hero Section 佔滿首屏 (100vh)
- 高品質攝影（專業拍攝，非素材庫）
- 影片背景（靜音、循環）
- 視差滾動 (Parallax) 增加深度

❌ DON'T:
- 低解析度圖片
- 過度壓縮
- 過多輪播（1-3張即可）
```

### 2. 極簡配色 (Minimal Color Palette)

```
推薦組合：
- 主色：黑 #1a1a1a 或 深灰 #2d2d2d
- 背景：白 #ffffff 或 米白 #f8f8f8
- 強調：金 #c9a962 / 品牌色（僅用於 CTA）

規則：
- 最多 3 色
- 圖片是主角，色彩是配角
- CTA 用對比色跳出
```

### 3. 字體層次 (Typography Hierarchy)

```
中文推薦：
- 標題：Noto Serif TC / 思源宋體
- 內文：Noto Sans TC / 思源黑體

英文推薦：
- 標題：Playfair Display / Cormorant
- 內文：Inter / Source Sans Pro

層次規則：
- H1: 48-72px, 粗體
- H2: 32-40px
- Body: 16-18px, 行高 1.6-1.8
- 字距適度加寬（中文 0.05em）
```

### 4. 動態微互動 (Subtle Animations)

```css
/* Scroll 進場動畫 */
.fade-in {
  opacity: 0;
  transform: translateY(30px);
  transition: all 0.8s ease-out;
}
.fade-in.visible {
  opacity: 1;
  transform: translateY(0);
}

/* Hover 狀態 */
.card:hover {
  transform: scale(1.02);
  box-shadow: 0 20px 40px rgba(0,0,0,0.1);
}

/* 圖片 Hover */
.img-container:hover img {
  transform: scale(1.05);
}
```

**原則：**
- 動畫時長 0.3s - 0.8s
- Ease-out 或 Cubic-bezier
- 目的是引導，非炫技

### 5. 留白與呼吸 (Whitespace)

```
Section 間距：
- Desktop: 120px - 200px
- Mobile: 60px - 100px

元素間距：
- 卡片間：24px - 40px
- 段落間：1.5em - 2em

規則：
- 寧可太空，不要太擠
- 奢侈品 = 空間 = 從容
```

### 6. 故事性敘事 (Storytelling)

```
結構建議：
1. Hero: 品牌精神一句話
2. 價值主張: 為什麼選我們（3點）
3. 作品展示: 精選案例（大圖）
4. 品牌故事: 歷史/理念
5. 社會證明: 合作夥伴/獎項
6. CTA: 聯絡/預約

文案原則：
- 少即是多
- 動詞優於名詞
- 情感連結優於功能列表
```

### 7. 導航與 CTA (Navigation)

```
導航：
- 最多 6 個主選單項
- Logo 左上，CTA 右上
- Mobile: 漢堡選單，全螢幕展開

浮動 CTA：
- 固定右下角或底部
- 「聯絡我們」或「預約諮詢」
- 不遮擋重要內容
```

---

## 📐 頁面結構範本

### 首頁

```
┌─────────────────────────────────┐
│  LOGO          NAV        CTA  │
├─────────────────────────────────┤
│                                 │
│     [全幅 Hero 影片/圖片]       │
│                                 │
│      品牌標語（一句話）          │
│         ↓ Scroll               │
├─────────────────────────────────┤
│                                 │
│   精選作品 (3張大圖卡片)        │
│                                 │
├─────────────────────────────────┤
│                                 │
│   關於我們 (左圖右文)           │
│                                 │
├─────────────────────────────────┤
│                                 │
│   服務項目 (圖標 + 簡述)        │
│                                 │
├─────────────────────────────────┤
│                                 │
│   最新消息 (3則)               │
│                                 │
├─────────────────────────────────┤
│                                 │
│   CTA Banner                   │
│                                 │
├─────────────────────────────────┤
│  Footer: 聯絡 | 社群 | 版權    │
└─────────────────────────────────┘
```

---

## 🛠️ 技術實作建議

### 框架
- **Next.js 14+** (App Router)
- **Tailwind CSS** (快速響應式)
- **Framer Motion** (動畫)

### 圖片優化
```jsx
// Next.js Image 自動優化
import Image from 'next/image'

<Image
  src="/hero.jpg"
  alt="Building"
  fill
  priority
  className="object-cover"
/>
```

### 動畫庫
```jsx
// Framer Motion 進場動畫
import { motion } from 'framer-motion'

<motion.div
  initial={{ opacity: 0, y: 30 }}
  whileInView={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.8 }}
>
  內容
</motion.div>
```

### 字體載入
```jsx
// next/font 自動優化
import { Noto_Serif_TC, Inter } from 'next/font/google'

const serif = Noto_Serif_TC({ 
  subsets: ['latin'],
  weight: ['400', '700']
})
```

---

## 📚 參考網站

| 網站 | 特色 |
|------|------|
| [Vista Properties](https://vistaprops.com) | 微動態、清晰篩選 |
| [聯聚建設](https://greatbuilding.com.tw) | 品牌哲學、中文排版 |
| [HELM.yt](https://helm.yt) | 奢華感、沉浸式 |

---

## ✅ Checklist

開發前確認：

- [ ] Hero 圖片/影片已準備（高解析度）
- [ ] 品牌色已定義
- [ ] 字體已選定
- [ ] 文案已完成
- [ ] 響應式斷點規劃

設計檢查：

- [ ] 留白足夠
- [ ] 字體層次分明
- [ ] 動畫流暢不卡
- [ ] CTA 明顯可見
- [ ] Mobile 體驗良好

---
*Created: 2026-01-31*

#ai-tools #ai-seo #seo 