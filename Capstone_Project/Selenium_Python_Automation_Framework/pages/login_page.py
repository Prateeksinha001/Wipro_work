from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    LOGIN_URL = "https://tutorialsninja.com/demo/index.php?route=account/login"

    EMAIL_FIELD = (By.ID, "input-email")
    PASSWORD_FIELD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")
    WARNING_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-danger")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_login_page(self):
        self.driver.get(self.LOGIN_URL)

    def enter_email(self, email):
        field = self.wait.until(
            EC.visibility_of_element_located(self.EMAIL_FIELD)
        )
        field.clear()
        field.send_keys(email)

    def enter_password(self, password):
        field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_FIELD)
        )
        field.clear()
        field.send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def get_warning_message(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.WARNING_MESSAGE)
            ).text
        except Exception:
            return None