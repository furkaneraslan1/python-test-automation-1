# src/pages/checkout_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from . import BasePage

class CheckoutPage(BasePage):
    """Page object for the checkout process"""
    
    # Locators
    CHECKOUT_HEADING = (By.CSS_SELECTOR, ".maintext")
    
    # Step 1: Guest/Login options
    GUEST_CHECKOUT_RADIO = (By.ID, "accountFrm_accountguest")
    REGISTER_ACCOUNT_RADIO = (By.ID, "accountFrm_accountregister")
    CONTINUE_BUTTON_STEP1 = (By.CSS_SELECTOR, "button[title='Continue']")
    
    # Step 2: Guest info
    FIRST_NAME = (By.ID, "guestFrm_firstname")
    LAST_NAME = (By.ID, "guestFrm_lastname")
    EMAIL = (By.ID, "guestFrm_email")
    TELEPHONE = (By.ID, "guestFrm_telephone")
    ADDRESS_1 = (By.ID, "guestFrm_address_1")
    CITY = (By.ID, "guestFrm_city")
    REGION_DROPDOWN = (By.ID, "guestFrm_zone_id")
    POSTCODE = (By.ID, "guestFrm_postcode")
    COUNTRY_DROPDOWN = (By.ID, "guestFrm_country_id")
    CONTINUE_BUTTON_STEP2 = (By.CSS_SELECTOR, "button[title='Continue']")
    
    # Step 3: Shipping method
    SHIPPING_METHOD_FLAT_RATE = (By.ID, "shipping_shipping_flat")
    CONTINUE_BUTTON_STEP3 = (By.CSS_SELECTOR, "#shipping_form button[title='Continue']")
    
    # Step 4: Payment method
    PAYMENT_METHOD_CASH = (By.ID, "payment_cod")
    TERMS_CHECKBOX = (By.ID, "checkout_terms")
    CONTINUE_BUTTON_STEP4 = (By.CSS_SELECTOR, "#checkout_btn")
    
    # Confirmation
    ORDER_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".maintext")
    ORDER_NUMBER = (By.CSS_SELECTOR, ".contentpanel p")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def select_guest_checkout(self):
        """Select guest checkout option"""
        self.wait_for_element_clickable(self.GUEST_CHECKOUT_RADIO).click()
        return self
    
    def select_register_account(self):
        """Select register account option"""
        self.wait_for_element_clickable(self.REGISTER_ACCOUNT_RADIO).click()
        return self
    
    def continue_step1(self):
        """Continue from Step 1"""
        self.wait_for_element_clickable(self.CONTINUE_BUTTON_STEP1).click()
        return self
    
    def fill_guest_details(self, first_name, last_name, email, telephone, address, city, postcode, country="United States", region="California"):
        """Fill in guest details form"""
        self.wait_for_element_visible(self.FIRST_NAME).send_keys(first_name)
        self.wait_for_element_visible(self.LAST_NAME).send_keys(last_name)
        self.wait_for_element_visible(self.EMAIL).send_keys(email)
        self.wait_for_element_visible(self.TELEPHONE).send_keys(telephone)
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
    
    def continue_step2(self):
        """Continue from Step 2"""
        self.wait_for_element_clickable(self.CONTINUE_BUTTON_STEP2).click()
        return self
    
    def select_shipping_method(self, flat_rate=True):
        """Select shipping method"""
        if flat_rate and self.is_element_present(self.SHIPPING_METHOD_FLAT_RATE):
            self.wait_for_element_clickable(self.SHIPPING_METHOD_FLAT_RATE).click()
        return self
    
    def continue_step3(self):
        """Continue from Step 3"""
        if self.is_element_present(self.CONTINUE_BUTTON_STEP3):
            self.wait_for_element_clickable(self.CONTINUE_BUTTON_STEP3).click()
        return self
    
    def select_payment_method(self, cash_on_delivery=True):
        """Select payment method"""
        if cash_on_delivery and self.is_element_present(self.PAYMENT_METHOD_CASH):
            self.wait_for_element_clickable(self.PAYMENT_METHOD_CASH).click()
        return self
    
    def accept_terms(self):
        """Accept terms and conditions"""
        checkbox = self.wait_for_element_clickable(self.TERMS_CHECKBOX)
        if not checkbox.is_selected():
            checkbox.click()
        return self
    
    def complete_order(self):
        """Complete the order"""
        self.wait_for_element_clickable(self.CONTINUE_BUTTON_STEP4).click()
        return self
    
    def is_order_successful(self):
        """Check if order was placed successfully"""
        if self.is_element_present(self.ORDER_SUCCESS_MESSAGE):
            return "success" in self.wait_for_element_visible(self.ORDER_SUCCESS_MESSAGE).text.lower()
        return False
    
    def get_order_number(self):
        """Get the order number from the confirmation page"""
        if self.is_element_present(self.ORDER_NUMBER):
            order_text = self.wait_for_element_visible(self.ORDER_NUMBER).text
            # Extract order number using string parsing or regex if needed
            if "order #" in order_text.lower():
                return order_text.split("order #")[1].strip().split(" ")[0]
        return None
    
    def complete_checkout_as_guest(self, first_name, last_name, email, telephone, 
                                  address, city, postcode, country="United States", 
                                  region="California"):
        """Complete the entire checkout process as a guest"""
        self.select_guest_checkout()
        self.continue_step1()
        self.fill_guest_details(first_name, last_name, email, telephone, address, city, postcode, country, region)
        self.continue_step2()
        self.select_shipping_method()
        self.continue_step3()
        self.select_payment_method()
        self.accept_terms()
        self.complete_order()
        return self