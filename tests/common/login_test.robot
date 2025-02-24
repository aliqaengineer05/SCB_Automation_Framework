*** Settings ***
Library    AppiumLibrary
Library    ../keywords/login_keywords.py
Library    RobotframeworkAllure    # Add allure library

*** Variables ***
${APP_PATH}           resources\apk\app-release.apk
${DEVICE_NAME}        1110025415008874
${PLATFORM_VERSION}   14.0

# Locators (should be replaced with actual locators from the app)
${USERNAME}           validusername
${PASSWORD}           validpassword
${INVALID_USERNAME}   invalidusername
${INVALID_PASSWORD}   invalidpassword
${ERROR_MESSAGE}      Please enter a valid username and password.

*** Test Cases ***

Login Test
    [Documentation]    This is the valid login test
    [Allure.label]      category    login
    [Allure.feature]    Login Functionality
    [Allure.severity]   critical
    [Allure.priority]   high
    Open Application    ${APP_PATH}    ${DEVICE_NAME}    ${PLATFORM_VERSION}
    Sleep    2
    Close Application

Invalid Login Test - Empty Username
    [Documentation]    Test for empty username in login form
    [Allure.label]      category    invalid_login
    [Allure.feature]    Login Functionality
    [Allure.severity]   major
    [Allure.priority]   high
    Open Application    ${APP_PATH}    ${DEVICE_NAME}    ${PLATFORM_VERSION}
    Enter Username    ""
    Enter Password    ${PASSWORD}
    Click Login Button
    ${error_message}=    Get Error Message
    Should Contain    ${error_message}    Username is required
    Close Application

Invalid Login Test - Empty Password
    [Documentation]    Test for empty password in login form
    [Allure.label]      category    invalid_login
    [Allure.feature]    Login Functionality
    [Allure.severity]   major
    [Allure.priority]   high
    Open Application    ${APP_PATH}    ${DEVICE_NAME}    ${PLATFORM_VERSION}
    Enter Username    ${USERNAME}
    Enter Password    ""
    Click Login Button
    ${error_message}=    Get Error Message
    Should Contain    ${error_message}    Password is required
    Close Application

Invalid Login Test - Invalid Credentials
    [Documentation]    Test for invalid login credentials
    [Allure.label]      category    invalid_login
    [Allure.feature]    Login Functionality
    [Allure.severity]   blocker
    [Allure.priority]   high
    Open Application    ${APP_PATH}    ${DEVICE_NAME}    ${PLATFORM_VERSION}
    Enter Username    ${INVALID_USERNAME}
    Enter Password    ${INVALID_PASSWORD}
    Click Login Button
    ${error_message}=    Get Error Message
    Should Contain    ${error_message}    Invalid username or password
    Close Application
