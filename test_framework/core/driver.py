from appium import webdriver
from selenium.webdriver.common.options import ArgOptions


def get_driver():
    options = ArgOptions()
    options.set_capability("platformName", "Android")
    options.set_capability("platformVersion", "15")
    options.set_capability("deviceName", "0020965BT005049")
    options.set_capability("automationName", "UiAutomator2")
    options.set_capability("appPackage", "com.whatsapp")
    options.set_capability("appActivity", "com.whatsapp.HomeActivity")
    options.set_capability("noReset", True)

    driver = webdriver.Remote(
        "http://127.0.0.1:4723/wd/hub", options=options)  # ← /wd/hub for v1
    return driver
