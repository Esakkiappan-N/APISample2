import pytest
from pages.api.login_api import login_api      # ← fixed
from utils.csv_reader import read_csv

def test_login_api():
    users = read_csv("testdata/api/test_data.csv")
    for user in users:
        response = login_api(user["username"], user["password"])
        print("Response:", response.text)
        if response.status_code == 200:
            assert "accessToken" in response.json()  
        else:
            assert response.status_code == 400
def get_token(response):
    if response.status_code == 200:
        return response.json().get("accessToken")  
    return None