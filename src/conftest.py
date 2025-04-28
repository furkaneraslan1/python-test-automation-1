import pytest
import json
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Configuration loader
def load_config():
    """Load test configuration from config file"""
    config_path = os.path.join(os.path.dirname(__file__), 'config', 'test_config.json')
    with open(config_path, 'r') as file:
        return json.load(file)

@pytest.fixture(scope="session")
def config():
    """Return test configuration"""
    return load_config()

@pytest.fixture(scope="function")
def browser(request, config):
    """
    Basic fixture for Chrome browser setup.
    Returns a WebDriver instance that will be used for the test.
    """
    browser_type = request.config.getoption("--browser", default="chrome")
    headless = request.config.getoption("--headless", default=False)
    
    print(f"Starting {browser_type} browser for testing...")
    
    if browser_type.lower() == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        
        # Path to your local ChromeDriver - update this to your actual path
        driver_path = config.get("chromedriver_path", r"C:\drivers\chromedriver.exe")
        
        # Create a service object with the driver path
        service = Service(executable_path=driver_path)
        
        # Initialize the driver with the service
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_type.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser type: {browser_type}")
    
    driver.maximize_window()
    
    yield driver
    
    print("Closing browser...")
    driver.quit()

@pytest.fixture(scope="function")
def authenticated_browser(browser, config):
    """Browser with authenticated user session"""
    from src.pages.store_home_page import StoreHomePage
    
    home_page = StoreHomePage(browser)
    home_page.navigate_to()
    
    login_page = home_page.go_to_login()
    login_page.login(
        username=config.get("test_user", {}).get("username", "testuser"),
        password=config.get("test_user", {}).get("password", "password123")
    )
    
    yield browser

@pytest.fixture(scope="session")
def api_client(config):
    """Return an API client for testing"""
    from src.utils.api_client import APIClient
    base_url = config.get("api_base_url", "https://reqres.in/api")
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    return APIClient(base_url, headers)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshots on test failure"""
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        try:
            browser = item.funcargs.get("browser")
            if browser:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                test_name = item.nodeid.replace("/", "_").replace(":", "_").replace("::", "_")
                screenshot_path = os.path.join("reports", "screenshots", f"{test_name}_{timestamp}.png")
                
                # Ensure directory exists
                os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
                
                browser.save_screenshot(screenshot_path)
                print(f"Screenshot saved to: {screenshot_path}")
        except Exception as e:
            print(f"Failed to capture screenshot: {e}")

def pytest_addoption(parser):
    """Add command-line options to pytest"""
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests (chrome or firefox)")
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode")