import pytest
from pages.HEADER.notifications.notifications_page import ClearNotifications

from pages.LOGIN.login_page import LoginPage


def test_clear_notifications(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login()
    notifications = ClearNotifications(browser)
    notifications.clear_notifications()
