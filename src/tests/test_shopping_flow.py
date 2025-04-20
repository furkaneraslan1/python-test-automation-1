# src/tests/test_shopping_flow.py
import pytest
import random
import string
from src.pages.store_home_page import StoreHomePage

def test_search_functionality(browser):
    """Test product search functionality"""
    # Initialize the homepage
    home_page = StoreHomePage(browser)
    home_page.navigate_to()
    
    # Search for a product
    search_results = home_page.search_for("cream")
    
    # Verify search results
    product_count = search_results.get_product_count()
    assert product_count > 0, "No products found in search results"
    
    # Verify product names contain the search term
    product_names = search_results.get_product_names()
    assert any("cream" in name.lower() for name in product_names), "Search term not found in product names"
    
    print(f"Found {product_count} products containing 'cream'")
    print(f"First few products: {', '.join(product_names[:3])}")

def test_add_to_cart(browser):
    """Test adding a product to the cart"""
    # Initialize the homepage
    home_page = StoreHomePage(browser)
    home_page.navigate_to()
    
    # Search for a specific product
    search_results = home_page.search_for("shampoo")
    
    # Select the first product
    product_page = search_results.select_product(0)
    
    # Get product details
    product_name = product_page.get_product_name()
    product_price = product_page.get_product_price()
    
    # Add to cart
    cart_page = product_page.add_to_cart()
    
    # Verify the product is in the cart
    cart_items_count = cart_page.get_cart_items_count()
    assert cart_items_count > 0, "Cart is empty after adding product"
    
    cart_product_names = cart_page.get_cart_product_names()
    assert product_name in cart_product_names, f"Product '{product_name}' not found in cart"
    
    print(f"Successfully added '{product_name}' to cart")
    print(f"Price: {product_price}")

def test_empty_cart(browser):
    """Test emptying the shopping cart"""
    # Initialize the homepage and add a product to cart
    home_page = StoreHomePage(browser)
    home_page.navigate_to()
    
    # Add a featured product to cart
    home_page.add_featured_product_to_cart(0)
    
    # Go to cart
    cart_page = home_page.view_cart()
    
    # Check that cart has items
    initial_count = cart_page.get_cart_items_count()
    assert initial_count > 0, "Cart is empty before test can proceed"
    
    # Remove the item
    cart_page.remove_item(0)
    
    # Verify cart is empty
    assert cart_page.is_cart_empty(), "Cart is not empty after removing item"
    
    print("Successfully emptied the cart")

def test_failed_login(browser):
    """Test login with invalid credentials"""
    # Initialize the homepage
    home_page = StoreHomePage(browser)
    home_page.navigate_to()
    
    # Go to login page
    login_page = home_page.go_to_login()
    
    # Generate random username and password
    random_user = ''.join(random.choices(string.ascii_lowercase, k=8))
    random_pass = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    
    # Attempt to login with invalid credentials
    result_page = login_page.login(random_user, random_pass)
    
    # Verify error message
    error_message = result_page.get_error_message()
    assert "Error: Incorrect login or password provided." in error_message
    
    print(f"Successfully verified login error: '{error_message}'")