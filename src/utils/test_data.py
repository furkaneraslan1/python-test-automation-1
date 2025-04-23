import json
import os
import random
import string

class TestData:
    """Test data management class"""
    
    @staticmethod
    def load_test_data(filename):
        """Load test data from JSON file"""
        data_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', f"{filename}.json")
        with open(data_path, 'r') as file:
            return json.load(file)
    
    @staticmethod
    def generate_random_email():
        """Generate a random email for testing"""
        username = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
        domain = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
        return f"{username}@{domain}.com"
    
    @staticmethod
    def generate_random_name():
        """Generate a random name for testing"""
        first_names = ["John", "Jane", "Michael", "Emily", "David", "Sarah", "Robert", "Lisa"]
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Wilson"]
        return {
            "first_name": random.choice(first_names),
            "last_name": random.choice(last_names)
        }
    
    @staticmethod
    def generate_test_user():
        """Generate random user data for registration"""
        name = TestData.generate_random_name()
        return {
            "first_name": name["first_name"],
            "last_name": name["last_name"],
            "email": TestData.generate_random_email(),
            "telephone": f"555{random.randint(1000000, 9999999)}",
            "address": f"{random.randint(100, 999)} Main St",
            "city": "Test City",
            "postcode": f"{random.randint(10000, 99999)}",
            "username": f"user_{random.randint(1000, 9999)}",
            "password": f"Pass{random.randint(1000, 9999)}!"
        }