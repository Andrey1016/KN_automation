# from lib2to3.pgen2 import driver
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        # self.driver = driver
        self.browser = browser

    def find(self, args):
        return self.browser.find_element(*args)

    def element_is_visible(self, locator, timeout=3):
        return wait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=3):
        return wait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=3):
        return wait(self.browser, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=3):
        return wait(self.browser, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=3):
        return wait(self.browser, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.browser, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView;", element)

    def elements_are_present2(self, locator, timeout=3):
        # """ Return a list of elements if present, or an empty list if not. """
        try:
            return wait(self.browser, timeout).until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            return []

    # __________________________Assert________________________________

    def url_is_match_to_first_login(self, timeout=5, expected_ulr='https://test2.kainexus.com/#b'):
        return wait(self.browser, timeout).until(EC.url_matches(expected_ulr))
