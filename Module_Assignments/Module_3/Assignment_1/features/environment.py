"""
Behave environment hooks.

BASE_URL is the single switch between:
  - a real device/application under test, and
  - the QEMU-simulated embedded target (Days 2-4 of the assignment).

Set it via an environment variable so you never have to edit feature/step
files when switching targets:

    export BASE_URL="http://localhost:8080"      # QEMU-forwarded port
    export BASE_URL="http://192.168.1.50"        # real hardware
"""

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = os.environ.get("BASE_URL", "https://tutorialsninja.com/demo/")
HEADLESS = os.environ.get("HEADLESS", "false").lower() == "true"


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
    context.driver.implicitly_wait(5)


def before_scenario(context, scenario):
    context.driver.delete_all_cookies()


def after_all(context):
    context.driver.quit()
