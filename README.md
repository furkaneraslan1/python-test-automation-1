# Test Automation Framework

![Test Status](https://github.com/furkaneraslan1/test-automation-framework/workflows/Test%20Automation/badge.svg)

A comprehensive test automation framework built with Python and Selenium.

## Features

- Web UI testing with Selenium WebDriver
- API testing capabilities
- Data-driven testing
- CI/CD integration with GitHub Actions
- Cross-browser testing
- Reporting functionality

## Test Status

| Test Suite | Status |
|------------|--------|
| Smoke Tests | ![Smoke Tests](https://github.com/furkaneraslan1/test-automation-framework/workflows/Test%20Automation/badge.svg?branch=main) |
| API Tests | ![API Tests](https://github.com/furkaneraslan1/test-automation-framework/workflows/Test%20Automation/badge.svg?branch=main) |
| Regression Tests | ![Regression Tests](https://github.com/furkaneraslan1/test-automation-framework/workflows/Test%20Automation/badge.svg?branch=main) |

## Setup and Installation

1. Clone this repository
2. Install the required dependencies: `pip install -r requirements.txt`
3. Configure the environment variables as needed

## Running Tests

```bash
# Run all tests
pytest

# Run specific test suites
pytest -m smoke  # Run smoke tests
pytest -m api    # Run API tests 
pytest -m cart   # Run shopping cart tests

# Run tests with specific browser
pytest --browser=firefox

# Run tests in headless mode
pytest --headless