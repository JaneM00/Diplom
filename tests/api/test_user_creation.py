# test_user_creation.py
import pytest
import allure

@allure.feature("User Registration")
class TestUserCreation:
    @allure.title("Create unique user")
    def test_create_unique_user(self, api, random_user):
        response = api.register_user(random_user)
        assert response.status_code == 200
        assert "accessToken" in response.json()
    
    @allure.title("Create duplicate user")
    def test_create_duplicate_user(self, api, registered_user):
        response = api.register_user(registered_user["user"])
        assert response.status_code == 403
        assert response.json()["message"] == "User already exists"
    
    @allure.title("Create user with missing required field")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_field(self, api, random_user, missing_field):
        user_data = random_user.copy()
        user_data.pop(missing_field)
        response = api.register_user(user_data)
        assert response.status_code == 403
        assert "error" in response.json()
