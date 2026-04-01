

from api_clients.brands_api import BrandsAPI

class TestBrands:
    api = BrandsAPI()

    def test_api_3_get_all_brands(self):
        response = self.api.get_all_brands()
        assert response.json()["responseCode"] == 200

    def test_api_4_put_to_brands_list(self):
        response = self.api.put_to_all_brands()
        assert response.json()["responseCode"] == 405
        assert response.json()["message"] == "This request method is not supported."