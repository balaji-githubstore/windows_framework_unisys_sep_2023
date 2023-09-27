import time

import assertpy
import pytest
from appium import webdriver
from appium.options.windows import WindowsOptions
from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that

from base.appium_wrapper import AutomationWrapper


class TestLogin(AutomationWrapper):

    @pytest.mark.parametrize("username,password,expected_error",[
        ('john123@gmail.com','john123','Incorrect email or password'),
        ('pete123@gmail.com', 'pete123', 'Incorrect email or password')
    ])
    def test_invalid_login(self,username,password,expected_error):
        time.sleep(3)
        self.driver.find_element(AppiumBy.NAME, 'Sign In').click()
        self.driver.find_element(AppiumBy.XPATH, "//Edit[@Name='Enter your email']").send_keys(username)
        self.driver.find_element(AppiumBy.XPATH, "//Edit[@Name='Enter your password']").click()
        self.driver.find_element(AppiumBy.XPATH, "//Edit[@Name='Enter your password']").send_keys(password)
        self.driver.find_element(AppiumBy.XPATH, '//Button[@Name="Sign In"]').click()
        time.sleep(10)
        actual_error = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@Name,'Incorrect')]").get_attribute("Name")
        assert_that(actual_error).is_equal_to(expected_error)

    def test_valid_login(self):
        self.driver.find_element(AppiumBy.NAME, 'Sign In').click()

