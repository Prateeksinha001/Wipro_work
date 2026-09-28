from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-btn")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message")

    def open(self, base_url):
        self.driver.get(f"{base_url}/login")

    def enter_credentials(self, username, password):
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)

    def submit(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        """Convenience method combining the steps above -
        keeps step definitions to a single readable call."""
        self.enter_credentials(username, password)
        self.submit()

    def get_error_message(self):
        if self.is_visible(self.ERROR_MESSAGE, timeout=3):
            return self.get_text(self.ERROR_MESSAGE)
        return None
