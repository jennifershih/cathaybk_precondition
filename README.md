# cathaybk_precondition

[![ci](https://github.com/jennifershih/cathaybk_precondition/actions/workflows/ci.yml/badge.svg)](https://github.com/jennifershih/cathaybk_precondition/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Appium](https://img.shields.io/badge/Appium-2-662D91?logo=appium&logoColor=white)

面試前測：兩題程式邏輯與一題 Appium 行動網頁自動化測試（2023）。

## 執行方式

```bash
pip install -e ".[dev,appium]"
python program_logic_1.py   # 德瑞克 33、尚恩 75、傑夫 65、馬基 40，總成績 213
python program_logic_2.py   # 第 10 次落地共 299.609375 公分，第 10 次反彈 0.09765625 公分
pytest                      # 邏輯題的單元測試
```

自動化測試題需要 Appium 2 server 與一台 Android 裝置或模擬器：

```bash
appium &                                  # 預設 http://127.0.0.1:4723
ANDROID_DEVICE="emulator-5554" python automated_test.py
```

截圖會存到 `screenshots/`。官網可能已改版，選擇器失效時需依實際頁面調整。

## 程式邏輯題目一
### 檔案：program_logic_1.py
### 題目：
"有一個老師想要幫學生的期末分數加分，加分規則如下:
如果新分數小於40分，不予加分(保持原分數)。
如果原分數的下一個最接近的5的倍數跟原分數的差在3以下，新分數則為下一個最接近的5的倍數
請利用程式來計算下列4位學生換算後的總成績為何?

德瑞克 33
尚恩 73
傑夫 63
馬基 39"


## 程式邏輯題目二
### 檔案：program_logic_2.py
### 題目：
"德瑞克小朋友在公園溜滑梯的高處將一顆球從100公分的高度自由落下，每次落地後反跳回原高度的一半；然後再落下。

請使用一段程式實做，並算出它在第10次落地時，總共經歷過了多少公分？和第10次的反彈有多高？"


## 自動化測試題目一
### 檔案：automated_test.py
### 題目：
1. 使用Chrome App到[國泰世華銀行官網](https://www.cathaybk.com.tw/cathaybk/)並將畫面截圖。
2. 點選左上角選單，進入 個人金融 > 產品介紹 > 信用卡列表，需計算有幾個項目並將畫面截圖。
3. 個人金融 > 產品介紹 > 信用卡 > 卡片介紹 > 計算頁面上所有(停發)信用卡數量並截圖
