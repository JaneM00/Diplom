# base_page.py
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import allure

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу {url}")
    def open(self, url: str):
        self.driver.get(url)
        return self

    @allure.step("Найти элемент {locator}")
    def find_element(self, locator: tuple):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Кликнуть по элементу {locator}")
    def click(self, locator: tuple):
        self.find_element(locator).click()
        return self
