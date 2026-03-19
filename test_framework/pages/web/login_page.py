import allure
from playwright.sync_api import Page
from locators.web.login_locators import LoginLocators


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Navigate to URL: {url}")
    def navigate(self, url):
        self.page.goto(url)

    @allure.step("Login with username: {username}")
    def login(self, username, password):
        self.page.wait_for_selector(LoginLocators.USERNAME, timeout=15000)
        self.page.locator(LoginLocators.USERNAME).fill(username)
        self.page.locator(LoginLocators.PASSWORD).fill(password)
        screenshot = self.page.screenshot()
        allure.attach(screenshot, name="Before Login", attachment_type=allure.attachment_type.PNG)
        self.page.locator(LoginLocators.LOGIN_BTN).click()

    @allure.step("Capture toaster message")
    def get_toaster_message(self):
        self.page.wait_for_selector(LoginLocators.TOASTER)
        msg = self.page.locator(LoginLocators.TOASTER).inner_text()

        allure.attach(msg, name="Toaster Message", attachment_type=allure.attachment_type.TEXT)
        return msg

    @allure.step("Capture dashboard message")
    def get_dashboard_message(self):
        self.page.wait_for_selector(LoginLocators.DASHBOARD_MSG)
        msg = self.page.locator(LoginLocators.DASHBOARD_MSG).inner_text()

        allure.attach(msg, name="Dashboard Message", attachment_type=allure.attachment_type.TEXT)
        return msg

    @allure.step("Login with username: {username}")
    def login(self, username, password):
        self.page.wait_for_load_state("networkidle")
        username_field = self.page.locator("input[placeholder='Username'], input[name='username']")
        username_field.wait_for(state="visible", timeout=20000)
        username_field.fill(username)
        password_field = self.page.locator("input[placeholder='Password'], input[type='password']")
        password_field.fill(password)
        screenshot = self.page.screenshot()
        allure.attach(screenshot, name="Before Login", attachment_type=allure.attachment_type.PNG)
        self.page.locator("button:has-text('Login')").click()