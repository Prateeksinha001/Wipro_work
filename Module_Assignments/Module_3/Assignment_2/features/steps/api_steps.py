import json
import os

from behave import given, when, then


@given('the API endpoint "{endpoint}"')
def step_set_endpoint(context, endpoint):
    context.endpoint = endpoint


@when('the user sends a POST request with name "{name}" and job "{job}"')
def step_post_user(context, name, job):
    url = f"{context.base_url}{context.endpoint}"
    payload = {"name": name, "job": job}
    context.response = context.session.post(url, json=payload)


@then("the response status code should be {status_code:d}")
def step_check_status(context, status_code):
    assert context.response.status_code == status_code, (
        f"Expected {status_code}, got {context.response.status_code}: "
        f"{context.response.text}"
    )


@then('the response should contain name "{name}"')
def step_check_body_name(context, name):
    body = context.response.json()
    assert body.get("name") == name, f"Expected name '{name}', got {body}"


# ---- External JSON data-driven approach ----

@when('the user creates all users defined in "{filepath}"')
def step_post_users_from_file(context, filepath):
    repo_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    full_path = os.path.join(repo_root, filepath)

    with open(full_path, "r") as f:
        test_data = json.load(f)

    context.data_driven_results = []
    url = f"{context.base_url}{context.endpoint}"

    for row in test_data:
        payload = {"name": row["name"], "job": row["job"]}
        response = context.session.post(url, json=payload)
        context.data_driven_results.append(
            {
                "expected_status": row["expected_status"],
                "actual_status": response.status_code,
                "name": row["name"],
            }
        )


@then("every response status code should match the expected value")
def step_verify_all_results(context):
    failures = [
        r for r in context.data_driven_results
        if r["actual_status"] != r["expected_status"]
    ]
    assert not failures, f"Mismatched results: {failures}"
