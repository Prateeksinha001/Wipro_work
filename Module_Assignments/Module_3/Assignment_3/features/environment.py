"""
Behave environment hooks.

Beyond driver setup/teardown (Scenario 1 pattern), this also:
  - instantiates page objects once per scenario and attaches them to
    `context`, so step definitions never touch Selenium directly.
  - captures a screenshot automatically whenever a step fails, which is the
    single highest-value "debugging" addition for a Selenium+Behave suite
    (Day 4's "debug and optimize" task).
"""

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

BASE_URL = os.environ.get("BASE_URL", "http://localhost:8080")
HEADLESS = os.environ.get("HEADLESS", "false").lower() == "true"
SCREENSHOT_DIR = "reports/screenshots"


def before_all(context):
    context.base_url = BASE_URL

    options = webdriver.ChromeOptions()
    if HEADLESS:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,900")

    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )
    context.driver.implicitly_wait(2)

    os.makedirs(SCREENSHOT_DIR, exist_ok=True)


def before_scenario(context, scenario):
    context.driver.delete_all_cookies()
    # Page objects, re-created each scenario for a clean state
    context.login_page = LoginPage(context.driver)
    context.dashboard_page = DashboardPage(context.driver)


def after_step(context, step):
    if step.status == "failed":
        safe_name = "".join(c if c.isalnum() else "_" for c in step.name)[:60]
        path = os.path.join(SCREENSHOT_DIR, f"{safe_name}.png")
        context.driver.save_screenshot(path)
        print(f"[DEBUG] Screenshot saved on failure: {path}")


def after_all(context):
    context.driver.quit()
