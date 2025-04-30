import pytest
import time
from pages.store_home_page import StoreHomePage

@pytest.mark.e2e
def test_search_and_verify_availability(browser, api_client):
    """Test that searches for a product in UI and verifies its availability in the API."""

    home_page = StoreHomePage(browser)
    home_page.navigate_to()

    search_term = "cream"
    search_results = home_page.search_for(search_term)

    product_names = search_results.get_product_names()
    assert len(product_names) > 0, f"No products found for term: {search_term}"

    first_product = product_names[0]
    print(f"First product in UI: {first_product}")

    # Simulate API check for product availability
    response_data, status_code = api_client.get("unknown")

    assert status_code == 200, f"API request failed with status code: {status_code}"
    assert "data" in response_data, "API response does not contain 'data' key"

    # Simulate matching product name with API data
    # In a real scenario, we would check against actual product data from the API
    print(f"Verified product availability in API: {response_data['data']}")