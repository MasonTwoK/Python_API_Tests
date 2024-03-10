# Tests related to Store controller in https://petstore.swagger.io/
import pytest


@pytest.mark.petstore_store
class TestStorePost:
    def test_post_store_order_success(self, store_post_order):
        assert store_post_order.status_code == 200

    @staticmethod
    @pytest.mark.skip(reason='BUG #1 Unexpected error code appear while sending request with out json body')
    @pytest.mark.negative_scenario
    def test_post_store_order_without_body(store_post_order_without_body):
        assert store_post_order_without_body.status_code == 400

    @staticmethod
    @pytest.mark.skip(reason='BUG #2 Response generates with random date')
    @pytest.mark.negative_scenario
    def test_post_store_order_with_empty_body(store_post_order_with_empty_body):
        assert store_post_order_with_empty_body.status_code == 400


@pytest.mark.petstore_store
class TestStoreGet:
    @staticmethod
    def test_get_store_order_success(store_get_order):
        assert store_get_order.status_code == 200

        response = store_get_order.json()
        # assert response['id'] == api_petstore.content.preset_store_order_1['id']
        # assert response['petId'] == content.preset_store_order_1['petId']
        # assert response['quantity'] == content.preset_store_order_1['quantity']
        # assert response['status'] == content.preset_store_order_1['status']
        # assert response['complete'] == content.preset_store_order_1['complete']
        # # assert response['shipDate'] == content.preset_store_order_1['shipDate'] # How to check data type right?


@pytest.mark.petstore_store
class TestStoreDelete:
    @staticmethod
    def test_delete_store_order_success(store_get_order, store_delete_order):
        assert store_delete_order.status_code == 200

        response = store_delete_order.json()
        # assert response['message'] == preset_store_order_1['id']
        assert response['type'] == 'unknown'
        assert response['code'] == store_delete_order.status_code


@pytest.mark.skip("Request GET Inventory looks wrong in Store controller")
@pytest.mark.petstore_store
class TestStoreGetInventory:
    @staticmethod
    def test_get_store_inventory_success(store_get_inventory):
        assert store_get_inventory.status_code == 200
