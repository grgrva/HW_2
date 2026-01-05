import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    opts = Options()

    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=opts)
    yield driver

    driver.quit()


url_google = 'https://www.google.com/'
url_github = 'https://github.com/'


def test_selenium_google(driver):
    driver.get(url_google)
    assert driver.title == "Google"
    assert driver.current_url == url_google


def test_selenium_github(driver):
    driver.get(url_github)
    assert "GitHub" in driver.title
    assert driver.current_url == url_github