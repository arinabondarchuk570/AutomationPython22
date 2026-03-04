import pytest
from selenium.webdriver.common.by import By
import time

URL = "http://uitestingplayground.com/frames"

@pytest.mark.iframes
def test_iframes(driver):
    driver.get(URL)
    driver.switch_to.frame(driver.find_element(By.ID, 'frame-outer'))
    button = driver.find_element(By.NAME, "my-button")
    button.click()
    time.sleep(2)
    outerframe = driver.find_element(By.ID, "result")
    assert outerframe.text == "Button pressed: Click me"

    driver.switch_to.frame(driver.find_element(By.ID, 'frame-inner'))
    button = driver.find_element(By.CSS_SELECTOR, '[data-action="edit"]')
    button.click()
    time.sleep(2)
    innerframe = driver.find_element(By.ID, 'result')
    assert innerframe.text == "Button pressed: Edit"

    driver.switch_to.default_content()