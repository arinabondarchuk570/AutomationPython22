import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

URL = "http://localhost:3000/automation-lab/subscription"

@pytest.mark.parametrize("invalid_promocode", [
    "",
    " ",
    "!@#@$",
    "abcde",
    "12345",
    "Abc",
])
def test_invalid_promocode(driver, invalid_promocode):
    driver.get(URL)
    time.sleep(5)
    promocode_input = driver.find_element(By.XPATH, "//*[@data-testid='promo-input']")
    promocode_input.clear()
    promocode_input.send_keys(invalid_promocode)

    apply_button = driver.find_element(By.XPATH, "//*[@data-testid='promo-apply-btn']")
    apply_button.click()

    error_message = driver.find_element(By.XPATH, "//*[@data-testid='promo-message']")
    assert error_message.is_displayed()