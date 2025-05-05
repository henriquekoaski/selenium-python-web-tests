from selenium import webdriver
from pages.signup_page import SignupPage

def test_signup_successful():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com/login")

    login_page = SignupPage(driver)
    login_page.do_signup("henrique", "teste.teste@teste.com")

    driver.quit()