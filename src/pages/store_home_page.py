# src/pages/store_home_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class StoreHomePage(BasePage):
    """Page object for Automation Test Store homepage"""
    
    # URL
    URL = "https://automationteststore.com/"
    
    # Locators
    LOGO = (By.CSS_SELECTOR, "#logo img")
    SEARCH_BOX = (By.ID, "filter_keyword")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".button-in-search")
    ACCOUNT_MENU = (By.CSS_SELECTOR, "ul.info_links_footer li:nth-child(3) a")
    LOGIN_LINK = (By.LINK_TEXT, "Login")
    CART_BUTTON = (By.CSS_SELECTOR, ".dropdown-toggle[title='Shopping Cart']")
    
    # Category menu locators
    CATEGORY_MENU = (By.CSS_SELECTOR, "#categorymenu > nav > ul > li")
    SKINCARE_CATEGORY = (By.LINK_TEXT, "Skincare")
    MAKEUP_CATEGORY = (By.LINK_TEXT, "Makeup")
    
    # Featured products
    FEATURED_PRODUCTS = (By.CSS_SELECTOR, ".thumbnails.row > div")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, ".productcart")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate_to(self):
        """Navigate to the homepage"""
        self.driver.get(self.URL)
        return self
    
    def search_for(self, keyword):
        """Search for a product"""
        search_box = self.wait_for_element_visible(self.SEARCH_BOX)
        search_box.clear()
        search_box.send_keys(keyword)
        self.wait_for_element_clickable(self.SEARCH_BUTTON).click()
        return SearchResultsPage(self.driver)
    
    def go_to_login(self):
        """Navigate to login page"""
        self.wait_for_element_clickable(self.LOGIN_LINK).click()
        return LoginPage(self.driver)
    
    def view_cart(self):
        """View shopping cart"""
        self.wait_for_element_clickable(self.CART_BUTTON).click()
        return CartPage(self.driver)
    
    def go_to_skincare_category(self):
        """Navigate to skincare category"""
        self.wait_for_element_clickable(self.SKINCARE_CATEGORY).click()
        return CategoryPage(self.driver)
    
    def add_featured_product_to_cart(self, index=0):
        """Add a featured product to cart by index"""
        featured_products = self.wait_for_elements_visible(self.FEATURED_PRODUCTS)
        if index < len(featured_products):
            # Hover over the product to make the Add to Cart button visible
            self.hover_over_element((By.CSS_SELECTOR, f".thumbnails.row > div:nth-child({index+1})"))
            # Click the Add to Cart button for the specific product
            add_buttons = self.wait_for_elements_visible(self.ADD_TO_CART_BUTTONS)
            add_buttons[index].click()
            return self
        else:
            raise IndexError(f"Featured product index {index} is out of range")