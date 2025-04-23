# src/pages/register_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from . import BasePage

class RegisterPage(BasePage):
    """Page object for the account registration page"""
    
    # Locators
    FIRST_NAME = (By.ID, "AccountFrm_firstname")
    LAST_NAME = (By.ID, "AccountFrm_lastname")
    EMAIL = (By.ID, "AccountFrm_email")
    TELEPHONE = (By.ID, "AccountFrm_telephone")
    ADDRESS_1 = (By.ID, "AccountFrm_address_1")
    CITY = (By.ID, "AccountFrm_city")
    REGION_DROPDOWN = (By.ID, "AccountFrm_zone_id")
    POSTCODE = (By.ID, "AccountFrm_postcode")
    COUNTRY_DROPDOWN = (By.ID, "AccountFrm_country_id")
    LOGIN_NAME = (By.ID, "AccountFrm_loginname")
    PASSWORD = (By.ID, "AccountFrm_password")
    PASSWORD_CONFIRM = (By.ID, "AccountFrm_confirm")
    PRIVACY_POLICY_CHECKBOX = (By.ID, "AccountFrm_agree")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "button[title='Continue']")
    REGISTER_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".maintext")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def fill_personal_details(self, first_name, last_name, email, telephone):
        """Fill in personal details section"""
        self.wait_for_element_visible(self.FIRST_NAME).send_keys(first_name)
        self.wait_for_element_visible(self.LAST_NAME).send_keys(last_name)
        self.wait_for_element_visible(self.EMAIL).send_keys(email)
        self.wait_for_element_visible(self.TELEPHONE).send_keys(telephone)
        return self
    
    def fill_address(self, address, city, postcode, country="United States", region="California"):
        """Fill in address section"""
        self.wait_for_element_visible(self.ADDRESS_1).send_keys(address)
        self.wait_for_element_visible(self.CITY).send_keys(city)
        self.wait_for_element_visible(self.POSTCODE).send_keys(postcode)
        
        # Select country
        country_dropdown = Select(self.wait_for_element_visible(self.COUNTRY_DROPDOWN))
        country_dropdown.select_by_visible_text(country)
        
        # Select region/state
        region_dropdown = Select(self.wait_for_element_visible(self.REGION_DROPDOWN))
        region_dropdown.select_by_visible_text(region)
        
        return self
    
    def fill_login_details(self, username, password):
        """Fill in login details section"""
        self.wait_for_element_visible(self.LOGIN_NAME).send_keys(username)
        self.wait_for_element_visible(self.PASSWORD).send_keys(password)
        self.wait_for_element_visible(self.PASSWORD_CONFIRM).send_keys(password)
        return self
    
    def accept_privacy_policy(self):
        """Check the privacy policy checkbox"""
        checkbox = self.wait_for_element_clickable(self.PRIVACY_POLICY_CHECKBOX)
        if not checkbox.is_selected():
            checkbox.click()
        return self
    
    def click_continue(self):
        """Click continue button to complete registration"""
        self.wait_for_element_clickable(self.CONTINUE_BUTTON).click()
        
        # Check if registration was successful
        if self.is_element_present(self.REGISTER_SUCCESS_MESSAGE):
            from . import AccountPage
            return AccountPage(self.driver)
        return self
    
    def register_new_account(self, first_name, last_name, email, telephone, 
                             address, city, postcode, username, password,
                             country="United States", region="California"):
        """Complete the full registration process"""
        self.fill_personal_details(first_name, last_name, email, telephone)
        self.fill_address(address, city, postcode, country, region)
        self.fill_login_details(username, password)
        self.accept_privacy_policy()
        return self.click_continue()