# FTX 自動放貸腳本

## 前言

> 還沒有 FTX 會員的大大們，歡迎透過下的邀請連結進行註冊。<br>
> 邀請連結: https://ftx.com/#a=6410127

<br>

## 該專案在做什麼事情？

該專案是透過 Python 腳本，每小時自動執行 FTX 交易所的貸款功能。

FTX 交易所的貸款每小時將會返回貸款利率，也就是說貸款金額越高返回金額越多，因此透過 FTX 每小時返回的機制，重新取得最大貸款金額，每小時重新進行最大額度貸款。

<br>

## 如何執行該腳本

- ### 複製該專案

  `$ git clone https://github.com/da8865892q/ftx-auto-lending.git`

- ### 安裝所需項目

  Python 3：[官網安裝連結](https://www.python.org/downloads/) (此專案執行 Python 版本為 V 3.9.2)
  Requests: `$ sudo easy_install -U requests`

- ### 設定相關參數

  1. 登入 FTX 平台 (還沒有 FTX 會員的大大們，可點擊該 [邀請連結](https://ftx.com/#a=6410127))
  2. 帳戶 icon → Settings(下拉選單) → Api(側邊欄)
  3. 新增並取得 API Key 與 API Secret
  4. 分別填入該專案的 `ftx.py` 的 `API_KEY` 與 `API_SECRET`
  5. 最後將想要執行貸款的幣種，填入 `currencys` 的陣列中
     (e.g. `currencys = ["BTC", "USDT", "ETH"]`)

- ### 執行該腳本

  透過 command line 即可在本地端執行該腳本

  1. 進入該專案料夾： `$ cd ftx-auto-lending`
  2. 使用 Python 3 執行腳本： `python3 ftx.py`

<br>

## 相關文件

- FTX - REST API: https://docs.ftx.com/#get-lending-info
