*** Settings ***
Documentation    Section 4: Assertions and Verification
Library          SeleniumLibrary
Library          RequestsLibrary
Resource         ../resources/common.robot

*** Test Cases ***
Perform Action Then Assert Expected Outcome
    [Documentation]    Performs an action (loading the page) and asserts the
    ...                expected result (the page title) matches reality.
    [Tags]    assertions
    Open Browser    ${BASE_URL}    ${BROWSER}
    ${title}=    Get Title
    Should Be Equal As Strings    ${title}    Account Login
    [Teardown]    Close Browser

Verify API Response Using Should Be Equal As Strings
    [Documentation]    Calls a public test API (reqres.in) and checks a
    ...                field in the JSON response using
    ...                "Should Be Equal As Strings".
    [Tags]    assertions    api
    Create Session    reqres    https://reqres.in
    ${response}=      GET On Session    reqres    /api/users/2
    Should Be Equal As Strings    ${response.status_code}    200
    ${first_name}=    Set Variable    ${response.json()}[data][first_name]
    Should Be Equal As Strings    ${first_name}    Janet
