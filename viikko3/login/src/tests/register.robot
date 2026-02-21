*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle0
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  kalle1
    Set Password  ka
    Set Password Confirmation  ka
    Click Button  Register
    Register Should Fail With Message  Password too short

Register With Valid Username And Invalid Password
    Set Username  kalle2
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Click Button  Register
    Register Should Fail With Message  Password must contain at least one number or special character

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle3
    Set Password  kalle123
    Set Password Confirmation  kalle456
    Click Button  Register
    Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Register Should Fail With Message  Username already exists

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To  ${REGISTER_URL}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Welcome Page Should Be Open
    Title Should Be  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}