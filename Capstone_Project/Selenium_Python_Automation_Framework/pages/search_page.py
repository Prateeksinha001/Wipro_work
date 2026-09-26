from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:

    PRODUCT_LINK = (
        By.CSS_SELECTOR,
        ".product-thumb h4 a"
    )

    PRODUCT_NAME = (
        By.CSS_SELECTOR,
        ".product-thumb h4 a"
    )

    ADD_TO_CART_BUTTON = (
        By.ID,
        "button-cart"
    )

    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR,
        ".alert-success"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def get_product_name(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.PRODUCT_NAME)
        ).text

    def select_product(self):
        self.wait.until(
            EC.element_to_be_clickable(self.PRODUCT_LINK)
        ).click()

    def add_to_cart(self):
        button = self.wait.until(
            EC.visibility_of_element_located(self.ADD_TO_CART_BUTTON)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            button
        )

        self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        )

    def get_success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        ).text