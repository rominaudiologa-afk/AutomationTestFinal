from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"
    USER_INPUT = (By.ID, "user-name")
    PASS_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def load(self):
        self.driver.get(self.URL)
        self.log.info(f"Navegando a {self.URL}")

    def login(self, username, password):
        self.type_text(self.USER_INPUT, username)
        self.type_text(self.PASS_INPUT, password)
        self.click(self.LOGIN_BTN)