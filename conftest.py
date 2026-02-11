import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(scope="session", autouse=False, params=["firefox", "chrome"])
def driver(request):
    if request.param == "firefox":
        opts = FirefoxOptions()
        opts.add_argument("--width=1980")
        opts.add_argument("--height=1600")
        web_driver = webdriver.Firefox(options=opts)

    else:
        opts = Options()
        # opts.add_argument("--headless=new")
        opts.add_argument("--window-size=1980,1600")
        web_driver = webdriver.Chrome(options=opts)

    yield web_driver
    web_driver.quit()


@pytest.fixture(scope="module", autouse=False)
def auto_use():
    print("\n+++Вызвали фикстуру 'auto_use'+++")
    yield {"name": "Alica"}
    print("\n+++Вернулись в фикстуру 'auto_use'+++")