# data.py
from faker import Faker

fake = Faker()

class TestData:
    @staticmethod
    @allure.step("Генерация тестовых данных пользователя")
    def generate_user():
        return {
            "email": fake.email(),
            "password": fake.password(length=10),
            "name": fake.first_name()
        }

    @staticmethod
    def invalid_ingredients():
        return ["invalid_hash_1", "invalid_hash_2"]

    @staticmethod
    def incomplete_user_data():
        return [
            {"password": "password123", "name": "Test User"},  # Без email
            {"email": "test@example.com", "name": "Test User"},  # Без пароля
            {"email": "test@example.com", "password": "password123"}  # Без имени
        ]
