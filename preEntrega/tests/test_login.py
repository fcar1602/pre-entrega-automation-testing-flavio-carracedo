import logging
from preEntrega.pages.login_page import LoginPage
from preEntrega.pages.inventory_page import HeaderContainer

def test_login_success(driver, caplog):
    caplog.set_level(logging.INFO)
    # Open the login page
    logging.getLogger().info("Open login page")
    LoginPage(driver).open_login_page()
    # Perform login with a standard user
    logging.getLogger().info("Logging in with standard_user")
    LoginPage(driver).login("standard_user", "secret_sauce")
    # Verify we navigated to the inventory page
    logging.getLogger().info(f"Assert: check that '/inventory.html' is in {driver.current_url}")
    assert "/inventory.html" in driver.current_url, "Did not navigate to /inventory.html"

    # Verify the page title contains 'Swag Labs'
    logging.getLogger().info(f"Assert: title contains 'Swag Labs' -> '{driver.title}'")
    assert "Swag Labs" in driver.title, "Incorrect title"

    # Verify the inventory page title is 'Products'
    logging.getLogger().info(f"Assert: title contains 'Products' -> '{HeaderContainer.get_inventory_title(driver)}'")
    assert HeaderContainer.get_inventory_title(driver) == "Products", "Incorrect inventory title"



