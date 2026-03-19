from appium.webdriver.common.appiumby import AppiumBy

class WhatsAppLocators:
    UPDATES_TAB = (AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='Updates']")
    CALLS_TAB = (AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='Calls']")
    CHATS_TAB = (AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='Chats']")
    SEARCH_BAR = (AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='Ask Meta AI or Search']")
    
    UPDATES_SEARCH_ICON = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Search']")
    SEARCH_INPUT = (AppiumBy.XPATH, "//android.widget.EditText")
    MESSAGE_INPUT   = (AppiumBy.XPATH, "//android.widget.EditText[@text='Message']")
    MESSAGE_INPUT_2 = (AppiumBy.XPATH, "//android.widget.EditText[@hint='Message']")
    MESSAGE_INPUT_3 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Message")')
    MESSAGE_INPUT_4 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')

    SEND_BUTTON = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Send']")