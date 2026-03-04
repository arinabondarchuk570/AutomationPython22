import pytest
from selenium.webdriver.common.by import By
import time

URL = "https://the-internet.herokuapp.com/windows"

@pytest.mark.windows
def test_windows(driver):
    driver.get(URL)

    driver.find_element(By.LINK_TEXT, 'Click here').click()
    time.sleep(5)
    allhandles = driver.window_handles
    newhandle = allhandles[-1]

    driver.switch_to.window(newhandle)
    time.sleep(5)
    newelement = driver.find_element(By.CSS_SELECTOR, '.example')
    assert newelement.text == "New window"