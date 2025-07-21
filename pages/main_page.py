# main_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .urls import Urls
import allure

class MainPage(BasePage):
    CONSTRUCTOR_LINK = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link') and contains(text(), 'Конструктор')]")
    ORDER_FEED_LINK = (By.LINK_TEXT, "Лента заказов")
    INGREDIENT_ITEM = (By.XPATH, "//div[contains(@class, 'Ingredient_ingredient')][1]")
    INGREDIENT_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_close')]")
    CONSTRUCTOR_AREA = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    INGREDIENT_COUNTER = (By.XPATH, "//div[contains(@class, 'Ingredient_counter')]")
    INGREDIENT_DETAILS = (By.XPATH, "//div[contains(@class, 'IngredientDetails_details')]")

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        return self.open(Urls.BASE)

    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient_to_constructor(self, ingredient_type: str):
        ingredient_locator = (By.XPATH, f"//div[contains(text(), '{ingredient_type}')]")
        self.drag_and_drop(ingredient_locator, self.CONSTRUCTOR_AREA)
        return self
