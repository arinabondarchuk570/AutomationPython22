import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

URL = "http://localhost:3000/automation-lab/subscription"

@pytest.mark.parametrize("period, tariff", [
    ('[data-testid="period-1"]', '[data-testid="tariff-basic"]'),
    ('[data-testid="period-1"]', '[data-testid="tariff-premium"]'),
    ('[data-testid="period-1"]', '[data-testid="tariff-family"]'),
    ('[data-testid="period-3"]', '[data-testid="tariff-basic"]'),
    ('[data-testid="period-3"]', '[data-testid="tariff-premium"]'),
    ('[data-testid="period-3"]', '[data-testid="tariff-family"]'),
    ('[data-testid="period-12"]', '[data-testid="tariff-basic"]'),
    ('[data-testid="period-12"]', '[data-testid="tariff-premium"]'),
    ('[data-testid="period-12"]', '[data-testid="tariff-family"]'),
])

def test_price_period(driver, period, tariff):
    driver.get(URL)
    time.sleep(5)
    period_button = driver.find_element(By.CSS_SELECTOR, period)
    period_button.click()

    tariff_button = driver.find_element(By.CSS_SELECTOR, tariff)
    tariff_button.click()

    assert "active" in period_button.get_attribute("class")
    assert "selected" in tariff_button.get_attribute("class")