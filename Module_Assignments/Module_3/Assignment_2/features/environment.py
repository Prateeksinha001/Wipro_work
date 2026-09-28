"""
Behave environment hooks for API automation.

context.base_url and context.session are set up once, before all tests,
so every step definition reuses the same connection/headers instead of
creating a new requests.Session() per step.
"""

import os
import requests

BASE_URL = os.environ.get("BASE_URL", "https://reqres.in/api")


def before_all(context):
    context.base_url = BASE_URL
    context.session = requests.Session()
    context.session.headers.update({"Content-Type": "application/json"})


def before_scenario(context, scenario):
    context.response = None


def after_all(context):
    context.session.close()
