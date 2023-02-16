import pytest
from selenium import webdriver
from selenium.webdriver import FirefoxOptions

@pytest.fixture(scope="function")
def firefox_browser_instance(request):
    """
    Provide a selenium webdriver instance
    """
    options = FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("windows-size=800x600")
    options.add_argument("disable-gpu")
    browser = webdriver.Firefox(options=options)
    yield browser
    browser.close()
