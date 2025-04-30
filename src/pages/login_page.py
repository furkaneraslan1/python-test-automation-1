from selenium.webdriver.common.by import By
from . import BasePage
from .account_page import AccountPage
from .register_page import RegisterPage

class LoginPage(BasePage):
    """Page object for login page"""
    
    # Locators
    LOGIN_EMAIL = (By.ID, "loginFrm_loginname")
    LOGIN_PASSWORD = (By.ID, "loginFrm_password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[title='Login']")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[title='Continue']")
    ERROR_MESSAGE = (By.CLASS_NAME, "alert-error")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def login(self, username, password):
        """Login with credentials"""
        self.wait_for_element_visible(self.LOGIN_EMAIL).send_keys(username)
        self.wait_for_element_visible(self.LOGIN_PASSWORD).send_keys(password)
        self.wait_for_element_clickable(self.LOGIN_BUTTON).click()
        
        # Check if there's an error
        if self.is_element_present(self.ERROR_MESSAGE):
            return self
        return AccountPage(self.driver)
    
    def go_to_create_account(self):
        """Navigate to account creation page"""
        self.wait_for_element_clickable(self.CREATE_ACCOUNT_BUTTON).click()
        return RegisterPage(self.driver)
    
    def get_error_message(self):
        """Get login error message if present"""
        if self.is_element_present(self.ERROR_MESSAGE):
            return self.wait_for_element_visible(self.ERROR_MESSAGE).text
        return ""