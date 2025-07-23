# login_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .urls import Urls
import allure

class LoginPage(BasePage):
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")

    @allure.step("Открыть страницу логина")
    def open_login_page(self):
        return self.open(Urls.LOGIN)

    @allure.step("Ввести email")
    def enter_email(self, email: str):
        self.find_element(self.EMAIL_INPUT).send_keys(email)
        return self

    @allure.step("Ввести пароль")
    def enter_password(self, password: str):
        self.find_element(self.PASSWORD_INPUT).send_keys(password)
        return self
