import pytest
import json
from jsonschema import validate

USER_SCHEMA = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "email": {"type": "string", "format": "email"},
                "first_name": {"type": "string"},
                "last_name": {"type": "string"},
                "avatar": {"type": "string", "format": "uri"}
            },
            "required": ["id", "email", "first_name", "last_name", "avatar"]
        },
        "support": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "format": "uri"},
                "text": {"type": "string"}
            },
            "required": ["url", "text"]
        }
    },
    "required": ["data", "support"]
}

@pytest.mark_api
def test_get_user(api_client):
    """Test GET /api/users/2 endpoint"""
    response_data, status_code = api_client.get("/users/2")
    assert status_code == 200, f"Expected status code 200, got {status_code}"
    validate(instance=response_data, schema=USER_SCHEMA)
    assert response_data["data"]["id"] == 2, "User ID does not match expected value"
    assert "janet.weaver@reqres.in" in response_data["data"]["email"], "Email does not match expected value"

    print(f"Successfully retrieved user: {response_data['data']['first_name']} {response_data['data']['last_name']}")

@pytest.mark_api
def test_create_user(api_client):
    """Test POST /api/users endpoint"""
    new_user_data = {
        "name": "John Doe",
        "job": "Software Engineer"
    }
    response_data, status_code = api_client.post("users", json_data=new_user_data)
    assert status_code == 201, f"Expected status code 201, got {status_code}"
    
    # Validate the response schema
    assert "id" in response_data, "Response does not contain 'id' field"
    assert response_data["name"] == new_user_data["name"], "Name does not match expected value"
    assert response_data["job"] == new_user_data["job"], "Job does not match expected value"

    print(f"Successfully created user: {response_data['name']} with job: {response_data['job']}")

@pytest.mark_api
def test_update_user(api_client):
    """Test PUT /api/users/2 endpoint"""
    updated_user_data = {
        "name": "Jane Doe",
        "job": "Senior Software Engineer"
    }
    response_data, status_code = api_client.put("/users/2", json_data=updated_user_data)
    assert status_code == 200, f"Expected status code 200, got {status_code}"
    
    # Validate the response schema
    assert response_data["name"] == updated_user_data["name"], "Name does not match expected value"
    assert response_data["job"] == updated_user_data["job"], "Job does not match expected value"

    print(f"Successfully updated user: {response_data['name']} with job: {response_data['job']}")

@pytest.mark_api
def test_delete_user(api_client):
    """Test DELETE /api/users/2 endpoint"""
    response_data, status_code = api_client.delete("/users/2")
    assert status_code == 204, f"Expected status code 204, got {status_code}"
    
    # Validate that the response is empty
    assert response_data == {}, "Response should be empty for DELETE request"

    print("Successfully deleted user with ID 2")