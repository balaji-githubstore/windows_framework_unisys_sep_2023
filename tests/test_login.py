import time

import assertpy
import pytest
from appium import webdriver
from appium.options.windows import WindowsOptions
from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that

from base.appium_wrapper import AutomationWrapper


class TestLogin(AutomationWrapper):

    def test_invalid_login(self):
        time.sleep(3)
        self.driver.find_element(AppiumBy.NAME, 'Sign In').click()
        self.driver.find_element(AppiumBy.XPATH, "//Edit[@Name='Enter your email']").send_keys("hello12345678@gmail.com")
        self.driver.find_element(AppiumBy.XPATH, "//Edit[@Name='Enter your password']").click()
        self.driver.find_element(AppiumBy.XPATH, "//Edit[@Name='Enter your password']").send_keys("hello123")
        self.driver.find_element(AppiumBy.XPATH, '//Button[@Name="Sign In"]').click()
        time.sleep(10)
        actual_error = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@Name,'Incorrect')]").get_attribute("Name")
        assert_that(actual_error).is_equal_to("Incorrect email or password")

    def test_valid_login(self):
        self.driver.find_element(AppiumBy.NAME, 'Sign In').click()

