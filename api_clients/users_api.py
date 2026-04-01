
"""
    User related API calls
"""

import requests
from config.settings import BASE_URL

class UsersAPI:

    def __init__(self):
        self.verify_login_url = f"{BASE_URL}/verifyLogin"
        self.create_account_url = f"{BASE_URL}/createAccount"
        self.delete_account_url = f"{BASE_URL}/deleteAccount"
        self.update_account_url = f"{BASE_URL}/updateAccount"
        self.get_user_url = f"{BASE_URL}/getUserDetailByEmail"

    def verify_login(self, email=None, password=None): # API 7, 8, 10
        payload = {}
        if email: payload["email"] = email
        if password: payload["password"] = password
        return requests.post(self.verify_login_url, data=payload)

    def delete_verify_login(self): # API 9
        return requests.delete(self.verify_login_url)

    def create_user(self, payload): # API 11
        return requests.post(self.create_account_url, data=payload)

    def delete_user(self, email, password): # API 12
        return requests.delete(self.delete_account_url, data={"email": email, "password": password})

    def update_user(self, payload): # API 13
        return requests.put(self.update_account_url, data=payload)

    def get_user_by_email(self, email):  # API 14
        return requests.get(self.get_user_url, params={"email": email})