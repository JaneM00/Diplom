# test_user_login.py
import pytest
import allure
@allure.feature("User Login")
class TestUserLogin:
    @allure.title("Login with valid credentials")
    def test_login_valid_user(self, api, registered_user):
        response = api.login_user({
            "email": registered_user["user"]["email"],
            "password": registered_user["user"]["password"]
        })
        assert response.status_code == 200
        assert "accessToken" in response.json()
    
    @allure.title("Login with invalid credentials")
    def test_login_invalid_credentials(self, api, registered_user):
        response = api.login_user({
            "email": registered_user["user"]["email"],
            "password": "wrong_password"
        })
        assert response.status_code == 401
        assert response.json()["message"] == "email or password are incorrect"
