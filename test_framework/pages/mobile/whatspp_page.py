from locators.mobile.whatsapp_locator import WhatsAppLocators
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshot_helper import take_screenshot
import time


class WhatsAppPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, 15)

    # ─────────────────────────────────────
    # Tab Actions
    # ─────────────────────────────────────
    def click_updates_tab(self):
        time.sleep(3)
        try:
            element = self.wait.until(
                EC.element_to_be_clickable(WhatsAppLocators.UPDATES_TAB)
            )
            element.click()
            take_screenshot(self.driver, "Updates_Tab_Clicked")
            print("✅ Clicked Updates tab!")
        except Exception as e:
            take_screenshot(self.driver, "Updates_Tab_FAILED")
            raise e

    def click_calls_tab(self):
        time.sleep(2)
        try:
            element = self.wait.until(
                EC.element_to_be_clickable(WhatsAppLocators.CALLS_TAB)
            )
            element.click()
            take_screenshot(self.driver, "Calls_Tab_Clicked")
            print("✅ Clicked Calls tab!")
        except Exception as e:
            take_screenshot(self.driver, "Calls_Tab_FAILED")
            raise e

    # ─────────────────────────────────────
    # Verify Tabs
    # ─────────────────────────────────────
    def is_updates_opened(self):
        return "Updates" in self.driver.page_source

    def is_calls_opened(self):
        return "Calls" in self.driver.page_source

    # ─────────────────────────────────────
    # Search Contact in Chats
    # ─────────────────────────────────────
    def search_contact(self, contact_name):
        try:
            # First go back to Chats tab
            time.sleep(2)
            chats_tab = self.driver.find_element(
                AppiumBy.XPATH,
                "//android.widget.FrameLayout[@content-desc='Chats']"
            )
            chats_tab.click()
            time.sleep(2)
            print("✅ Clicked Chats tab!")

            # Now click search bar
            search_bar = self.wait.until(
                EC.element_to_be_clickable(WhatsAppLocators.SEARCH_BAR)
            )
            search_bar.click()
            time.sleep(1)

            # Type contact name
            search_input = self.wait.until(
                EC.presence_of_element_located(WhatsAppLocators.SEARCH_INPUT)
            )
            search_input.send_keys(contact_name)
            time.sleep(2)
            take_screenshot(self.driver, f"Searched_{contact_name}")
            print(f"✅ Searched for: {contact_name}")

        except Exception as e:
            take_screenshot(self.driver, "Search_FAILED")
            raise e

    def open_contact(self, contact_name):
        try:
            contact_locator = (
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().text("{contact_name}")'
            )
            contact = self.wait.until(
                EC.element_to_be_clickable(contact_locator)
            )
            contact.click()
            time.sleep(2)
            take_screenshot(self.driver, f"Opened_chat_{contact_name}")
            print(f"✅ Opened chat with: {contact_name}")

        except Exception as e:
            take_screenshot(self.driver, "Open_Contact_FAILED")
            raise e

    # ─────────────────────────────────────
    # Send Message
    # ─────────────────────────────────────
    def get_message_input(self):
        locators = [
            WhatsAppLocators.MESSAGE_INPUT,
            WhatsAppLocators.MESSAGE_INPUT_2,
            WhatsAppLocators.MESSAGE_INPUT_3,
            WhatsAppLocators.MESSAGE_INPUT_4,
        ]
        for locator in locators:
            try:
                element = self.wait.until(
                    EC.element_to_be_clickable(locator)
                )
                print(f"✅ Found message input using: {locator}")
                return element
            except Exception:
                continue
        raise Exception("❌ Could not find message input box!")

    def send_message(self, message):
        try:
            msg_input = self.get_message_input()
            msg_input.click()
            time.sleep(1)
            msg_input.send_keys(message)
            time.sleep(1)

            send_btn = self.wait.until(
                EC.element_to_be_clickable(WhatsAppLocators.SEND_BUTTON)
            )
            send_btn.click()
            time.sleep(1)
            take_screenshot(self.driver, "Message_Sent")
            print("✅ Message sent!")

        except Exception as e:
            take_screenshot(self.driver, "Send_Message_FAILED")
            raise e

    def is_message_sent(self, message):
        return message in self.driver.page_source

    # ─────────────────────────────────────
    # Status Actions
    # ─────────────────────────────────────
    def search_status(self, status_name):
        try:
            # Wait for screen to settle
            time.sleep(3)

            # Find search icon freshly to avoid stale element
            search_icon = self.driver.find_element(
                AppiumBy.XPATH,
                "//android.widget.ImageButton[@content-desc='Search']"
            )
            search_icon.click()
            time.sleep(2)
            print("✅ Clicked Search icon in Updates!")

            # Type name in search input
            search_input = self.wait.until(
                EC.presence_of_element_located(WhatsAppLocators.SEARCH_INPUT)
            )
            search_input.send_keys(status_name)
            time.sleep(2)
            take_screenshot(self.driver, f"Searched_status_{status_name}")
            print(f"✅ Searched status for: {status_name}")

        except Exception as e:
            take_screenshot(self.driver, "Search_Status_FAILED")
            raise e

    def open_status(self, status_name):
        try:
            status_locator = (
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().text("{status_name}")'
            )
            status = self.wait.until(
                EC.element_to_be_clickable(status_locator)
            )
            status.click()
            time.sleep(2)
            take_screenshot(self.driver, f"Opened_status_{status_name}")
            print(f"✅ Opened status of: {status_name}")

        except Exception as e:
            take_screenshot(self.driver, "Open_Status_FAILED")
            raise e

    def is_status_visible(self, status_name):
        return status_name in self.driver.page_source