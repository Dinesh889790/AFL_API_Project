import pytest
import time
from api_clients.users_api import UsersAPI
from payloads.user_data import get_user_payload


class TestUsers:
    api = UsersAPI()

    # Class level variables for dynamic test data
    dynamic_email = f"afl_test_{int(time.time())}@yopmail.com"
    password = "Password123!"

    # --- Login APIs ---
    def test_api_7_verify_login_valid(self):
        # Using a known existing user for valid login test (or create one in setup)
        response = self.api.verify_login("dinesh8897@gmail.com", "Ange949161@")
        # Note: 'test@test.com' is often available on this site, if it fails, replace with a known created user.
        assert response.json()["responseCode"] == 200

    def test_api_8_verify_login_without_email(self):
        response = self.api.verify_login(password="test")
        assert response.json()["responseCode"] == 400

    def test_api_9_delete_verify_login(self):
        response = self.api.delete_verify_login()
        assert response.json()["responseCode"] == 405

    def test_api_10_verify_login_invalid(self):
        response = self.api.verify_login("invalid_afl@mail.com", "wrongpass")
        assert response.json()["responseCode"] == 404

    # --- User Lifecycle APIs (11, 14, 13, 12) ---
    # We run these sequentially to Create -> Get -> Update -> Delete

    def test_api_11_create_user(self):
        payload = get_user_payload(self.dynamic_email, self.password)
        response = self.api.create_user(payload)
        assert response.json()["responseCode"] == 201

    def test_api_14_get_user_by_email(self):
        response = self.api.get_user_by_email(self.dynamic_email)
        assert response.json()["responseCode"] == 200
        assert response.json()["user"]["email"] == self.dynamic_email

    def test_api_13_update_user(self):
        payload = get_user_payload(self.dynamic_email, self.password)
        payload["name"] = "AFL Updated Name"  # Changing data
        response = self.api.update_user(payload)
        assert response.json()["responseCode"] == 200

    def test_api_12_delete_user(self):
        response = self.api.delete_user(self.dynamic_email, self.password)
        assert response.json()["responseCode"] == 200