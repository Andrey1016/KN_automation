from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    SIGN_IN_BTN = (By.ID, 'signInBtn')
    NEED_HELP = (By.XPATH, '//a[@class="need-help"]')
    PAGE_TEXT = (By.XPATH, '//span[text()="First time signing in?"]')
    CLICK_CONTINUE_LOGIN_NOTICE = (By.XPATH, "//span[contains(@class,'x-') and text()='Continue']")
    DISMISS_MESSAGE_CLICK = (By.XPATH, "//a[contains(@class,'x-') and text()='Dismiss Message']")
    DELETE_MESSAGE_CLICK = (By.XPATH, "//span[contains(@class,'x-') and text()='Delete']")
    # WRONG_CREDENTIALS = (By.XPATH, '//span[text()= Invalid username or password.]')






