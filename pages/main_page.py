# main_page.py
def navigate_to_constructor(self):
    self.click(self.CONSTRUCTOR_LINK)
    return self

def navigate_to_order_feed(self):
    self.click(self.ORDER_FEED_LINK)
    return self

def is_constructor_active(self):
    return "current" in self.get_element_attribute(self.CONSTRUCTOR_LINK, "class")

def is_order_feed_visible(self):
    from pages.order_feed_page import OrderFeedPage
    return OrderFeedPage(self.driver).is_visible()

def open_ingredient_details(self, ingredient_type):
    locator = (By.XPATH, f"//div[contains(text(), '{ingredient_type}')]")
    self.click(locator)
    return self

def are_ingredient_details_visible(self):
    return self.is_element_visible(self.INGREDIENT_DETAILS)

def get_ingredient_counter(self, ingredient_type):
    locator = (By.XPATH, f"//div[contains(text(), '{ingredient_type}')]//following-sibling::div[contains(@class, 'counter')]")
    return int(self.get_text(locator)) if self.is_element_present(locator) else 0

def add_ingredient_to_constructor(self, ingredient_type):
    ingredient_locator = (By.XPATH, f"//div[contains(text(), '{ingredient_type}')]")
    self.drag_and_drop(ingredient_locator, self.CONSTRUCTOR_AREA)
    return self
