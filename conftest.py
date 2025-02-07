import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    """Add a command-line option for headless mode."""
    parser.addoption("--headless", action="store_true", help="Run tests in headless mode")

@pytest.fixture(scope="function")
def browser(request):
    """Set up WebDriver with optional headless mode."""
    options = Options()
    
    # Enable headless mode if the command-line option is provided
    if request.config.getoption("--headless"):
        options.add_argument("--headless=new")  # 'new' prevents deprecation warnings
        options.add_argument("--disable-gpu")  # Required for some environments
        options.add_argument("--window-size=1920,1080")  # Ensure consistent test results
        options.add_argument("--no-sandbox")  # Recommended for CI/CD environments
        options.add_argument("--disable-dev-shm-usage")  # Fixes issues in Docker containers
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    
    yield driver
    driver.quit()