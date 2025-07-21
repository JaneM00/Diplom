# main_page.py
from selenium.webdriver.common.action_chains import ActionChains

class MainPage(BasePage):
    # ... существующие локаторы ...
    INGREDIENT_COUNTER = (By.XPATH, "//div[contains(@class, 'Ingredient_counter')]")
    INGREDIENT_DETAILS_NAME = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//h3")

    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient_to_constructor(self, ingredient_locator):
        self.drag_and_drop(ingredient_locator, self.CONSTRUCTOR_AREA)
        return self

    @allure.step("Получить значение счетчика ингредиента")
    def get_ingredient_counter_value(self, ingredient_locator):
        counter = self.find_element(ingredient_locator.find_element(*self.INGREDIENT_COUNTER))
        return int(counter.text) if counter.text else 0

    @allure.step("Получить название ингредиента в модальном окне")
    def get_ingredient_details_name(self):
        return self.find_element(self.INGREDIENT_DETAILS_NAME).text
