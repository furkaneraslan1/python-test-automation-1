# src/pages/cart_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    """Page object for shopping cart page"""
    
    # Locators
    CART_ITEMS = (By.CSS_SELECTOR, ".product-list tr")
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".align_left a")
    CHECKOUT_BUTTON = (By.ID, "cart_checkout1")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, ".contentpanel")
    TOTAL_PRICE = (By.CSS_SELECTOR, ".bold.totalamout")
    REMOVE_ICONS = (By.CSS_SELECTOR, ".remove")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_cart_items_count(self):
        """Get the number of items in the cart"""
        if self.is_element_present(self.CART_ITEMS):
            # Subtracting 1 to account for the header row
            return len(self.wait_for_elements_visible(self.CART_ITEMS)) - 1
        return 0
    
    def get_cart_product_names(self):
        """Get list of product names in the cart"""
        if self.is_element_present(self.PRODUCT_NAMES):
            product_elements = self.wait_for_elements_visible(self.PRODUCT_NAMES)
            return [element.text for element in product_elements]
        return []
    
    def proceed_to_checkout(self):
        """Proceed to checkout"""
        if self.is_element_present(self.CHECKOUT_BUTTON):
            self.wait_for_element_clickable(self.CHECKOUT_BUTTON).click()
            return CheckoutPage(self.driver)
        return None
    
    def get_total_price(self):
        """Get the total price of items in cart"""
        if self.is_element_present(self.TOTAL_PRICE):
            return self.wait_for_element_visible(self.TOTAL_PRICE).text
        return "0"
    
    def remove_item(self, index=0):
        """Remove an item from the cart by index"""
        if self.is_element_present(self.REMOVE_ICONS):
            remove_buttons = self.wait_for_elements_visible(self.REMOVE_ICONS)
            if index < len(remove_buttons):
                remove_buttons[index].click()
                return self
        return self
    
    def is_cart_empty(self):
        """Check if the cart is empty"""
        if self.is_element_present(self.EMPTY_CART_MESSAGE):
            message = self.wait_for_element_visible(self.EMPTY_CART_MESSAGE).text
            return "Your shopping cart is empty" in message
        return False