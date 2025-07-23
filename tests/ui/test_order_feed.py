# test_order_feed.py
import allure

@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.story("Счетчики заказов")
    @allure.title("Проверка счетчика заказов")
    def test_order_counters(self, main_page, order_feed_page):
        initial_total = order_feed_page.get_total_orders_count()
        main_page.open_main_page().add_ingredient_to_constructor("Соус")
        order_feed_page.open_order_feed()
        assert order_feed_page.get_total_orders_count() > initial_total
