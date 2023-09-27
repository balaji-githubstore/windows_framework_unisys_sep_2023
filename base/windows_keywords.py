from typing import Tuple

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class WindowsKeywords:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def wait_and_click(self, locator: Tuple[str, str]):
        self.wait.until(expected_conditions.visibility_of_element_located(locator)).click()

    def wait_and_type(self, locator: Tuple[str, str], text):
        self.wait.until(expected_conditions.visibility_of_element_located(locator)).send_keys(text)

    def get_name_attribute_value(self, locator: Tuple[str, str]):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator)).get_attribute("Name")

    # all the windows keywords we can create in this place