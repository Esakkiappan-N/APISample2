import pytest
import allure
from core.driver import get_driver
from pages.mobile.whatspp_page import WhatsAppPage
from utils.csv_reader import get_test_data, get_status_data


# ─────────────────────────────────
# Read data from CSV files
# ─────────────────────────────────
send_message_data = get_test_data("whatsapp_data.csv")
status_data       = get_status_data("whatsappstatus_data.csv")


# ─────────────────────────────────
# Test 1 - Open Updates Tab
# ─────────────────────────────────
@allure.epic("WhatsApp Automation")
@allure.feature("Navigation")
@allure.story("Updates Tab")
@allure.severity(allure.severity_level.NORMAL)
def test_open_updates():
    with allure.step("Launch WhatsApp"):
        driver = get_driver()
        page = WhatsAppPage(driver)

    with allure.step("Click Updates Tab"):
        page.click_updates_tab()

    with allure.step("Verify Updates Tab is Opened"):
        assert page.is_updates_opened()

    driver.quit()


# ─────────────────────────────────
# Test 2 - Open Calls Tab
# ─────────────────────────────────
@allure.epic("WhatsApp Automation")
@allure.feature("Navigation")
@allure.story("Calls Tab")
@allure.severity(allure.severity_level.NORMAL)
def test_open_calls():
    with allure.step("Launch WhatsApp"):
        driver = get_driver()
        page = WhatsAppPage(driver)

    with allure.step("Click Calls Tab"):
        page.click_calls_tab()

    with allure.step("Verify Calls Tab is Opened"):
        assert page.is_calls_opened()

    driver.quit()


# ─────────────────────────────────
# Test 3 - Send Message
# ─────────────────────────────────
@allure.epic("WhatsApp Automation")
@allure.feature("Messaging")
@allure.story("Send Message")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("contact_name, message", send_message_data)
def test_send_message(contact_name, message):
    with allure.step("Launch WhatsApp"):
        driver = get_driver()
        page = WhatsAppPage(driver)

    with allure.step(f"Search Contact: {contact_name}"):
        page.search_contact(contact_name)

    with allure.step(f"Open Chat with {contact_name}"):
        page.open_contact(contact_name)

    with allure.step(f"Send Message: {message}"):
        page.send_message(message)

    with allure.step("Verify Message is Sent"):
        assert page.is_message_sent(message)

    driver.quit()


# ─────────────────────────────────
# Test 4 - View Status
# ─────────────────────────────────
@allure.epic("WhatsApp Automation")
@allure.feature("Status")
@allure.story("View Status")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("status_name", status_data)
def test_view_status(status_name):
    with allure.step("Launch WhatsApp"):
        driver = get_driver()
        page = WhatsAppPage(driver)

    with allure.step("Click Updates Tab"):
        page.click_updates_tab()

    with allure.step(f"Search Status: {status_name}"):
        page.search_status(status_name)

    with allure.step(f"Open Status of: {status_name}"):
        page.open_status(status_name)

    with allure.step("Verify Status is Visible"):
        assert page.is_status_visible(status_name)

    driver.quit()