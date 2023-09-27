import time

import assertpy
import pytest
from appium import webdriver
from appium.options.windows import WindowsOptions
from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that

from base.asppium_wrapper import AutomationWrapper
from pages.home_page import HomePage
from pages.sign_in_page import SignInPage
from utilities.data_source import DataSource


class TestLogin(AutomationWrapper):

    @pytest.mark.login
    @pytest.mark.parametrize("username,password,expected_error",
                             DataSource.test_invalid_login)
    def test_invalid_login(self,username,password,expected_error):

        home_page=HomePage(self.driver)
        home_page.click_on_sign_in()

        sign_in_page=SignInPage(self.driver)
        sign_in_page.enter_username(username)
        sign_in_page.enter_password(password)
        sign_in_page.click_on_login()

        actual_error = sign_in_page.get_error_message()
        assert_that(actual_error).is_equal_to(expected_error)

    @pytest.mark.smoke
    @pytest.mark.login
    @pytest.mark.parametrize("username,password,expected_value",
                             DataSource.test_invalid_login)
    def test_valid_login(self,username,password,expected_value):
        home_page = HomePage(self.driver)
        home_page.click_on_sign_in()

        sign_in_page = SignInPage(self.driver)
        sign_in_page.enter_username(username)
        sign_in_page.enter_password(password)
        sign_in_page.click_on_login()

        #assert the dashboard page any content


