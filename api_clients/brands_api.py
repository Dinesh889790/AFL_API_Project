
"""
    Common GET,POST requests wrappers
"""
import requests
from config.settings import BASE_URL

class BrandsAPI:

    def __init__(self):
        self.brands_list_url = f"{BASE_URL}/brandsList"

    def get_all_brands(self):
        return requests.get(self.brands_list_url)

    def put_to_all_brands(self):
        return requests.put(self.brands_list_url)
