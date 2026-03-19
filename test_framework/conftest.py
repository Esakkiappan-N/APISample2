import pytest
from playwright.sync_api import sync_playwright
from core.driver import get_driver
from locators.web.variables import BASE_URL
from pages.api.login_api import login_api, get_token    # ← fixed
from utils.csv_reader import read_csv
import os

# ─────────────────────────────────────────
# Mobile Fixture
# ─────────────────────────────────────────


@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


# ─────────────────────────────────────────
# API Fixture
# ─────────────────────────────────────────
@pytest.fixture(scope="session")
def auth_token():
    users = read_csv("testdata/api/test_data.csv")
    user = users[0]
    response = login_api(user["username"], user["password"])
    token = get_token(response)
    assert token is not None, "Login failed in session fixture"
    return token


# ─────────────────────────────────────────
# Web Fixture
# ─────────────────────────────────────────
@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu"
            ]
        )

        # ✅ Correct indentation
        context = browser.new_context()
        page = context.new_page()

        yield page

        browser.close()
