from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    CART_LINK = (By.CSS_SELECTOR, "#cart > button")

    VIEW_CART_LINK = (
        By.CSS_SELECTOR,
        "#cart .dropdown-menu li:last-child a"
    )

    PRODUCT_NAME = (
        By.XPATH,
        "//*[@id='content']//table//tbody//tr//td//a[contains(@href, 'product/product') and normalize-space()]"
    )

    QUANTITY_FIELD = (
        By.CSS_SELECTOR,
        "table tbody tr input[name^='quantity']"
    )

    UPDATE_BUTTON = (
        By.CSS_SELECTOR,
        "table tbody tr button[data-original-title='Update']"
    )

    REMOVE_BUTTON = (
        By.CSS_SELECTOR,
        "table tbody tr button[data-original-title='Remove']"
    )

    CART_TOTAL = (
        By.CSS_SELECTOR,
        "#cart-total"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        ).click()

        self.wait.until(self._click_view_cart)

    def _click_view_cart(self, driver):
        try:
            link = driver.find_element(*self.VIEW_CART_LINK)
            if not link.is_displayed() or not link.is_enabled():
                return False
            link.click()
            return True
        except StaleElementReferenceException:
            return False

    def get_product_name(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.PRODUCT_NAME)
        ).text

    def get_quantity(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.QUANTITY_FIELD)
        ).get_attribute("value")

    def update_quantity(self, quantity):
        field = self.wait.until(
            EC.visibility_of_element_located(self.QUANTITY_FIELD)
        )

        field.clear()
        field.send_keys(str(quantity))

        self.wait.until(
            EC.element_to_be_clickable(self.UPDATE_BUTTON)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(self.QUANTITY_FIELD)
        )

    def get_cart_total(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.CART_TOTAL)
        ).text

    def remove_product(self):
        self.wait.until(
            EC.element_to_be_clickable(self.REMOVE_BUTTON)
        ).click()