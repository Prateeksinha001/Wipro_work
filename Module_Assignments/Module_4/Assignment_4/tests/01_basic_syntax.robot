*** Settings ***
Documentation    Section 1: Basic Syntax and Keywords
Library          SeleniumLibrary
Resource         ../resources/common.robot
Suite Teardown   Close All Browsers

*** Test Cases ***
Open Browser And Navigate To A Specific URL
    [Documentation]    Opens a browser and navigates to the login page URL.
    [Tags]    basic-syntax
    Open Browser    ${BASE_URL}    ${BROWSER}
    Title Should Be    Account Login
    [Teardown]    Close Browser

Fill In A Form Field Using Input Text
    [Documentation]    Demonstrates the "Input Text" keyword filling a form field.
    [Tags]    basic-syntax
    Open Browser    ${BASE_URL}    ${BROWSER}
    Input Text    id:input-email    testuser@example.com
    [Teardown]    Close Browser

Verify Presence Of A Specific Element
    [Documentation]    Demonstrates "Page Should Contain Element" to confirm
    ...                an element exists on the page.
    [Tags]    basic-syntax
    Open Browser    ${BASE_URL}    ${BROWSER}
    Page Should Contain Element    id:input-password
    [Teardown]    Close Browser
