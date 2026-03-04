import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

URL = "http://localhost:3000/automation-lab/subscription"

def test_valid_promocode(driver):
    driver.get(URL)
    time.sleep(5)
    promocode_input = driver.find_element(By.XPATH, "//*[@data-testid='promo-input']")
    promocode_input.clear()
    promocode_input.send_keys("ALWAYS")

    apply_button = driver.find_element(By.XPATH, "//*[@data-testid='promo-apply-btn']")
    apply_button.click()

    message = driver.find_element(By.XPATH, "//*[@data-testid='promo-message']")
    actual_message = message.text
    print(f"Получено сообщение: {actual_message}")
    assert message.is_displayed()