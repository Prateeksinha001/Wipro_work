*** Settings ***
Documentation    Section 2: Variables and Data-Driven Automation
Library          SeleniumLibrary
Library          ../libraries/CustomLibrary.py
Resource         ../resources/common.robot
Suite Teardown   Close All Browsers

*** Variables ***
${USERNAME}    you@example.com
${PASSWORD}    YourPass123

*** Test Cases ***
Login Using Variables
    [Documentation]    Stores username/password in variables instead of
    ...                hardcoding them inline in the test steps.
    [Tags]    data-driven
    Open Browser     ${BASE_URL}    ${BROWSER}
    Input Text       id:input-email       ${USERNAME}
    Input Password   id:input-password    ${PASSWORD}
    Click Button     css:input[value='Login']
    [Teardown]    Close Browser

Data Driven Login From External CSV File
    [Documentation]    Reads test data from testdata/login_data.csv via our
    ...                custom keyword, and repeats the same login steps
    ...                once per row in the file.
    [Tags]    data-driven
    ${data}=    Get Test Data From Csv    testdata/login_data.csv
    FOR    ${row}    IN    @{data}
        Log    Trying login with: ${row}[email]    console=True
        Open Browser     ${BASE_URL}    ${BROWSER}
        Input Text       id:input-email       ${row}[email]
        Input Password   id:input-password    ${row}[password]
        Click Button     css:input[value='Login']
        Close Browser
    END
