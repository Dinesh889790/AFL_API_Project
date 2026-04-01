
"""
    Related to products api calls
"""

import requests
from config.settings import BASE_URL

class ProductsAPI:

    def __init__(self):
        self.products_list_url = f"{BASE_URL}/productsList"
        self.search_product_url = f"{BASE_URL}/searchProduct"

    def get_all_products(self):  # API 1
        return requests.get(self.products_list_url)

    def post_to_all_products(self):
        return requests.post(self.products_list_url)

    def search_product(self,search_item = None):
        if search_item:
            return requests.post(self.search_product_url,data={"search_product": search_item})
        return requests.post(self.search_product_url)


