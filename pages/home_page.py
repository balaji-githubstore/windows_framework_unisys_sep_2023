import time

from appium.webdriver.common.appiumby import AppiumBy

from base.windows_keywords import WindowsKeywords


class HomePage(WindowsKeywords):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def click_on_sign_in(self):
        super().wait_and_click((AppiumBy.NAME, 'Sign In'))

    def click_on_sign_up(self):
        super().wait_and_click((AppiumBy.NAME, 'Sign Up'))

    def click_on_join_meeting(self):
        super().wait_and_click((AppiumBy.NAME, 'Join a Meeting'))
