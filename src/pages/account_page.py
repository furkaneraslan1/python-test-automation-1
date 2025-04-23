# src/pages/account_page.py
from selenium.webdriver.common.by import By
from . import BasePage

class AccountPage(BasePage):
    """Page object for the user account page"""
    
    # Locators
    ACCOUNT_HEADING = (By.CSS_SELECTOR, "h1.heading")
    ACCOUNT_WELCOME = (By.CSS_SELECTOR, "div.menu_text")
    EDIT_ACCOUNT_LINK = (By.LINK_TEXT, "Edit account details")
    ORDER_HISTORY_LINK = (By.LINK_TEXT, "Order history")
    TRANSACTION_HISTORY_LINK = (By.LINK_TEXT, "Transaction history")
    DOWNLOADS_LINK = (By.LINK_TEXT, "Downloads")
    LOGOUT_LINK = (By.LINK_TEXT, "Logoff")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_welcome_message(self):
        """Get the welcome message text"""
        return self.wait_for_element_visible(self.ACCOUNT_WELCOME).text
    
    def edit_account_details(self):
        """Navigate to edit account details page"""
        self.wait_for_element_clickable(self.EDIT_ACCOUNT_LINK).click()
        return self  # Could return an EditAccountPage class if you create one
    
    def view_order_history(self):
        """Navigate to order history page"""
        self.wait_for_element_clickable(self.ORDER_HISTORY_LINK).click()
        return self  # Could return an OrderHistoryPage class if you create one
    
    def logout(self):
        """Log out of the account"""
        self.wait_for_element_clickable(self.LOGOUT_LINK).click()
        from . import StoreHomePage  # Import here to avoid circular imports
        return StoreHomePage(self.driver)
    
    def is_user_logged_in(self):
        """Check if the user is logged in"""
        return self.is_element_present(self.LOGOUT_LINK)