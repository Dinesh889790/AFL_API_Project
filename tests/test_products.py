from api_clients.products_api import ProductsAPI

class TestProducts:
    api = ProductsAPI()

    def test_api_1_get_all_products(self):
        response = self.api.get_all_products()
        assert response.json()["responseCode"] == 200

    def test_api_2_post_to_products_list(self):
        response = self.api.post_to_all_products()
        assert response.json()["responseCode"] == 405
        assert response.json()["message"] == "This request method is not supported."

    def test_api_5_search_product_valid(self):
        response = self.api.search_product("top")
        assert response.json()["responseCode"] == 200

    def test_api_6_search_product_without_param(self):
        response = self.api.search_product()
        assert response.json()["responseCode"] == 400
        assert response.json()["message"] == "Bad request, search_product parameter is missing in POST request."