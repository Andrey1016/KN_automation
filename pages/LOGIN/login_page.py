import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from generator.generator import correct_credentials
from locators.LOGIN_LOCATORS.login_page_locators import LoginPageLocators

from pages.base_page import BasePage

CLICK_CONTINUE_LOGIN_NOTICE = (By.XPATH, "//span[contains(@class,'x-') and text()='Continue']")
DELETE_MESSAGE_CLICK = (By.XPATH, "//span[contains(@class,'x-') and text()='Delete']")


class LoginPage(BasePage):
    locators = LoginPageLocators()

    def __init__(self, browser):
        super().__init__(browser)
        self.header_locators = None

    def open(self):
        self.browser.get('https://test2.kainexus.com')

    def login(self):
        login_info = next(correct_credentials())
        login_name = login_info.login_name
        password = login_info.password
        self.element_is_visible(self.locators.USERNAME).send_keys(login_name)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SIGN_IN_BTN).click()
        # self.continue_login_notice()
        # self.delete_pop_up_message()

        # assert self.url_is_match_to_first_login()

    # ----------- You were in the process of submitting an Item.---------------
    # def delete_pop_up_message(self):
    #     try:
    #         self.element_is_clickable(DELETE_MESSAGE_CLICK).click()
    #     except NoSuchElementException:
    #         pass

    def delete_pop_up_message(self, max_attempts=3, retry_delay=1):
        attempts = 0
        while attempts < max_attempts:
            try:
                delete_button = self.element_is_clickable(DELETE_MESSAGE_CLICK)
                if delete_button.is_displayed():
                    delete_button.click()
            except NoSuchElementException:
                pass
            time.sleep(retry_delay)
            attempts += 1

    def continue_login_notice(self, max_attempts=3, retry_delay=1):
        attempts = 0
        while attempts < max_attempts:
            try:
                continue_button = self.element_is_clickable(CLICK_CONTINUE_LOGIN_NOTICE)
                if continue_button.is_displayed():
                    continue_button.click()
            except NoSuchElementException:
                pass
            time.sleep(retry_delay)
            attempts += 1
