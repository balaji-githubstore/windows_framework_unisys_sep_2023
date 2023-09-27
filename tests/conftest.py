import pytest
from appium.webdriver.appium_service import AppiumService

""" APPIUM SERVER START AND STOPS ONLY ONCE AT SESSION LEVEL"""


@pytest.fixture(scope="session", autouse=True)
def init():
    service = AppiumService()
    service.start(args=['-p', '7878', '-a', '127.0.0.1', "--base-path", '/wd/hub'])
    print(service.is_running)
    yield
    service.stop()
