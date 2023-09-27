import pytest
from appium import webdriver
from appium.options.windows import WindowsOptions
from assertpy import assert_that
from base.appium_wrapper import AutomationWrapper


class TestHomeScreenUI(AutomationWrapper):
    def test_validate_version(self):
        assert_that(self.driver.page_source).contains("5.16.1")
