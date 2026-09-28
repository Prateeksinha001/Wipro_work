*** Settings ***
Documentation      Section 5: Test Setup and Teardown
...                Section 6: Tags and Test Execution
Library            SeleniumLibrary
Resource           ../resources/common.robot
Test Setup         Open Application And Login
Test Teardown      Logout And Close

*** Test Cases ***
Verify Dashboard After Login
    [Documentation]    Test Setup already opened the browser and logged in;
    ...                this test just verifies we landed on the account page.
    [Tags]    smoke    login
    Location Should Contain    route=account/account
    Log    Reached My Account page successfully    console=True

Verify Account Page Has Edit Account Link
    [Documentation]    Another test reusing the same Test Setup/Teardown
    ...                automatically - no duplicated login/logout code.
    [Tags]    regression    login
    Page Should Contain Element    link:Edit Account
    Log    Account page contains the Edit Account link    console=True
