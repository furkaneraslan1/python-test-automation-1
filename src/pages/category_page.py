from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from . import BasePage
from .product_page import ProductPage


class CategoryPage(BasePage):
    """Page object for category pages"""
    
    # Locators
    CATEGORY_TITLE = (By.CSS_SELECTOR, ".maintext")
    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".thumbnail")
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".prdocutname")
    PRODUCT_PRICES = (By.CSS_SELECTOR, ".oneprice, .pricenew")
    SORT_DROPDOWN = (By.ID, "sort")
    LIST_VIEW_BUTTON = (By.ID, "list")
    GRID_VIEW_BUTTON = (By.ID, "grid")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_category_title(self):
        """Get the category title"""
        return self.wait_for_element_visible(self.CATEGORY_TITLE).text
    
    def get_product_count(self):
        """Get the number of products displayed"""
        products = self.wait_for_elements_visible(self.PRODUCT_ITEMS)
        return len(products)
    
    def get_product_names(self):
        """Get all product names on the page"""
        product_elements = self.wait_for_elements_visible(self.PRODUCT_NAMES)
        return [element.text for element in product_elements]
    
    def get_product_prices(self):
        """Get all product prices on the page"""
        price_elements = self.wait_for_elements_visible(self.PRODUCT_PRICES)
        return [element.text for element in price_elements]
    
    def select_product(self, index=0):
        """Click on a product by index"""
        products = self.wait_for_elements_visible(self.PRODUCT_NAMES)
        if index < len(products):
            products[index].click()
            return ProductPage(self.driver)
        else:
            raise IndexError(f"Product index {index} is out of range")
    
    def sort_by(self, sort_option):
        """Sort products by the given option"""
        dropdown = Select(self.wait_for_element_visible(self.SORT_DROPDOWN))
        dropdown.select_by_visible_text(sort_option)
        return self
    
    def switch_to_list_view(self):
        """Switch to list view"""
        self.wait_for_element_clickable(self.LIST_VIEW_BUTTON).click()
        return self
    
    def switch_to_grid_view(self):
        """Switch to grid view"""  
        self.wait_for_element_clickable(self.GRID_VIEW_BUTTON).click()
        return self