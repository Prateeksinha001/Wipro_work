*** Settings ***
Documentation    Section 3: Custom Keywords and Libraries
Library          ../libraries/CustomLibrary.py
Library          BuiltIn

*** Test Cases ***
Use Custom Keyword To Add Two Numbers
    [Documentation]    Calls our own custom Python keyword, defined in
    ...                libraries/CustomLibrary.py.
    [Tags]    custom-keyword
    ${result}=    Add Two Numbers    5    7
    Should Be Equal As Numbers    ${result}    12

Manipulate Strings And Numbers Using BuiltIn
    [Documentation]    Uses Robot Framework's own BuiltIn library (always
    ...                available, no install needed) for string/math work.
    [Tags]    custom-keyword
    ${combined}=    Catenate    Hello    Robot    Framework
    Should Be Equal As Strings    ${combined}    Hello Robot Framework

    ${sum}=    Evaluate    10 + 25
    Should Be Equal As Integers    ${sum}    35

    ${upper}=    Convert To Upper Case    robot framework
    Should Be Equal As Strings    ${upper}    ROBOT FRAMEWORK
