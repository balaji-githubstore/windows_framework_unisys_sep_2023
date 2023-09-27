import time

from appium.webdriver.common.appiumby import AppiumBy


class HomePage:

    def __init__(self,driver):
        self.driver=driver

    def click_on_sign_in(self):
        time.sleep(3)
        self.driver.find_element(AppiumBy.NAME, 'Sign In').click()

    def click_on_sign_up(self):
        self.driver.find_element(AppiumBy.NAME, 'Sign Up').click()

    def click_on_join_meeting(self):
        self.driver.find_element(AppiumBy.NAME, 'Join a Meeting').click()
