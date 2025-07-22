# test_main_page.py
import allure

@allure.feature("Главная страница")
class TestMainPage:
    @allure.story("Навигация")
    @allure.title("Переход в конструктор")
    def test_navigate_to_constructor(self, authorized_user):
        with allure.step("Кликнуть на ссылку конструктора"):
            authorized_user.navigate_to_constructor()
        
        with allure.step("Проверить активное состояние"):
            assert authorized_user.is_constructor_active()

    @allure.story("Навигация")
    @allure.title("Переход в ленту заказов")
    def test_navigate_to_order_feed(self, authorized_user):
        with allure.step("Кликнуть на ссылку ленты заказов"):
            authorized_user.navigate_to_order_feed()
        
        with allure.step("Проверить отображение ленты"):
            assert authorized_user.is_order_feed_visible()

    @allure.story("Интерактивные элементы")
    @allure.title("Отображение деталей ингредиента")
    def test_ingredient_details_display(self, authorized_user):
        with allure.step("Кликнуть на ингредиент"):
            authorized_user.open_ingredient_details("Булка")
        
        with allure.step("Проверить отображение деталей"):
            assert authorized_user.are_ingredient_details_visible()
