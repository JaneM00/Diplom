from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.nomoreparties.site/"
    
    def open(self):
        self.driver.get(self.base_url)
    
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

class MainPage(BasePage):
    CONSTRUCTOR_LINK = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link') and contains(text(), 'Конструктор')]")
    ORDER_FEED_LINK = (By.LINK_TEXT, "Лента заказов")
    INGREDIENT_ITEM = (By.XPATH, "//div[contains(@class, 'Ingredient_ingredient')][1]")
    INGREDIENT_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_close')]")
    CONSTRUCTOR_AREA = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    INGREDIENT_COUNTER = (By.XPATH, "//div[contains(@class, 'Ingredient_counter')]")

    def click_constructor_link(self):
        self.wait_for_element(self.CONSTRUCTOR_LINK).click()
    
    def click_order_feed_link(self):
        self.wait_for_element(self.ORDER_FEED_LINK).click()
    
    def click_first_ingredient(self):
        self.wait_for_element(self.INGREDIENT_ITEM).click()
    
    def is_ingredient_modal_visible(self):
        try:
            return self.wait_for_element(self.INGREDIENT_MODAL).is_displayed()
        except:
            return False
    
    def close_ingredient_modal(self):
        self.wait_for_element(self.MODAL_CLOSE_BUTTON).click()
    
    def drag_ingredient_to_constructor(self):
        ingredient = self.wait_for_element(self.INGREDIENT_ITEM)
        constructor = self.wait_for_element(self.CONSTRUCTOR_AREA)
        
        ActionChains(self.driver).drag_and_drop(ingredient, constructor).perform()
    
    def click_order_button(self):
        self.wait_for_element(self.ORDER_BUTTON).click()
    
    def get_ingredient_counter(self):
        try:
            counter = self.wait_for_element(self.INGREDIENT_COUNTER)
            return int(counter.text)
        except:
            return 0
    
    def get_constructor_link(self):
        return self.wait_for_element(self.CONSTRUCTOR_LINK)


class LoginPage(BasePage):
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")

    def open(self):
        self.driver.get(self.base_url + "login")
    
    def login(self, email, password):
        self.wait_for_element(self.EMAIL_INPUT).send_keys(email)
        self.wait_for_element(self.PASSWORD_INPUT).send_keys(password)
        self.wait_for_element(self.LOGIN_BUTTON).click()


class OrderFeedPage(BasePage):
    ORDER_FEED_SECTION = (By.XPATH, "//section[contains(@class, 'OrderFeed')]")
    TOTAL_ORDERS = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    TODAY_ORDERS = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")

    def open(self):
        self.driver.get(self.base_url + "feed")
    
    def is_order_feed_visible(self):
        try:
            return self.wait_for_element(self.ORDER_FEED_SECTION).is_displayed()
        except:
            return False
    
    def get_total_orders_count(self):
        return int(self.wait_for_element(self.TOTAL_ORDERS).text)
    
    def get_today_orders_count(self):
        return int(self.wait_for_element(self.TODAY_ORDERS).text)
