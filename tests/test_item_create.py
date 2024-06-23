import time

from pages.HEADER.create_btn.create_btn_page import ClickCreateBtn
from pages.ITEM_CRETE_WINDOW.item_create_window_page import ItemCreate
from pages.LOGIN.login_page import LoginPage
import pytest

from pages.utility2_page import CreateAllItems


class TestCreateAdvancedItem:

    @pytest.mark.test
    def test_create_new_items(self, browser):
        # Instantiate the login page
        login_page = LoginPage(browser)
        login_page.open()
        login_page.login()

        create_item = CreateAllItems(browser)
        create_item.create_item()

    def test_create_active_items(self, browser):
        # Instantiate the login page
        login_page = LoginPage(browser)
        login_page.open()
        login_page.login()

        create_item = CreateAllItems(browser)
        create_item.create_item_active_status()

        # click_create_btn = ClickCreateBtn(browser)
        # click_create_btn.click_create_btn()
        # click_create_btn.item_advanced_auto_test()
        #
        # item_create = ItemCreate(browser)
        # item_create.add_item_title()
        # item_create.add_all_attributes4()
        #
        # # item_create.add_all_text_area()
        # # item_create.add_all_text_fields()
        # # item_create.add_all_number_fields()
        # item_create.click_create()
        # item_create.success_window_item_link()
        # time.sleep(10)
