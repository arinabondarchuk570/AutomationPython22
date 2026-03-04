import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

URL = "http://localhost:3000/automation-lab/subscription"

@pytest.mark.parametrize("number, expir_date, cvv", [
    ('378282246310005', '1135','4143'),
])

def test_card_input(number, expir_date, cvv):
    driver.get(URL)
    time.sleep(5)
    card_number_button = driver.find_element(By.CSS_SELECTOR, ".card-input card-number")
    card_number_button.clear()
    card_number_button.send_keys(number)

    card_expir_date = driver.find_element(By.CSS_SELECTOR, ".card-input card-expiry")
    card_expir_date.clear()
    card_expir_date.send_keys(expir_date)

    card_cvv = driver.find_element(By.CSS_SELECTOR, ".card-input card-cvv")
    card_cvv.clear()
    card_cvv.send_keys(cvv)

    button_visibility = driver.find_element(By.CLASS_NAME, 'cvv-toggle')
    button_visibility.click()

    actual_cvv = card_cvv.get_attribute("value")
    assert actual_cvv == cvv

