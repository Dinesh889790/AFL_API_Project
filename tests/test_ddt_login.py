"""
Data driven testing
"""

import pytest
from api_clients.users_api import BASE_URL, UsersAPI
from payloads.user_data import data_driven

@pytest.mark.parametrize("email,password,expected_status",data_driven())
def test_login_api_ddt(email,password,expected_status):
    api = UsersAPI()
    response = api.verify_login(email=email,password=password)

    actual_code = response.json().get("responseCode")
    assert actual_code == expected_status
