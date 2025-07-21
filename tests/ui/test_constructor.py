# test_constructor.py
import allure
from selenium.webdriver.common.by import By

@allure.feature("Конструктор бургеров")
class TestBurgerConstructor:
    @allure.story("Добавление ингредиентов")
    @allure.title("Проверка счетчика ингредиентов")
    def test_ingredient_counter(self, main_page):
        sauce_locator = (By.XPATH, "//div[contains(text(), 'Соус')]")
        main_page.open_main_page()
        initial_count = main_page.get_element_text(main_page.INGREDIENT_COUNTER) or 0
        main_page.add_ingredient_to_constructor("Соус")
        assert main_page.get_element_text(main_page.INGREDIENT_COUNTER) == initial_count + 1
