# test_constructor.py
import allure
import pytest

@allure.feature("Конструктор бургеров")
class TestBurgerConstructor:
    @allure.story("Добавление ингредиентов")
    @allure.title("Проверка счетчика ингредиентов")
    def test_ingredient_counter_increases(self, authorized_user):
        """Тест проверяет увеличение счетчика при добавлении ингредиента"""
        with allure.step("Добавить соус в конструктор"):
            initial_count = authorized_user.get_ingredient_counter("Соус")
            authorized_user.add_ingredient_to_constructor("Соус")
        
        with allure.step("Проверить увеличение счетчика"):
            assert authorized_user.get_ingredient_counter("Соус") == initial_count + 1

    @allure.story("Модальное окно")
    @allure.title("Закрытие модального окна с деталями ингредиента")
    def test_close_ingredient_modal(self, authorized_user):
        """Тест проверяет закрытие модального окна"""
        with allure.step("Открыть детали ингредиента"):
            authorized_user.open_ingredient_details("Соус")
        
        with allure.step("Закрыть модальное окно"):
            authorized_user.close_ingredient_modal()
        
        with allure.step("Проверить что окно закрыто"):
            assert not authorized_user.is_ingredient_modal_visible()
