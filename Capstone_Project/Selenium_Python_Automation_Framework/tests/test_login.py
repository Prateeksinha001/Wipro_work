import pytest

from pages.login_page import LoginPage


@pytest.mark.login
def test_valid_login(driver):
    login_page = LoginPage(driver)

    login_page.open_login_page()
    login_page.login(
        "test@example.com",
        "Test@123"
    )

    assert "My Account" in driver.title or "Account" in driver.title


@pytest.mark.login
def test_invalid_login(driver):
    login_page = LoginPage(driver)

    login_page.open_login_page()
    login_page.login(
        "invalid@example.com",
        "WrongPassword123"
    )

    message = login_page.get_warning_message()

    assert message is not None