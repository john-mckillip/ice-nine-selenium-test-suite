from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        """Opens a webpage."""
        self.driver.get(url)

    def find(self, locator):
        """Finds an element."""
        return self.driver.find_element(*locator)

    def click(self, locator):
        """Clicks an element."""
        self.find(locator).click()

    def type(self, locator, text):
        """Types text into an input field."""
        self.find(locator).send_keys(text)

    def wait_for_element(self, locator):
        """Waits for an element to be visible."""
        return self.wait.until(EC.visibility_of_element_located(locator))