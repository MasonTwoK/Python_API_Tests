# Tests related to Store controller in https://petstore.swagger.io/
import pytest


@pytest.mark.petstore_store
@pytest.mark.scenario_positive
class TestStoreSuccess:
    @staticmethod
    def test_store_success(store_post_order, store_get_order, store_delete_order):
        assert store_post_order.status_code == 200

        response = store_post_order.json()
        assert len(response) == 6

        assert response['id'] == 100
        assert response['petId'] == 10
        assert response['quantity'] == 100
        assert response['status'] == "placed"
        assert response['complete'] is True
        # assert response['shipDate'] == #

        assert store_get_order.status_code == 200

        assert store_delete_order.status_code == 200


@pytest.mark.petstore_store
@pytest.mark.scenario_negative
class TestStorePost:
    @staticmethod
    @pytest.mark.skip(reason='BUG #1 Unexpected error code appear while sending request with out json body')
    def test_post_store_order_without_body(store_post_order_without_body):
        assert store_post_order_without_body.status_code == 400

    @staticmethod
    @pytest.mark.skip(reason='BUG #2 Response generates with random date')
    def test_post_store_order_with_empty_body(store_post_order_with_empty_body):
        assert store_post_order_with_empty_body.status_code == 400


@pytest.mark.petstore_store
@pytest.mark.scenario_negative
class TestStoreGet:

    @staticmethod
    def test_get_invalid_data(store_get_order):
        pass


@pytest.mark.petstore_store
@pytest.mark.scenario_negative
class TestStoreDelete:
    @staticmethod
    def test_delete_invalid_id():
        pass


@pytest.mark.skip("Request GET Inventory looks wrong in Store controller")
@pytest.mark.petstore_store
class TestStoreGetInventory:
    @staticmethod
    @pytest.mark.scenario_positive
    def test_get_store_inventory_success(store_get_inventory):
        assert store_get_inventory.status_code == 200
