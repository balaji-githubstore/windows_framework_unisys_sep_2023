import pytest
from appium import webdriver
from appium.options.windows import WindowsOptions


class AutomationWrapper:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        option = WindowsOptions()
        option.app = r'C:\Users\Balaji_Dinakaran\AppData\Roaming\Zoom\bin\Zoom.exe'
        self.driver = webdriver.Remote(command_executor='http://localhost:4723/wd/hub', options=option)
        self.driver.implicitly_wait(20)
        yield
        self.driver.quit()
