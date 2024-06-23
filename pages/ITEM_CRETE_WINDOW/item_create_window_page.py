from locators.ITEM_CREATE_WINDOW_LOCATORS.item_create_window_locators import ItemCreateWindow
from pages.base_page import BasePage


class ItemCreate(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.locators = ItemCreateWindow()

    def add_item_title(self):
        self.element_is_visible(self.locators.ITEM_TITLE).send_keys("Advanced AutoTest")

    def add_all_text_area(self):
        text_area_elements = self.elements_are_present(self.locators.TEXT_AREA)
        for element in text_area_elements:
            element.send_keys("Text Area")

    def add_all_text_fields(self):
        text_area_elements = self.elements_are_present(self.locators.TEXT_FIELDS)
        for element in text_area_elements:
            element.send_keys("Text Fields")

    def add_all_number_fields(self):
        number_field_elements = self.elements_are_present(self.locators.NUMBER_FIELDS)
        for element in number_field_elements:
            element.send_keys(12343)

    def click_create(self):
        self.element_is_visible(self.locators.CREATE_ITEM_BTN).click()

    def close_success_window(self):
        self.element_is_visible(self.locators.SUCCESS_WINDOW_CLOSE).click()

    def success_window_item_link(self):
        self.element_is_visible(self.locators.SUCCESS_WINDOW_ITEM_LINK).click()
