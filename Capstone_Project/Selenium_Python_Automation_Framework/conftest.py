import os
import pytest

from utils.driver_factory import DriverFactory
from utils.config_reader import ConfigReader
from utils.csv_reader import CSVReader
from utils.screenshot import Screenshot


config = ConfigReader()


@pytest.fixture(scope="session")
def driver():

    browser = config.get("browser")
    headless = config.get_boolean("headless")

    driver = DriverFactory.create_driver(
        browser=browser,
        headless=headless
    )

    driver.maximize_window()

    driver.get(config.get("base_url"))

    yield driver

    driver.quit()


@pytest.fixture(autouse=True)
def reset_browser(driver):

    driver.get(config.get("base_url"))

    yield


@pytest.fixture(scope="function")
def test_data():

    data = CSVReader.read_data()

    return data[0]


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            test_name = item.name

            Screenshot.capture(
                driver,
                test_name
            )