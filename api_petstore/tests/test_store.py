# Tests related to Store controller in https://petstore.swagger.io/
import pytest


@pytest.mark.petstore_store
class TestStorePost:
    def test_post_store_order_success(self, petstore_post_store_order):
        assert petstore_post_store_order.status_code == 200

    @staticmethod
    @pytest.mark.skip(reason='BUG #1 Unexpected error code appear while sending request with out json body')
    @pytest.mark.negative_scenario
    def test_post_store_order_without_body(petstore_post_store_order_without_body):
        assert petstore_post_store_order_without_body.status_code == 400

    @staticmethod
    @pytest.mark.skip(reason='BUG #2 Response generates with random date')
    @pytest.mark.negative_scenario
    def test_post_store_order_with_empty_body(petstore_post_store_order_with_empty_body):
        assert petstore_post_store_order_with_empty_body.status_code == 400


@pytest.mark.petstore_store
class TestStoreGet:
    @staticmethod
    def test_get_store_order_success(petstore_get_store_order):
        assert petstore_get_store_order.status_code == 200


@pytest.mark.petstore_store
class TestStoreDelete:

    @staticmethod
    def test_delete_store_order_success(petstore_delete_store_order):
        assert petstore_delete_store_order.status_code == 200


@pytest.mark.petstore_store
class TestStoreGetInventory:

    @staticmethod
    def test_get_store_inventory_success(petstore_get_store_inventory):
        assert petstore_get_store_inventory.status_code == 200
