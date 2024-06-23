from pages.LOGIN.login_page import LoginPage


class TestElements:
    class TestLoginPage:

        def test_login_with_correct_credentials(self, browser):
            login_page = LoginPage(browser)
            login_page.open()
            login_page.login()




