import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    chrome_browser = webdriver.Chrome()
    # chrome_browser.implicitly_wait(3)
    chrome_browser.explicitly_wait(3)
    chrome_browser.maximize_window()
    yield chrome_browser
    chrome_browser.quit()




