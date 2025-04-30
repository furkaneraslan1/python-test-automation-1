from selenium.webdriver.common.by import By
from . import BasePage
from .cart_page import CartPage

class ProductPage(BasePage):
    """Page object for product details page"""
    
    # Locators
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1.productname")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".productfilneprice")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".cart")
    QUANTITY_INPUT = (By.ID, "product_quantity")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_product_name(self):
        """Get the product name"""
        return self.wait_for_element_visible(self.PRODUCT_NAME).text
    
    def get_product_price(self):
        """Get the product price"""
        return self.wait_for_element_visible(self.PRODUCT_PRICE).text
    
    def set_quantity(self, quantity):
        """Set product quantity"""
        quantity_field = self.wait_for_element_visible(self.QUANTITY_INPUT)
        quantity_field.clear()
        quantity_field.send_keys(str(quantity))
        return self
    
    def add_to_cart(self):
        """Add product to cart"""
        self.wait_for_element_clickable(self.ADD_TO_CART_BUTTON).click()
        return CartPage(self.driver)