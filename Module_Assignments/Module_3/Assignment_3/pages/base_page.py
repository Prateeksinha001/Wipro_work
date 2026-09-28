"""
BasePage centralizes the low-level Selenium mechanics (explicit waits,
clicking, typing) so every page object gets robust, non-flaky interactions
for free instead of reimplementing waits in every step.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 10


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _wait(self, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout)

    def wait_for_element(self, locator, timeout=DEFAULT_TIMEOUT):
        return self._wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=DEFAULT_TIMEOUT):
        element = self._wait(timeout).until(EC.element_to_be_clickable(locator))
        element.click()

    def type_text(self, locator, text, timeout=DEFAULT_TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=DEFAULT_TIMEOUT):
        return self.wait_for_element(locator, timeout).text

    def is_visible(self, locator, timeout=DEFAULT_TIMEOUT):
        try:
            self._wait(timeout).until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def current_url(self):
        return self.driver.current_url
