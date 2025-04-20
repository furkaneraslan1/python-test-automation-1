# src/conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def browser():
    """Simple Chrome browser fixture using local ChromeDriver"""
    print("Starting Chrome browser for testing...")
    
    driver_path = "C:\drivers\chromedriver.exe"
    
    service = Service(executable_path=driver_path)
    
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    
    yield driver
    
    print("Closing browser...")
    driver.quit()