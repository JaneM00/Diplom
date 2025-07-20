import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import MainPage, LoginPage, OrderFeedPage


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("UI Tests for Stellar Burgers")
class TestStellarBurgersUI:
    @allure.story("Main Page Navigation")
    @allure.title("Navigate to Constructor")
    def test_navigate_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_constructor_link()
        
        with allure.step("Verify constructor is active"):
            assert "current" in main_page.get_constructor_link().get_attribute("class")

    @allure.story("Main Page Navigation")
    @allure.title("Navigate to Order Feed")
    def test_navigate_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_feed_link()
        
        order_feed_page = OrderFeedPage(driver)
        with allure.step("Verify order feed is displayed"):
            assert order_feed_page.is_order_feed_visible()

    @allure.story("Ingredient Details")
    @allure.title("Open ingredient details modal")
    def test_open_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_first_ingredient()
        
        with allure.step("Verify modal is displayed"):
            assert main_page.is_ingredient_modal_visible()

    @allure.story("Ingredient Details")
    @allure.title("Close ingredient details modal")
    def test_close_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_first_ingredient()
        main_page.close_ingredient_modal()
        
        with allure.step("Verify modal is closed"):
            assert not main_page.is_ingredient_modal_visible()

    @allure.story("Order Creation")
    @allure.title("Add ingredient to order")
    def test_add_ingredient_to_order(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        
        initial_counter = main_page.get_ingredient_counter()
        main_page.drag_ingredient_to_constructor()
        
        with allure.step("Verify counter increased"):
            assert main_page.get_ingredient_counter() == initial_counter + 1


@allure.feature("Order Feed Tests")
class TestOrderFeed:
    @pytest.fixture
    def create_order(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("test_user@example.com", "password123")
        
        main_page = MainPage(driver)
        main_page.drag_ingredient_to_constructor()
        main_page.click_order_button()
        
        yield
        
        # Cleanup if needed

    @allure.story("Order Feed Updates")
    @allure.title("Check total orders counter")
    def test_total_orders_counter(self, driver, create_order):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open()
        
        initial_total = order_feed_page.get_total_orders_count()
        create_order
        driver.refresh()
        
        with allure.step("Verify total counter increased"):
            assert order_feed_page.get_total_orders_count() > initial_total

    @allure.story("Order Feed Updates")
    @allure.title("Check today orders counter")
    def test_today_orders_counter(self, driver, create_order):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open()
        
        initial_today = order_feed_page.get_today_orders_count()
        create_order
        driver.refresh()
        
        with allure.step("Verify today counter increased"):
            assert order_feed_page.get_today_orders_count() > initial_today
