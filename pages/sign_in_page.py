import time

from appium.webdriver.common.appiumby import AppiumBy

from base.windows_keywords import WindowsKeywords


class SignInPage(WindowsKeywords):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.__username_locator=(AppiumBy.XPATH, "//Edit[@Name='Enter your email']")
        self.__password_locator=(AppiumBy.XPATH, "//Edit[@Name='Enter your password']")
        self.__login_locator=(AppiumBy.XPATH, '//Button[@Name="Sign In"]')
        self.__error_locator=(AppiumBy.XPATH, "//*[contains(@Name,'Incorrect')]")

    def enter_username(self,username):
        super().wait_and_type(self.__username_locator,username)

    def enter_password(self,password):
        super().wait_and_click(self.__password_locator)
        super().wait_and_type(self.__password_locator,password)

    def click_on_login(self):
        super().wait_and_click(self.__login_locator)

    def get_error_message(self):
        return super().get_name_attribute_value(self.__error_locator)


