"""自動化測試題目一：用 Appium 在 Android Chrome 開啟國泰世華銀行官網並截圖。

1. 開啟官網並截圖。
2. 左上角選單 → 個人金融 → 產品介紹 → 信用卡列表，計算項目數量並截圖。
3. 個人金融 → 產品介紹 → 信用卡 → 卡片介紹，計算「停發」信用卡數量並截圖。

需要：Appium 2 server（uiautomator2 driver）、一台連接的 Android 裝置或模擬器。
網站版面可能已改版；選擇器若失效，請以實際頁面重新確認。
"""

from __future__ import annotations

import os
from pathlib import Path

from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

HOME_URL = "https://www.cathaybk.com.tw/cathaybk/"
APPIUM_URL = os.environ.get("APPIUM_URL", "http://127.0.0.1:4723")
SCREENSHOTS = Path(os.environ.get("SCREENSHOT_DIR", "screenshots"))


def create_driver() -> WebDriver:
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.browser_name = "Chrome"
    options.device_name = os.environ.get("ANDROID_DEVICE", "Android Emulator")
    return webdriver.Remote(APPIUM_URL, options=options)


def click(driver: WebDriver, by: str, value: str, timeout: int = 15) -> None:
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value))).click()


def screenshot(driver: WebDriver, name: str) -> Path:
    SCREENSHOTS.mkdir(exist_ok=True)
    path = SCREENSHOTS / f"{name}.png"
    driver.save_screenshot(str(path))
    return path


def run() -> tuple[int, int]:
    driver = create_driver()
    wait = WebDriverWait(driver, 15)
    try:
        # 1. Home page
        driver.get(HOME_URL)
        wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        screenshot(driver, "1-home")

        # 2. Credit card list
        click(driver, By.CSS_SELECTOR, ".header-menu-btn")
        click(driver, By.LINK_TEXT, "個人金融")
        click(driver, By.LINK_TEXT, "產品介紹")
        click(driver, By.LINK_TEXT, "信用卡")
        items = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".cards-list-item"))
        )
        card_count = len(items)
        screenshot(driver, "2-credit-card-list")

        # 3. Discontinued cards on the card introduction page
        click(driver, By.LINK_TEXT, "卡片介紹")
        discontinued = driver.find_elements(By.XPATH, "//*[contains(text(), '停發')]")
        discontinued_count = len(discontinued)
        screenshot(driver, "3-discontinued-cards")

        return card_count, discontinued_count
    finally:
        driver.quit()


if __name__ == "__main__":
    cards, discontinued = run()
    print(f"信用卡列表項目數：{cards}")
    print(f"停發信用卡數量：{discontinued}")
