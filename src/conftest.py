# src/conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def browser():
    """Simple Chrome browser fixture using local ChromeDriver"""
    print("Starting Chrome browser for testing...")
    
    # Path to your local ChromeDriver - update this to your actual path
    driver_path = "C:\drivers\chromedriver.exe"
    
    # Create a service object with the driver path
    service = Service(executable_path=driver_path)
    
    # Initialize the driver with the service
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    
    # Return the driver to the test
    yield driver
    
    # Clean up after the test is done
    print("Closing browser...")
    driver.quit()