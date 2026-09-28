from behave import given, when, then


@given("the user is on the login page")
def step_open_login_page(context):
    context.login_page.open(context.base_url)


@when('the user logs in with username "{username}" and password "{password}"')
def step_login(context, username, password):
    context.login_page.login(username, password)


@then('the login result should be "{expected_result}"')
def step_verify_result(context, expected_result):
    if expected_result == "success":
        assert context.dashboard_page.is_loaded(), (
            f"Expected dashboard, got URL: {context.dashboard_page.current_url()}"
        )
    else:
        error = context.login_page.get_error_message()
        assert error is not None, "Expected a login error message, but none appeared"
