import allure
from pages.web.login_page import LoginPage
from utils.csv_data_joiner import read_test_data


@allure.feature("Login")
@allure.story("Valid Login")

def test_valid_login(page):
    data = read_test_data("reg_login")

    login_page = LoginPage(page)
    login_page.login(data["usernamevalue"], data["passwordvalue"])

    actual = login_page.get_dashboard_message()

    assert data["expectedresult"] in actual

@allure.feature("Login")
@allure.story("Invalid Password")

def test_invalid_password(page):
    data = read_test_data("reg_valuninvpa")

    login_page = LoginPage(page)
    login_page.login(data["usernamevalue"], data["passwordvalue"])

    actual = login_page.get_toaster_message()

    assert data["expectedresult"] in actual

@allure.feature("Login")
@allure.story("Invalid Username")

def test_invalid_username(page):
    data = read_test_data("reg_invusvalpa")

    login_page = LoginPage(page)
    login_page.login(data["usernamevalue"], data["passwordvalue"])

    actual = login_page.get_toaster_message()

    assert data["expectedresult"] in actual

@allure.feature("Login")
@allure.story("Invalid Username and Password")

def test_invalid_both(page):
    data = read_test_data("reg_invunpa")

    login_page = LoginPage(page)
    login_page.login(data["usernamevalue"], data["passwordvalue"])

    actual = login_page.get_toaster_message()

    assert data["expectedresult"] in actual