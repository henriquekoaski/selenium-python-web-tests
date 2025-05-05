from selenium import webdriver
from pages.login_page import LoginPage

def test_login_successful():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com/login")

    login_page = LoginPage(driver)
    login_page.do_login("teste.teste@teste.com", "123456")

    assert login_page.is_user_logged_in()

    driver.quit()
