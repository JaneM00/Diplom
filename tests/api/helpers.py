# helpers.py
import requests
from .urls import URLs

class APIHelper:
    @staticmethod
    def register_user(user_data):
        return requests.post(URLs.REGISTER, json=user_data)
    
    @staticmethod
    def login_user(credentials):
        return requests.post(URLs.LOGIN, json=credentials)
    
    @staticmethod
    def delete_user(token):
        return requests.delete(URLs.USER, headers={"Authorization": token})
    
    @staticmethod
    def create_order(ingredients, token=None):
        headers = {"Authorization": token} if token else {}
        return requests.post(URLs.ORDERS, json={"ingredients": ingredients}, headers=headers)
    
    @staticmethod
    def get_ingredients():
        return requests.get(URLs.INGREDIENTS)
