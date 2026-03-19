import pytest
from pages.api.login_api import login_api, get_token      # ← fixed
from pages.api.user_api import get_user_profile            # ← fixed
from utils.csv_reader import read_csv


@pytest.mark.parametrize("user", read_csv("testdata/api/test_data.csv"))
def test_user_flow(user):
    login_response = login_api(user["username"], user["password"])
    print("Login Response:", login_response.text)

   if expected_valid:
    assert login_response.status_code == 200
   else:
    assert login_response.status_code == 400

    token = get_token(login_response)
    print("Token:", token)

    assert token is not None

    profile_response = get_user_profile(token)
    print("Profile Response:", profile_response.text)

   if expected_valid:
    assert login_response.status_code == 200
  else:
    assert login_response.status_code == 400
