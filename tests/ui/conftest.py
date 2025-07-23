# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    """Фикстура для инициализации драйвера с поддержкой мультибраузерности"""
    if request.param == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    
    yield driver
    driver.quit()

@pytest.fixture
def authorized_user(driver):
    """Фикстура для авторизации пользователя (сложная логика предусловия)"""
    from pages.login_page import LoginPage
    from pages.main_page import MainPage
    
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    
    # Выполняем авторизацию
    login_page.open()
    login_page.login("test@example.com", "password123")
    
    yield main_page
