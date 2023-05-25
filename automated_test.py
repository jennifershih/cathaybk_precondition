from appium import webdriver
from selenium.webdriver.common.by import By

# Appium連線設定
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'your_device_name',
    'browserName': 'Chrome'
}

# Appium建立連線
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 前往國泰世華銀行官網
driver.get('https://www.cathaybk.com.tw/cathaybk/')

# 等待網頁載入完成
driver.implicitly_wait(10)

# 截圖1: 國泰世華銀行官網
driver.save_screenshot('screenshot1.png')

# 點選左上角選單
menu_button = driver.find_element(By.CSS_SELECTOR, '.header-menu-btn')
menu_button.click()

# 點選個人金融
personal_finance = driver.find_element(By.LINK_TEXT, '個人金融')
personal_finance.click()

# 點選產品介紹
product_introduction = driver.find_element(By.LINK_TEXT, '產品介紹')
product_introduction.click()

# 點選信用卡
credit_card_list = driver.find_element(By.LINK_TEXT, '信用卡')
credit_card_list.click()

# 計算項目數量
items = driver.find_elements(By.CSS_SELECTOR, '.cards-list-item')
item_count = len(items)

# 截圖2: 信用卡列表
driver.save_screenshot('screenshot2.png')

# 點選第一個信用卡
first_credit_card = driver.find_element(By.CSS_SELECTOR, '.cards-list-item')
first_credit_card.click()

# 進入卡片介紹
card_introduction = driver.find_element(By.LINK_TEXT, '卡片介紹')
card_introduction.click()

# 計算(停發)信用卡數量
discontinued_cards = driver.find_elements(By.XPATH, "//span[contains(text(), '(停發)')]")
discontinued_card_count = len(discontinued_cards)

# 截圖3: (停發)信用卡計算頁面
driver.save_screenshot('screenshot3.png')

# 關閉連線
driver.quit()
