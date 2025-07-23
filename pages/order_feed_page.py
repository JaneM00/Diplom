# order_feed_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .urls import Urls
import allure
class OrderFeedPage(BasePage):
    ORDER_FEED_SECTION = (By.XPATH, "//section[contains(@class, 'OrderFeed')]")
    TOTAL_ORDERS = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    TODAY_ORDERS = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_in_progress')]//li")

    @allure.step("Открыть ленту заказов")
    def open_order_feed(self):
        return self.open(Urls.FEED)

    @allure.step("Получить количество заказов за все время")
    def get_total_orders_count(self):
        return int(self.get_text(self.TOTAL_ORDERS))
