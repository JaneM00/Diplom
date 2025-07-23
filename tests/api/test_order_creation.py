# test_order_creation.py
import allure
import pytest
from .urls import URLs

@allure.feature("Создание заказа")
class TestOrderCreation:
    @allure.story("Авторизованный пользователь")
    @allure.title("Создание заказа с авторизацией")
    def test_create_order_authorized(self, registered_user, valid_ingredients):
        api = APIHelper()
        
        with allure.step("Отправка запроса на создание заказа"):
            response = api.create_order(
                ingredients=valid_ingredients[:2],
                token=registered_user["token"]
            )
        
        with allure.step("Проверка ответа"):
            assert response.status_code == 200
            assert "order" in response.json()
            assert response.json()["order"]["number"] is not None

    @allure.story("Неавторизованный пользователь")
    @allure.title("Создание заказа без авторизации")
    def test_create_order_unauthorized(self, valid_ingredients):
        api = APIHelper()
        
        with allure.step("Отправка запроса без токена"):
            response = api.create_order(ingredients=valid_ingredients[:2])
        
        with allure.step("Проверка ответа"):
            assert response.status_code == 200
            assert "order" in response.json()

    @allure.story("Валидация данных")
    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_empty_ingredients(self, registered_user):
        api = APIHelper()
        
        with allure.step("Отправка запроса с пустым списком ингредиентов"):
            response = api.create_order(
                ingredients=[],
                token=registered_user["token"]
            )
        
        with allure.step("Проверка ошибки"):
            assert response.status_code == 400
            assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.story("Валидация данных")
    @allure.title("Создание заказа с невалидными ингредиентами")
    def test_create_order_invalid_ingredients(self, registered_user):
        api = APIHelper()
        
        with allure.step("Отправка запроса с неверными хешами ингредиентов"):
            response = api.create_order(
                ingredients=["invalid_hash_1", "invalid_hash_2"],
                token=registered_user["token"]
            )
        
        with allure.step("Проверка ошибки сервера"):
            assert response.status_code == 500
