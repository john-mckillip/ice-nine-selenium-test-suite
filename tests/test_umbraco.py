from pages.umbraco_login_page import UmbracoLoginPage
from dotenv import load_dotenv
import os
import pytest

# Load environment variables from .env file 
load_dotenv()

@pytest.fixture(scope="class")
def umbraco_login_url():
    return os.getenv('UMBRACO_LOGIN_URL')

@pytest.mark.usefixtures("umbraco_login_url")
class TestUmbraco:
    def test_umbraco_login_loads(self, browser, umbraco_login_url):
        umbraco_login = UmbracoLoginPage(browser)
        umbraco_login.open(umbraco_login_url)
        assert "Umbraco" in browser.title

