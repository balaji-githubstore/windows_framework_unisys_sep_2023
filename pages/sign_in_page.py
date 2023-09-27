import time

from appium.webdriver.common.appiumby import AppiumBy


class SignInPage:
    def __init__(self,driver):
        self.driver=driver

    def enter_username(self,username):
        self.driver.find_element(AppiumBy.XPATH, "//Edit[@Name='Enter your email']").send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(AppiumBy.XPATH, "//Edit[@Name='Enter your password']").click()
        self.driver.find_element(AppiumBy.XPATH, "//Edit[@Name='Enter your password']").send_keys(password)

    def click_on_login(self):
        self.driver.find_element(AppiumBy.XPATH, '//Button[@Name="Sign In"]').click()

    def get_error_message(self):
        time.sleep(10)
        return (self.driver.find_element(AppiumBy.XPATH, "//*[contains(@Name,'Incorrect')]")
                        .get_attribute("Name"))


