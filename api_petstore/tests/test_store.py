# Tests related to Store controller in https://petstore.swagger.io/
import pytest


@pytest.mark.petstore_store
class TestStorePost:
    @pytest.mark.scenario_positive
    def test_post_store_order_success(self, store_post_order):
        assert store_post_order.status_code == 200

    @staticmethod
    @pytest.mark.skip(reason='BUG #1 Unexpected error code appear while sending request with out json body')
    @pytest.mark.scenario_negative
    def test_post_store_order_without_body(store_post_order_without_body):
        assert store_post_order_without_body.status_code == 400

    @staticmethod
    @pytest.mark.skip(reason='BUG #2 Response generates with random date')
    @pytest.mark.scenario_negative
    def test_post_store_order_with_empty_body(store_post_order_with_empty_body):
        assert store_post_order_with_empty_body.status_code == 400


@pytest.mark.petstore_store
class TestStoreGet:

    @staticmethod
    @pytest.mark.scenario_positive
    def test_get_store_order_success(store_get_order):
        assert store_get_order.status_code == 200

        response = store_get_order.json()
        assert response['id'] == 100
        assert response['petId'] == 10
        assert response['quantity'] == 100
        assert response['status'] == "placed"
        assert response['complete'] is True
        # assert response['shipDate'] == content.preset_store_order_1['shipDate'] # How to check data type right?


@pytest.mark.petstore_store
class TestStoreDelete:
    @staticmethod
    @pytest.mark.scenario_positive
    def test_delete_store_order_success(store_get_order, store_delete_order):
        assert store_delete_order.status_code == 200

        response = store_delete_order.json()
        assert response['message'] == '100'
        assert response['type'] == 'unknown'
        assert response['code'] == store_delete_order.status_code


@pytest.mark.petstore_store
class TestStoreGetInventory:
    @staticmethod
    @pytest.mark.skip("Request GET Inventory looks wrong in Store controller")
    @pytest.mark.scenario_positive
    def test_get_store_inventory_success(store_get_inventory):
        assert store_get_inventory.status_code == 200
