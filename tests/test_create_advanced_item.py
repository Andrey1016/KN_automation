import time

from pages.LOGIN.login_page import LoginPage
import pytest

from pages.create_advanced_item_page import CreateAdvancedItem


@pytest.fixture(autouse=True)
def login(browser):
    # Instantiate the login page
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login()


def test_create_items(browser):
    create_item = CreateAdvancedItem(browser)
    create_item.fill_author()
    time.sleep(4)
