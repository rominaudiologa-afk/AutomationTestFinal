from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage(BasePage):
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    ADD_BACKPACK_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    def count_products(self):
        self.wait.until(EC.presence_of_element_located(self.INVENTORY_ITEM))
        return len(self.driver.find_elements(*self.INVENTORY_ITEM))

    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK_BTN)

    def go_to_cart(self):
        self.click(self.CART_LINK)