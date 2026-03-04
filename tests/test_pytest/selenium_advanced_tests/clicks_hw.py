import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

URL = 'http://uitestingplayground.com/click'

@pytest.mark.usualclick
def test_usual_click(driver):
    driver.get(URL)
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()

@pytest.mark.jsclick
def test_js_click(driver):
    driver.get(URL)
    time.sleep(5)
    buttonelement = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    driver.execute_script("arguments[0].click();", buttonelement)

@pytest.mark.actionchainsclick
def test_actionchains_click(driver):
    driver.get(URL)
    time.sleep(5)
    buttonelement = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
    actions = ActionChains(driver)
    actions.click(buttonelement).perform()

@pytest.mark.keysclick
def test_keys_click(driver):
    driver.get(URL)
    time.sleep(5)
    buttonelement = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    buttonelement.click()
    buttonelement.send_keys(Keys.ENTER)