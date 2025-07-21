# test_order_creation.py
import pytest
import allure

@allure.feature("Order Creation")
class TestOrderCreation:
    @allure.title("Create order with authorization")
    def test_create_order_authorized(self, api, registered_user, valid_ingredients):
        response = api.create_order(valid_ingredients, registered_user["token"])
        assert response.status_code == 200
        assert "order" in response.json()
    
    @allure.title("Create order without authorization")
    def test_create_order_unauthorized(self, api, valid_ingredients):
        response = api.create_order(valid_ingredients)
        assert response.status_code == 200
        assert "order" in response.json()
    
    @allure.title("Create order without ingredients")
    def test_create_order_empty_ingredients(self, api, registered_user):
        response = api.create_order([], registered_user["token"])
        assert response.status_code == 400
        assert response.json()["message"] == "Ingredient ids must be provided"
    
    @allure.title("Create order with invalid ingredients")
    def test_create_order_invalid_ingredients(self, api, registered_user, invalid_ingredients):
        response = api.create_order(invalid_ingredients, registered_user["token"])
        assert response.status_code == 500
