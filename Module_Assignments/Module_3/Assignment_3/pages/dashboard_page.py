from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):
    WELCOME_BANNER = (By.CSS_SELECTOR, ".welcome-banner")

    def is_loaded(self):
        return "dashboard" in self.current_url()

    def get_welcome_text(self):
        return self.get_text(self.WELCOME_BANNER)
