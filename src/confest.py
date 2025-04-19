# src/conftest.py
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def browser():
    """
    Basic fixture for Chrome browser setup.
    Returns a WebDriver instance that will be used for the test.
    """
    print("Starting Chrome browser for testing...")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    
    yield driver
    
    print("Closing browser...")
    driver.quit()