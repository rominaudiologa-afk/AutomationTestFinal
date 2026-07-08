import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.log = logging.getLogger(__name__)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        self.log.info(f"Click realizado en el elemento: {locator}")

    def type_text(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)
        self.log.info(f"Texto ingresado en {locator}")

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text