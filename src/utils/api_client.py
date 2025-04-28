import requests
import json
import logging
from urllib.parse import urljoin

class APIClient:
    """A simple API client for making HTTP requests."""

    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.session = requests.Session()
        self.headers = headers or {}
        self.logger = logging.getLogger(__name__)

    def update_headers(self, headers):
        """Update the headers for the session."""
        self.headers.update(headers)
    
    def get(self, endpoint, params=None):
        """Send GET request to API endpoint."""
        url = urljoin(self.base_url, endpoint)
        self.logger.info(f"GET request to {url}")
        response = self.session.get(url, params=params, headers=self.headers)
        return self._process_response(response)
    
    def post(self, endpoint, data=None, json_data=None):
        """Send POST request to API endpoint."""
        url = urljoin(self.base_url, endpoint)
        self.logger.info(f"POST request to {url}")
        response = self.session.post(url, data=data, json=json_data, headers=self.headers)
        return self._process_response(response)
    
    def put(self, endpoint, data=None, json_data=None):
        """Send PUT request to API endpoint."""
        url = urljoin(self.base_url, endpoint)
        self.logger.info(f"PUT request to {url}")
        response = self.session.put(url, data=data, json=json_data, headers=self.headers)
        return self._process_response(response)

    def delete(self, endpoint, data=None, json_data=None):
        """Send DELETE request to API endpoint."""
        url = urljoin(self.base_url, endpoint)
        self.logger.info(f"DELETE request to {url}")
        response = self.session.delete(url, data=data, json=json_data, headers=self.headers)
        return self._process_response(response)
    
    def _process_response(self, response):
        """Process the HTTP response."""
        try:
            self.logger.info(f"Response status code: {response.status_code}")
            if 'application/json' in response.headers.get('Content-Type', ''):
                return response.json(), response.status_code
            return response.text, response.status_code
        except json.JSONDecodeError:
            self.logger.warning("Response could not be decoded as JSON")
            return response.text, response.status_code