# 輪班對照神器 — GitHub Pages 部署步驟（約 5 分鐘）

這個資料夾已是可直接上線的靜態網站，不需後端，多少人用都沒問題（每個人的班表存在自己的瀏覽器，不會互搶）。

## 上線檔案（同資料夾）
- `index.html`（= shift-app.html，PWA 已內建）
- `manifest.webmanifest`、`sw.js`
- `icon-192.png`、`icon-512.png`、`apple-touch-icon.png`

## 步驟
1. 到 GitHub 新增一個公開 repo（例如 `shift-app`），不要勾 README。
2. 在本資料夾執行：
   ```
   git add index.html manifest.webmanifest sw.js icon-192.png icon-512.png apple-touch-icon.png
   git commit -m "Deploy shift app to GitHub Pages"
   git branch -M main
   git remote add origin https://github.com/<你的帳號>/shift-app.git
   git push -u origin main
   ```
   （若 `shift-app.html` 後續有改，改完再 `Copy-Item shift-app.html index.html` 蓋過去後重新 commit/push。）
3. 到 repo 的 Settings → Pages → Source 選 `main` / `root`，存檔。
4. 等 1-2 分鐘，網址就是 `https://<你的帳號>.github.io/shift-app/`，傳給大家用。

## 手機安裝成 App
- Android（Chrome）：開網址 → 選單 →「安裝應用程式」或「加到主畫面」。頁面也有「📲 安裝App」按鈕。
- iPhone（Safari）：分享 →「加入主畫面」。之後可離線開（Service Worker 已快取）。

## 注意
- 部署後是公開網址，任何拿到連結的人都能用；但每個人的班表只存在自己的裝置，不會外洩。
- 若要公司內部限定，改放公司內網主機即可，同樣把上面 6 個檔丟上去就行。
