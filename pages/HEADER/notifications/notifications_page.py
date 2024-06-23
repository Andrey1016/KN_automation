import time

from selenium.common import NoSuchElementException, TimeoutException

from locators.NOTIFICATIONS.notification_locators import Notifications
from locators.HEADER_LOCATORS.header_page_locators import HeaderLocators
from pages.base_page import BasePage


class ClearNotifications(BasePage):
    header_locators = HeaderLocators
    notifications = Notifications

    def clear_notifications(self):
        try:
            self.element_is_visible(self.header_locators.NOTIFICATIONS).click()
            notification = self.element_is_present(self.notifications.ALL_CLEARED)
            is_displayed = notification.is_displayed()
            if is_displayed:
                print("All notifications are already cleared")
                return True
        except NoSuchElementException:
            print("No 'all cleared' notification found, proceeding to clear notifications")
        except TimeoutException:
            print("Timeout waiting for the 'all cleared' notification")

            self.element_is_visible(self.notifications.CLEAR_BUTTON).click()
            self.element_is_visible(self.notifications.CHECKBOX_CLEAR_FLAGS).click()
            self.element_is_visible(self.notifications.CLEAR_BUTTON_MAIN).click()
            time.sleep(3)
            # self.element_is_visible(self.notifications.CLOSE_NOTIF_WINDOW).click()
        try:
            notification = self.element_is_visible(self.notifications.ALL_CLEARED)
            if notification.is_displayed():
                print("All notifications are cleared after attempting to clear them")
                return True
        except NoSuchElementException:
            self.browser.save_screenshot('all_notifications_not_cleared_after_attempt.png')
        # except TimeoutException:
        #     print("Timeout waiting for an element during clearing process")
        # return False

