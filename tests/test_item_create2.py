from pages.LOGIN.login_page import LoginPage
import pytest

from pages.utility2_page import CreateAllItems


class TestCreateAdvancedItem:

    @pytest.mark.test
    def test_create_new_items(self, browser):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.login()

        create_item = CreateAllItems(browser)
        create_item.create_item()

    def test_create_active_items(self, browser):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.login()

        create_item = CreateAllItems(browser)
        create_item.create_item_active_status()

    def test_create_deferred_items(self, browser):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.login()

        create_item = CreateAllItems(browser)
        create_item.create_item_deferred_status()


