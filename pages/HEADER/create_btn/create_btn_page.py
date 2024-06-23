from locators.HEADER_LOCATORS.header_page_locators import HeaderLocators
from locators.HEADER_LOCATORS.header_page_locators import CreateBtnItemsDropdown
from pages.base_page import BasePage


class ClickCreateBtn(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.header_locators = HeaderLocators()
        self.create_btn_locators = CreateBtnItemsDropdown()

    def click_create_btn(self):
        self.element_is_visible(self.header_locators.HEADER_CREATE_BTN).click()

    def item_advanced_auto_test(self):
        self.element_is_visible(self.create_btn_locators.ITEM_ADVANCED_AUTO_TEST).click()

    def process_each_item(self):
        items = self.element_is_present(self.create_btn_locators.ALL_ITEMS_CREATE).click()
        for item in items:
            item.click()
