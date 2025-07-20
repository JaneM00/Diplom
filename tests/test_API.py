# test_API.py
import pytest
import requests
import allure
from urllib.parse import urljoin

BASE_URL = "https://stellarburgers.nomoreparties.site/api/"
USER_DATA = {
    "email": "test_user@example.com",
    "password": "password123",
    "name": "Test User"
}


@allure.feature("API Tests for Stellar Burgers")
class TestStellarBurgersAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.session = requests.Session()
        yield
        self.session.close()

    @allure.story("User Registration")
    @allure.title("Register unique user")
    def test_register_unique_user(self):
        unique_email = f"user_{pytest.time.time()}@example.com"
        payload = {
            "email": unique_email,
            "password": "password123",
            "name": "Unique User"
        }
        
        with allure.step("Send registration request"):
            response = self.session.post(
                urljoin(BASE_URL, "auth/register"),
                json=payload
            )
        
        with allure.step("Check response"):
            assert response.status_code == 200
            assert "accessToken" in response.json()
            
        with allure.step("Cleanup - delete user"):
            token = response.json()["accessToken"]
            self.session.delete(
                urljoin(BASE_URL, "auth/user"),
                headers={"Authorization": token}
            )

    @allure.story("User Registration")
    @allure.title("Register duplicate user")
    def test_register_duplicate_user(self):
        with allure.step("First registration"):
            response = self.session.post(
                urljoin(BASE_URL, "auth/register"),
                json=USER_DATA
            )
            assert response.status_code == 200
            
        with allure.step("Second registration attempt"):
            response = self.session.post(
                urljoin(BASE_URL, "auth/register"),
                json=USER_DATA
            )
            assert response.status_code == 403
            assert response.json()["message"] == "User already exists"
            
        with allure.step("Cleanup - delete user"):
            token = response.json().get("accessToken")
            if token:
                self.session.delete(
                    urljoin(BASE_URL, "auth/user"),
                    headers={"Authorization": token}
                )

    @allure.story("User Login")
    @allure.title("Login with valid credentials")
    def test_login_valid_user(self):
        with allure.step("Register test user"):
            reg_response = self.session.post(
                urljoin(BASE_URL, "auth/register"),
                json=USER_DATA
            )
            assert reg_response.status_code == 200
            
        with allure.step("Login with test user"):
            login_response = self.session.post(
                urljoin(BASE_URL, "auth/login"),
                json={
                    "email": USER_DATA["email"],
                    "password": USER_DATA["password"]
                }
            )
            assert login_response.status_code == 200
            assert "accessToken" in login_response.json()
            
        with allure.step("Cleanup - delete user"):
            token = login_response.json()["accessToken"]
            self.session.delete(
                urljoin(BASE_URL, "auth/user"),
                headers={"Authorization": token}
            )

    @allure.story("Order Creation")
    @allure.title("Create order with authorization")
    def test_create_order_authorized(self):
        with allure.step("Register and login user"):
            reg_response = self.session.post(
                urljoin(BASE_URL, "auth/register"),
                json=USER_DATA
)
            token = reg_response.json()["accessToken"]
            
        with allure.step("Get ingredients"):
            ingredients_response = self.session.get(
                urljoin(BASE_URL, "ingredients")
            )
            assert ingredients_response.status_code == 200
            ingredients = ingredients_response.json()["data"]
            valid_ingredient = ingredients[0]["_id"]
            
        with allure.step("Create order"):
            order_response = self.session.post(
                urljoin(BASE_URL, "orders"),
                headers={"Authorization": token},
                json={"ingredients": [valid_ingredient]}
            )
            assert order_response.status_code == 200
            assert "order" in order_response.json()
            
        with allure.step("Cleanup - delete user"):
            self.session.delete(
                urljoin(BASE_URL, "auth/user"),
                headers={"Authorization": token}
            )
