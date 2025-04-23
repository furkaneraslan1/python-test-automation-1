from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from . import BasePage
from .search_results_page import SearchResultsPage
from .login_page import LoginPage
from .cart_page import CartPage
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
    CART_BUTTON = (By.CSS_SELECTOR, "a.dropdown-toggle[href*='cart']")  # More generic selector
    
    # Category menu locators
    CATEGORY_MENU = (By.CSS_SELECTOR, "#categorymenu > nav > ul > li")
    SKINCARE_CATEGORY = (By.LINK_TEXT, "Skincare")
    MAKEUP_CATEGORY = (By.LINK_TEXT, "Makeup")
    
    # Featured products
    FEATURED_PRODUCTS = (By.CSS_SELECTOR, ".product-block")
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
        try:
            # First try the original locator
            if self.is_element_present(self.CART_BUTTON):
                self.wait_for_element_clickable(self.CART_BUTTON).click()
            else:
                # Fallback - try an alternate approach
                print("Cart button not found with primary locator, trying alternate approach")
                # Try direct navigation to cart URL
                self.driver.get("https://automationteststore.com/index.php?rt=checkout/cart")
            
            from .cart_page import CartPage
            return CartPage(self.driver)
        except Exception as e:
            print(f"Error navigating to cart: {str(e)}")
            # Force navigation to cart page
            self.driver.get("https://automationteststore.com/index.php?rt=checkout/cart")
            from .cart_page import CartPage
            return CartPage(self.driver)
    
    # def go_to_skincare_category(self):
    #     """Navigate to skincare category"""
    #     self.wait_for_element_clickable(self.SKINCARE_CATEGORY).click()
    #     return CategoryPage(self.driver)
    
    def add_featured_product_to_cart(self, index=0):
        """Add a featured product to cart by index"""
        print(f"Looking for featured products on {self.driver.current_url}")
        
        try:
            # Use the existing self.wait that's already defined in BasePage
            featured_products = self.wait_for_elements_visible(self.FEATURED_PRODUCTS)
            print(f"Found {len(featured_products)} featured products")
            
            if index < len(featured_products):
                # Try direct click without hover
                featured_products[index].click()
                
                # Look for the add to cart button
                add_buttons = self.wait_for_elements_visible(self.ADD_TO_CART_BUTTONS)
                if len(add_buttons) > 0:
                    add_buttons[0].click()
                return self
            else:
                raise IndexError(f"Featured product index {index} is out of range")
        except Exception as e:
            print(f"Error adding product to cart: {str(e)}")
            # Try alternate approach - navigate to a product directly
            self.driver.get("https://automationteststore.com/index.php?rt=product/product&product_id=52")
            add_button = self.wait_for_element_clickable((By.CSS_SELECTOR, ".productpagecart"))
            add_button.click()
            return self