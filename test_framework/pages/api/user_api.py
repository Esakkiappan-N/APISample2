import requests

BASE_URL = "https://dummyjson.com"
USER_PROFILE_PATH = "/users/1"


def get_user_profile(token):
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return requests.get(BASE_URL + USER_PROFILE_PATH, headers=headers)
