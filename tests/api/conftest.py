# conftest.py
import pytest
import allure
from faker import Faker
from .helpers import APIHelper
from .data import TestData

fake = Faker()

@pytest.fixture
def registered_user():
    """Фикстура создает и удаляет тестового пользователя"""
    api = APIHelper()
    user_data = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.first_name()
    }
    
    # Создание пользователя (предусловие)
    with allure.step("Регистрация тестового пользователя"):
        response = api.register_user(user_data)
        assert response.status_code == 200
        token = response.json()["accessToken"]
    
    yield {"user": user_data, "token": token}
    
    # Удаление пользователя (постусловие)
    with allure.step("Удаление тестового пользователя"):
        api.delete_user(token)

@pytest.fixture
def valid_ingredients():
    """Фикстура получает валидные ингредиенты из API"""
    api = APIHelper()
    with allure.step("Получение списка ингредиентов"):
        response = api.get_ingredients()
        assert response.status_code == 200
        return [ingredient["_id"] for ingredient in response.json()["data"]]
