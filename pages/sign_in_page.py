import time

from appium.webdriver.common.appiumby import AppiumBy

from base.windows_keywords import WindowsKeywords


class SignInPage(WindowsKeywords):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def enter_username(self,username):
        super().wait_and_type((AppiumBy.XPATH, "//Edit[@Name='Enter your email']"),username)

    def enter_password(self,password):
        super().wait_and_click((AppiumBy.XPATH, "//Edit[@Name='Enter your password']"))
        super().wait_and_type((AppiumBy.XPATH, "//Edit[@Name='Enter your password']"),password)



    def click_on_login(self):
        super().wait_and_click((AppiumBy.XPATH, '//Button[@Name="Sign In"]'))

    def get_error_message(self):
        return super().get_name_attribute_value((AppiumBy.XPATH, "//*[contains(@Name,'Incorrect')]"))


