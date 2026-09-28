from behave import given, when, then
from selenium.webdriver.common.by import By


@given("the user is on the login page")
def step_open_login_page(context):
    context.driver.get(f"{context.base_url}/index.php?route=account/login")


@when('the user enters username "{username}" and password "{password}"')
def step_enter_credentials(context, username, password):
    context.driver.find_element(By.ID, "input-email").send_keys(username)
    context.driver.find_element(By.ID, "input-password").send_keys(password)


@when("the user clicks the login button")
def step_click_login(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()


@then("the user should see the dashboard page")
def step_verify_dashboard(context):
    assert "dashboard" in context.driver.current_url, (
        f"Expected to land on dashboard, got: {context.driver.current_url}"
    )


@then('the user should see an error message "{message}"')
def step_verify_error(context, message):
    error_el = context.driver.find_element(By.CSS_SELECTOR, ".alert.alert-danger.alert-dismissible")
    assert message in error_el.text, (
        f"Expected error '{message}', got '{error_el.text}'"
    )
