from selenium.webdriver.common.by import By
from . import BasePage
from .product_page import ProductPage

class SearchResultsPage(BasePage):
    """Page object for search results page"""
    
    # Locators
    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".list-inline > div")
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".fixed_wrapper .prdocutname")
    NO_RESULTS_MESSAGE = (By.CSS_SELECTOR, ".contentpanel")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_product_count(self):
        """Get the number of products in search results"""
        if self.is_element_present(self.PRODUCT_ITEMS):
            products = self.wait_for_elements_visible(self.PRODUCT_ITEMS)
            return len(products)
        return 0
    
    def get_product_names(self):
        """Get list of product names from search results"""
        if self.is_element_present(self.PRODUCT_NAMES):
            product_elements = self.wait_for_elements_visible(self.PRODUCT_NAMES)
            return [element.text for element in product_elements]
        return []
    
    def select_product(self, index=0):
        """Select a product from search results by index"""
        if self.is_element_present(self.PRODUCT_NAMES):
            product_links = self.wait_for_elements_visible(self.PRODUCT_NAMES)
            if index < len(product_links):
                product_links[index].click()
                return ProductPage(self.driver)
        return None
    
    def no_results_message(self):
        """Get the no results message if present"""
        if self.is_element_present(self.NO_RESULTS_MESSAGE):
            return self.wait_for_element_visible(self.NO_RESULTS_MESSAGE).text
        return ""