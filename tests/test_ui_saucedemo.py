import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.ui
@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    # Aquí podrías agregar más usuarios como "problem_user"
])
def test_flujo_completo_compra(driver, username, password):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    # 1. Login
    login_page.load()
    login_page.login(username, password)
    assert "inventory.html" in driver.current_url
    
    # 2. Inventario
    productos_encontrados = inventory_page.count_products()
    assert productos_encontrados > 0
    
    # 3. Carrito
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()
    
    item_text = inventory_page.get_text(inventory_page.ITEM_NAME)
    assert item_text == "Sauce Labs Backpack"