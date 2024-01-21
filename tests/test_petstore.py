# Coverage of https://petstore.swagger.io/
import pytest


# Questions:
# Q1: Do I need create a separate project for separate API coverage?

@pytest.mark.petstore_store
class TestStore:
    def test_post_store_order_success(self, petstore_post_store_order):
        assert petstore_post_store_order.status_code == 200

    def test_get_store_order_success(self, petstore_get_store_order):
        assert petstore_get_store_order.status_code == 200

    def test_delete_store_order_success(self, petstore_delete_store_order):
        assert petstore_delete_store_order.status_code == 200
