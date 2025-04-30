import pytest

@pytest.mark.api
def test_create_user(api_client):
    """Test POST /api/users endpoint"""
    new_user_data = {
        "name": "John Doe",
        "job": "Software Engineer"
    }
    response_data, status_code = api_client.post("users", json_data=new_user_data)
    
    # Basic response validation
    assert status_code == 201, f"Expected status code 201, got {status_code}"
    assert "id" in response_data, "Response does not contain 'id' field"
    assert response_data["name"] == new_user_data["name"], "Name does not match expected value"
    assert response_data["job"] == new_user_data["job"], "Job does not match expected value"
    
    print(f"Successfully created user: {response_data['name']} with job: {response_data['job']}")

@pytest.mark.api
def test_get_single_user(api_client):
    """Test GET /api/users/2 endpoint"""
    user_id = 2  # Using a known existing user ID
    response_data, status_code = api_client.get(f"users/{user_id}")
    
    # Basic response validation
    assert status_code == 200, f"Expected status code 200, got {status_code}"
    assert "data" in response_data, "Response does not contain 'data' field"
    assert response_data["data"]["id"] == user_id, "User ID does not match expected value"
    
    user = response_data["data"]
    print(f"Successfully retrieved user: {user['first_name']} {user['last_name']}")

@pytest.mark.api
def test_update_user(api_client):
    """Test PUT /api/users/2 endpoint"""
    user_id = 2  # Using a known existing user ID
    updated_user_data = {
        "name": "Jane Doe",
        "job": "Senior Software Engineer"
    }
    response_data, status_code = api_client.put(f"users/{user_id}", json_data=updated_user_data)
    
    # Basic response validation
    assert status_code == 200, f"Expected status code 200, got {status_code}"
    assert response_data["name"] == updated_user_data["name"], "Name does not match expected value"
    assert response_data["job"] == updated_user_data["job"], "Job does not match expected value"
    assert "updatedAt" in response_data, "Response does not contain timestamp"
    
    print(f"Successfully updated user: {response_data['name']} with job: {response_data['job']}")

@pytest.mark.api
def test_delete_user(api_client):
    """Test DELETE /api/users/2 endpoint"""
    user_id = 2  # Using a known existing user ID
    response_data, status_code = api_client.delete(f"users/{user_id}")
    
    # Basic response validation
    assert status_code == 204, f"Expected status code 204, got {status_code}"
    
    print(f"Successfully deleted user with ID {user_id}")

@pytest.mark.api
def test_get_users_list(api_client):
    """Test GET /api/users endpoint (list)"""
    response_data, status_code = api_client.get("users")
    
    # Basic response validation
    assert status_code == 200, f"Expected status code 200, got {status_code}"
    assert "data" in response_data, "Response does not contain 'data' field"
    assert "page" in response_data, "Response does not contain pagination info"
    assert len(response_data["data"]) > 0, "Users list is empty"
    
    print(f"Successfully retrieved {len(response_data['data'])} users")