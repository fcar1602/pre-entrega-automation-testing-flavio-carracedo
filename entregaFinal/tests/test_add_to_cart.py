import logging

import pytest
from entregaFinal.pages.cart_page import CartListContainer
from entregaFinal.pages.inventory_page import InventoryContainer
from entregaFinal.pages.inventory_page import HeaderContainer
from entregaFinal.pages.login_page import LoginPage
from entregaFinal.data.data_login import valid_login

@pytest.mark.parametrize("username,password", valid_login)
def test_add_to_cart(driver, caplog, username, password):
    caplog.set_level(logging.INFO)
    page = LoginPage(driver)
    page.open_login_page()
    page.login(username, password)
    # Log the current number of items in inventory
    InventoryContainer.get_items_count(driver)
    logging.getLogger().info(f"Number of items in inventory: {InventoryContainer.get_items_count(driver)}")

    # Click the 'Add to cart' button for the first item
    logging.getLogger().info("Clicking the 'Add to cart' button")
    InventoryContainer.click_add_to_cart_by_index(driver, index=0)

    # Open the shopping cart
    HeaderContainer.click_your_cart_button(driver)
    logging.getLogger().info("Clicked the shopping cart button")

    # Log the cart badge number
    CartListContainer.get_cart_inventory_qty(driver)
    logging.getLogger().info(f"Number in shopping cart badge: {CartListContainer.get_cart_inventory_qty(driver)}")

    # Verify there is an item in the shopping cart
    logging.getLogger().info("Verifying that an item exists in the shopping cart")
    CartListContainer.is_cart_item_visible(driver)
    assert CartListContainer.is_cart_item_visible(driver) == True