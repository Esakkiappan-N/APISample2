import requests

BASE_URL = "https://dummyjson.com"
LOGIN_PATH = "/auth/login"


def login_api(username, password):
    url = BASE_URL + LOGIN_PATH
    payload = {
        "username": username,
        "password": password
    }
    response = requests.post(url, json=payload)
    return response


def get_token(response):
    if response.status_code == 200:
        return response.json().get("token") or response.json().get("accessToken")
    return None
