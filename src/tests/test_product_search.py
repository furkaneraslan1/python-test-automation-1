import pytest
from pages.store_home_page import StoreHomePage
from utils.test_data import TestData

@pytest.mark.parametrize(
    "search_term,expected_results", 
    [
        ("cream", True),
        ("shampoo", True),
        ("xyzabc123", False)  # Should return no results
    ]
)
def test_product_search_with_various_terms(browser, search_term, expected_results):
    """Test searching for various products"""
    # Initialize the homepage
    home_page = StoreHomePage(browser)
    home_page.navigate_to()
    
    # Search for the product
    search_results = home_page.search_for(search_term)
    
    # Get product count
    product_count = search_results.get_product_count()
    
    # Verify results match expectations
    if expected_results:
        assert product_count > 0, f"No products found for term: {search_term}"
        print(f"Found {product_count} products for '{search_term}'")
    else:
        assert product_count == 0, f"Expected no results for term: {search_term}, but found {product_count}"
        print(f"Confirmed no results for '{search_term}' as expected")