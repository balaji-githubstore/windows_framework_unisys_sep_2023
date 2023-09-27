import time

from appium.webdriver.common.appiumby import AppiumBy

from base.windows_keywords import WindowsKeywords


class HomePage(WindowsKeywords):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.__sign_in_locator=(AppiumBy.NAME, 'Sign In')
        self.__sign_up_locator = (AppiumBy.NAME, 'Sign Up')
        self.__join_meeting_locator = (AppiumBy.NAME, 'Join a Meeting')


    def click_on_sign_in(self):
        super().wait_and_click(self.__sign_in_locator)

    def click_on_sign_up(self):
        super().wait_and_click(self.__sign_up_locator)

    def click_on_join_meeting(self):
        super().wait_and_click(self.__join_meeting_locator)
