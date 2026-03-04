import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "http://uitestingplayground.com/alerts"

@pytest.mark.simplealert
def test_simple_alert(driver):
    driver.get(URL)
    button = driver.find_element(By.ID, 'alertButton')
    button.click()

    simplealert = driver.switch_to.alert
    print(simplealert.text)
    assert simplealert.text == 'Today is a working day.\nOr less likely a holiday.'
    simplealert.accept()

@pytest.mark.confirmalert
def test_confirm_alert(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 5)
    button = driver.find_element(By.ID, 'confirmButton')
    button.click()

    confirmalert = driver.switch_to.alert
    confirmalert.accept()
    wait.until(EC.alert_is_present())
    secondalert = driver.switch_to.alert
    assert secondalert.text == 'Yes'
    secondalert.accept()

    button.click()
    confirmalert = driver.switch_to.alert
    confirmalert.dismiss()
    wait.until(EC.alert_is_present())
    secondalert = driver.switch_to.alert
    assert secondalert.text == 'No'
    secondalert.accept()

@pytest.mark.promptalert
def test_prompt_alert(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 5)
    button = driver.find_element(By.ID, 'promptButton')
    button.click()

    promptalert = driver.switch_to.alert
    promptalert.send_keys("cats")
    promptalert.accept()
    wait.until(EC.alert_is_present())
    secondalert = driver.switch_to.alert
    assert secondalert.text == "User value: cats"

    button = driver.find_element(By.ID, 'promptButton')
    button.click()
    promptalert = driver.switch_to.alert
    promptalert.send_keys("dogs")
    promptalert.accept()
    wait.until(EC.alert_is_present())
    secondalert = driver.switch_to.alert
    assert secondalert.text == "User value: dogs"
