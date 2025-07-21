# test_main_page.py
import allure

@allure.feature("Главная страница")
class TestMainPage:
    @allure.story("Навигация")
    @allure.title("Переход в конструктор")
    def test_constructor_navigation(self, main_page):
        main_page.open_main_page()
        main_page.click(main_page.CONSTRUCTOR_LINK)
        assert "current" in main_page.get_element_attribute(main_page.CONSTRUCTOR_LINK, "class")

    @allure.story("Модальное окно")
    @allure.title("Просмотр деталей ингредиента")
    def test_ingredient_details(self, main_page):
        main_page.open_main_page()
        main_page.click(main_page.INGREDIENT_ITEM)
        assert main_page.is_element_visible(main_page.INGREDIENT_DETAILS)
