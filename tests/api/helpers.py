# helpers.py
import requests
import allure
from .urls import URLs

class APIHelper:
    @allure.step("POST {url}")
    def _post(self, url, json=None, headers=None):
        return requests.post(url, json=json, headers=headers)

    @allure.step("DELETE {url}")
    def _delete(self, url, headers=None):
        return requests.delete(url, headers=headers)

    @allure.step("GET {url}")
    def _get(self, url):
        return requests.get(url)

    @allure.step("Регистрация пользователя")
    def register_user(self, user_data):
        return self._post(URLs.REGISTER, json=user_data)

    @allure.step("Авторизация пользователя")
    def login_user(self, credentials):
        return self._post(URLs.LOGIN, json=credentials)

    @allure.step("Удаление пользователя")
    def delete_user(self, token):
        return self._delete(URLs.USER, headers={"Authorization": token})

    @allure.step("Создание заказа")
    def create_order(self, ingredients, token=None):
        headers = {"Authorization": token} if token else {}
        return self._post(URLs.ORDERS, json={"ingredients": ingredients}, headers=headers)

    @allure.step("Получение списка ингредиентов")
    def get_ingredients(self):
        return self._get(URLs.INGREDIENTS)
