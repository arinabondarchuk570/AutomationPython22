import time
import pytest
from selenium.webdriver.common.by import By

URL = "http://uitestingplayground.com/textinput"

@pytest.mark.textinput
def test_textinput(driver):
    driver.get(URL)
    time.sleep(5)
    input = driver.find_element(By.CSS_SELECTOR, ".form-control")
    input.click()
    input.send_keys("happy wednesday <3")

@pytest.mark.cleartext
def test_clear_text(driver):
    driver.get(URL)
    time.sleep(5)
    input = driver.find_element(By.CSS_SELECTOR, ".form-control")
    input.send_keys("happy wednesday <3")
    input.clear()
