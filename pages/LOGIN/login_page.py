import time
from selenium.common import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

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
        time.sleep(1.5)
        self.continue_login_notice()
        self.delete_pop_up_message()

    def handle_login_notice_button(self, button_locator, button_name):
        try:
            button = self.element_is_visible(button_locator)
            if button:
                button.click()
                print(f"{button_name} clicked.")
            else:
                print(f"{button_name} not found. Proceeding without clicking.")
        except NoSuchElementException:
            print(f"{button_name} not present. Proceeding with the next steps.")
        except TimeoutException:
            print(f"{button_name} found but not clickable. Proceeding with the next steps.")

    def delete_pop_up_message(self):
        self.handle_login_notice_button(self.locators.DELETE_MESSAGE_CLICK, "Login notice delete button")

    def continue_login_notice(self):
        self.handle_login_notice_button(self.locators.CLICK_CONTINUE_LOGIN_NOTICE, "Continue login notice button")

# Add your next steps here
