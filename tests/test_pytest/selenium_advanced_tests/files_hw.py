import pytest
from selenium.webdriver.common.by import By
import urllib.request

URL = "https://demoqa.com/upload-download"

@pytest.mark.fileupload
def test_fileupload(driver):
    driver.get(URL)
    file_element = driver.find_element(By.CSS_SELECTOR, "input[type=file]")
    file_path = " D:/progi4/kitties.txt"
    file_element.send_keys(file_path)

@pytest.mark.filedownload
def test_downloadfile(driver):
    driver.get(URL)
    link = driver.find_element(By.ID, "downloadButton")
    file_url = link.get_attribute("href")
    response = urllib.request.urlopen(file_url)

    file = open("document.pdf", 'wb')
    file.write(response.read())
    file.close()
