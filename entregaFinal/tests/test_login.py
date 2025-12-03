import logging
import pytest
from entregaFinal.pages.login_page import LoginPage
from entregaFinal.pages.inventory_page import HeaderContainer
from entregaFinal.data.data_login import data_login

@pytest.mark.parametrize("username,password,login_bool", data_login)
def test_login(driver, caplog, username, password, login_bool):
    caplog.set_level(logging.INFO)
    # Open the login page
    logging.getLogger().info("Open login page")
    LoginPage(driver).open_login_page()
    # Perform login with a standard user
    logging.getLogger().info(f"Logging in with {username}")
    LoginPage(driver).login(username, password)

    if login_bool:

        # Verify we navigated to the inventory page
        logging.getLogger().info(f"Assert: check that '/inventory.html' is in {driver.current_url}")
        assert "/inventory.html" in driver.current_url, "Did not navigate to /inventory.html"

        # Verify the page title contains 'Swag Labs'
        logging.getLogger().info(f"Assert: title contains 'Swag Labs' -> '{driver.title}'")
        assert "Swag Labs" in driver.title, "Incorrect title"

        # Verify the inventory page title is 'Products'
        logging.getLogger().info(f"Assert: title contains 'Products' -> '{HeaderContainer.get_inventory_title(driver)}'")
        assert HeaderContainer.get_inventory_title(driver) == "Products", "Incorrect inventory title"

    else:
        # Negative scenario: should NOT reach inventory
        logging.getLogger().info("Assert: current_url should NOT contain '/inventory.html'")
        assert "/inventory.html" not in driver.current_url, "Unexpected navigation to inventory for invalid credentials"

        # SauceDemo stays on base page (https://www.saucedemo.com/) with same title
        logging.getLogger().info(f"Assert: title contains 'Swag Labs' -> '{driver.title}'")
        assert "Swag Labs" in driver.title, "Incorrect title on failed login"

