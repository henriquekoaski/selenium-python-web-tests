from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Login')]")
    LOGGED_USER_NAME = (By.XPATH, "//i[@class='fa fa-user']/following-sibling::b")

    def do_login(self, email, password):
        self.write(*self.EMAIL_INPUT, text=email)
        self.write(*self.PASSWORD_INPUT, text=password)
        self.click(*self.LOGIN_BUTTON)

    def is_user_logged_in(self):
        return self.is_element_visible(*self.LOGGED_USER_NAME)
