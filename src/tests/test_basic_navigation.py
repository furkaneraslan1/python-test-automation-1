import pytest

def test_website_title(browser):
    """
    Basic test to verify website title.
    """
    # Navigate to a website
    browser.get("https://www.example.com")
    
    # Assert the title contains expected text
    assert "Example" in browser.title
    
    # Add a simple print for verification
    print(f"Website title: {browser.title}")