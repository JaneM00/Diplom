# conftest.py
import pytest
import allure
from .helpers import APIHelper
from .data import TestData

@pytest.fixture
def api():
    return APIHelper()

@pytest.fixture
def random_user():
    return TestData.random_user()

@pytest.fixture
def registered_user(api, random_user):
    # Создание пользователя
    response = api.register_user(random_user)
    assert response.status_code == 200
    token = response.json()["accessToken"]
    
    yield {"user": random_user, "token": token}
    
    # Удаление пользователя после теста
    with allure.step("Cleanup: delete test user"):
        api.delete_user(token)

@pytest.fixture
def valid_ingredients():
    return TestData.valid_ingredients()

@pytest.fixture
def invalid_ingredients():
    return TestData.invalid_ingredients()
