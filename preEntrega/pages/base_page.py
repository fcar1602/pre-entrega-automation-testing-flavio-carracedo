from preEntrega.utils import helpers

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def click(self, locator, timeout=10):
        element = helpers.wait_for_clickable(self.driver, locator, timeout)
        element.click()

    def type(self, locator, text, timeout=10):
        element = helpers.wait_for_visibility(self.driver, locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=10):
        element = helpers.wait_for_visibility(self.driver, locator, timeout)
        return element.text