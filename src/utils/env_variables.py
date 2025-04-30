import os

def get_env_variable(name, default=None):
    """
    Get the environment variable or return default value.
    """
    return os.environ.get(name, default)

def get_browser_from_env():
    """
    Get the browser type from environment variables.
    """
    return get_env_variable('TEST_BROWSER', 'chrome')

def get_headless_from_env():
    """
    Check if headless mode is enabled from environment variables.
    """
    headless_env = get_env_variable('TEST_HEADLESS', 'false')
    return headless_env.lower() in ('true', '1', 'yes')

def get_base_url_from_env(default="https://automationstore.com"):
    """
    Get the base URL from environment variables.
    """
    return get_env_variable('BASE_URL', default)

def get_api_url_from_env(default="https://reqres.in/api"):
    """
    Get the API URL from environment variables.
    """
    return get_env_variable('TEST_API_URL', default)