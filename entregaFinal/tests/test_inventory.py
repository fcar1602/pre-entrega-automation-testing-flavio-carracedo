import logging

import pytest
from entregaFinal.pages.inventory_page import InventoryContainer
from entregaFinal.pages.inventory_page import HeaderContainer
from entregaFinal.pages.login_page import LoginPage
from entregaFinal.data.data_login import valid_login


@pytest.mark.parametrize("username,password", valid_login)
def test_navigation_flow(driver, caplog, username, password):
    caplog.set_level(logging.INFO)
    page = LoginPage(driver)
    page.open_login_page()
    page.login(username, password)
    # Verify the app logo is visible
    logging.getLogger().info("Assert: check that the app logo is visible")
    assert HeaderContainer.is_app_logo_visible(driver), "App logo is not visible"

    # Verify the side drawer menu is visible
    logging.getLogger().info("Assert: check that the side drawer menu is visible")
    assert HeaderContainer.is_side_drawer_menu_visible(driver), "Side drawer menu is not visible"

    # Verify we are on the inventory page
    logging.getLogger().info(f"Assert: check that '/inventory.html' is in {driver.current_url}")
    assert "/inventory.html" in driver.current_url, "Did not navigate to /inventory.html"

    # Verify the inventory page title is 'Products'
    logging.getLogger().info(f"Assert: check that inventory title is 'Products' -> '{HeaderContainer.get_inventory_title(driver)}'")
    assert HeaderContainer.get_inventory_title(driver) == "Products", "Incorrect inventory title"

    # Verify there are items in the inventory list
    logging.getLogger().info("Assert: check that there are items in the inventory list")
    assert InventoryContainer.get_items_count(driver) > 0, "No items found in the inventory list"

    # Verify the inventory list is visible
    logging.getLogger().info("Assert: check that the inventory list is visible")
    assert InventoryContainer.is_inventory_list_visible(driver), "Inventory list is not visible"

    # Verify the price and name of the first item
    logging.getLogger().info(f"Assert: check that the first item's price is '$29.99' -> '{InventoryContainer.get_inventory_price(driver)}'")
    assert InventoryContainer.get_inventory_price(driver) == "$29.99", "First item price is incorrect"

    logging.getLogger().info(f"Assert: check that the first item's name is 'Sauce Labs Backpack' -> '{InventoryContainer.get_inventory_item_name(driver)}'")
    assert InventoryContainer.get_inventory_item_name(driver) == "Sauce Labs Backpack", "First item name is incorrect"
    