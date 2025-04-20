from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    """Base class that all page models can inherit from"""
    
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(driver, self.timeout)
    
    def get_title(self):
        """Returns the title of the current page"""
        return self.driver.title
    
    def get_url(self):
        """Returns the URL of the current page"""
        return self.driver.current_url
    
    def wait_for_element_visible(self, locator):
        """Wait for an element to be visible"""
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def wait_for_element_clickable(self, locator):
        """Wait for an element to be clickable"""
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def wait_for_elements_visible(self, locator):
        """Wait for elements to be visible"""
        return self.wait.until(EC.visibility_of_all_elements_located(locator))
    
    def is_element_present(self, locator):
        """Check if an element is present on the page"""
        try:
            self.wait_for_element_visible(locator)
            return True
        except TimeoutException:
            return False
            
    def hover_over_element(self, locator):
        """Hover over an element"""
        element = self.wait_for_element_visible(locator)
        ActionChains(self.driver).move_to_element(element).perform()
        return self