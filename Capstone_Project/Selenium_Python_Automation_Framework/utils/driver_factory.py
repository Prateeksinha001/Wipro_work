from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class DriverFactory:

    @staticmethod
    def create_driver(browser="chrome", headless=False):

        if browser.lower() == "chrome":

            options = Options()

            if headless:
                options.add_argument("--headless=new")

            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-popup-blocking")

            driver = webdriver.Chrome(options=options)

            return driver

        raise ValueError(
            f"Unsupported browser: {browser}"
        )