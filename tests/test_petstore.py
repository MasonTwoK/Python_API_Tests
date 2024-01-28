# Coverage of https://petstore.swagger.io/
import pytest


# Questions:
# Q1: Do I need create a separate project for separate API coverage?

@pytest.mark.petstore_store
class TestStore:
    def test_post_store_order_success(self, petstore_post_store_order):
        assert petstore_post_store_order.status_code == 200

    @pytest.mark.skip(reason='BUG #1 Unexpected error code appear while sending request with out json body')
    @pytest.mark.negative_scenario
    def test_post_store_order_without_body(self, petstore_post_store_order_without_body):
        assert petstore_post_store_order_without_body.status_code == 400

    def test_get_store_order_success(self, petstore_get_store_order):
        assert petstore_get_store_order.status_code == 200

    def test_delete_store_order_success(self, petstore_delete_store_order):
        assert petstore_delete_store_order.status_code == 200
