from selenium.webdriver.common.by import By


class Notifications:
    NOTIFICATIONS_CLICK = (By.XPATH, "//span[contains(@class,'fas far fa-bell')]")
    CLEAR_BUTTON = (By.XPATH, "//a[contains(@class,'-toolbar-medium')]")
    CLEAR_BUTTON_MAIN = (By.XPATH, "//span[contains(@class,'-large')and text()='Clear']")
    CHECKBOX_CLEAR_FLAGS = (By.XPATH, "//label[text()='Also, clear all ']")
    NOTIF_CLEARED = (By.XPATH, "//div[text()=\"You're all caught up.\"]")
    CLOSE_NOTIF_WINDOW = (By.CSS_SELECTOR, " a.x-btn.app-item-window-close-button")
    ALL_CLEARED = (By.XPATH, "//div[text()=\"You're all caught up.\"]")
