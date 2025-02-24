# from robot.api.deco import keyword
# from appium import webdriver
# import sys
# print(sys.path)
#
# @keyword
# def open_application(app_path, device_name, platform_version):
#     desired_caps = {
#         "platformName": "Android",
#         "platformVersion": platform_version,
#         "deviceName": device_name,
#         "app": app_path,
#         "automationName": "UiAutomator2",
#         "newCommandTimeout": 300,
#         "noReset": True
#     }
#     driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
#     return driver
from robot.api.deco import keyword
from appium import webdriver
import time


@keyword
def open_application(app_path, device_name, platform_version):
    desired_caps = {
        "platformName": "Android",
        "platformVersion": platform_version,
        "deviceName": device_name,
        "app": app_path,
        "automationName": "UiAutomator2",
        "newCommandTimeout": 300,
        "noReset": True
    }

    print(f"Starting WebDriver with capabilities: {desired_caps}")  # Debug print
    try:
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        if driver is None:
            print("WebDriver returned None")
        else:
            print(f"WebDriver started successfully: {driver}")
    except Exception as e:
        print(f"Error initializing WebDriver: {e}")
        driver = None

    return driver
