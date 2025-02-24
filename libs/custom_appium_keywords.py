from appium import webdriver
from robot.api.deco import keyword
import appium.webdriver.common.mobileby
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CustomAppiumLibrary:
    def __init__(self, driver=None):
        self.driver = driver

    @keyword
    def start_application(self, app_path="resources/apk/app-release.apk", platform_name="Android", device_name="1110025415008874", platform_version="14.0"):
        desired_caps = {
            "platformName": platform_name,
            "platformVersion": platform_version,
            "deviceName": device_name,
            "app": app_path,
            "automationName": "UiAutomator2"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        return self.driver

    @keyword
    def stop_application(self):
        if self.driver:
            self.driver.quit()

    # @keyword
    # def click_element(self, locator):
    #     element = self.driver.find_element(MobileBy.XPATH, locator)
    #     element.click()
    #
    # @keyword
    # def input_text(self, locator, text):
    #     element = self.driver.find_element(MobileBy.XPATH, locator)
    #     element.send_keys(text)
    #
    # @keyword
    # def wait_for_element(self, locator, timeout=30):
    #     WebDriverWait(self.driver, timeout).until(
    #         EC.presence_of_element_located((MobileBy.XPATH, locator))
    #     )
