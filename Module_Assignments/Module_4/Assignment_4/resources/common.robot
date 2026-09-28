*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BASE_URL}          https://tutorialsninja.com/demo/index.php?route=account/login
${LOGOUT_URL}        https://tutorialsninja.com/demo/index.php?route=account/logout
${BROWSER}           chrome
${VALID_USERNAME}    you@example.com
${VALID_PASSWORD}    YourPass123

*** Keywords ***
Open Application And Login
    [Documentation]    Suite/Test Setup keyword: opens the browser and logs in.
    ...                Reused by any test suite that needs an already-logged-in session.
    Open Browser    ${BASE_URL}    ${BROWSER}
    Input Text      id:input-email       ${VALID_USERNAME}
    Input Password  id:input-password    ${VALID_PASSWORD}
    Click Button    css:input[value='Login']

Logout And Close
    [Documentation]    Test/Suite Teardown keyword: logs out and closes the browser.
    Go To    ${LOGOUT_URL}
    Close Browser
