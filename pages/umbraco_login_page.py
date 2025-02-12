from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class UmbracoLoginPage(BasePage):
    Email_Input = (By.NAME, "username")
    Password_Input = (By.NAME, "password")
    Login_Button = (By.ID, "button")

    def __init__(self, driver):
        super().__init__(driver)