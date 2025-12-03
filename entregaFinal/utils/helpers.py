from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def wait_for_visibility(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))

def wait_for_clickable(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))

def click_when_clickable(driver, locator, timeout=10):
    el = wait_for_clickable(driver, locator, timeout)
    el.click()
    return el