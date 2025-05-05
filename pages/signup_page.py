from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time 

class SignupPage(BasePage):
    
    NAME_INPUT = (By.NAME, "name")
    EMAIL_IMPUT = (By.CSS_SELECTOR, '[data-qa="signup-email"]')
    SIGNUP_BUTTON = (By.XPATH, "//button[contains(text(),'Signup')]")


    def do_signup(self, name, email):
        self.write(*self.NAME_INPUT, text=name)
        self.write(*self.EMAIL_IMPUT, text=email)
        time.sleep(10)
        self.click(*self.SIGNUP_BUTTON)
    