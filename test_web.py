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