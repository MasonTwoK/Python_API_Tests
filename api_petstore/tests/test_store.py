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

        assert response['id'] == 101
        assert response['petId'] == 10
        assert response['quantity'] == 100
        assert response['status'] == "placed"
        assert response['complete'] is True
        # assert response['shipDate'] ==  # Need to be discuss

        assert store_get_order.status_code == 200

        response = store_get_order.json()
        assert len(response) == 6

        assert response['id'] == 101
        assert response['petId'] == 10
        assert response['quantity'] == 100
        assert response['status'] == "placed"
        assert response['complete'] is True
        # assert response['shipDate'] ==  # Need to be discuss

        # BUG: Successful code is not described in documentation
        assert store_delete_order.status_code == 200

        response = store_delete_order.json()
        assert response['type'] == "unknown"  # BUG: Type is not described
        assert response['message'] == "100"  # BUG: field should be named id ...


@pytest.mark.petstore_store
@pytest.mark.scenario_negative
class TestStorePostErrorHandling:
    @staticmethod
    @pytest.mark.skip(reason='BUG #1 Unexpected error code appear while sending request with out json body')
    def test_post_store_order_without_body(store_post_order_without_body):
        assert store_post_order_without_body.status_code == 400

    @staticmethod
    @pytest.mark.skip(reason='BUG #2 Response generates with random date')
    def test_post_store_order_with_empty_body(store_post_order_with_empty_body):
        assert store_post_order_with_empty_body.status_code == 400

    @staticmethod
    @pytest.mark.skip(reason='BUG #3 Random id assigned')
    def test_post_store_order_with_none_id(store_post_order_with_none_id):
        assert store_post_order_with_none_id.status_code == 400


@pytest.mark.skip(reason='TBD')
@pytest.mark.petstore_store
@pytest.mark.scenario_negative
class TestStoreGetErrorHandling:

    @staticmethod
    def test_get_invalid_data(store_get_order):
        pass


@pytest.mark.skip(reason='TBD')
@pytest.mark.petstore_store
@pytest.mark.scenario_negative
class TestStoreDeleteErrorHandling:
    @staticmethod
    def test_delete_invalid_id():
        pass


@pytest.mark.skip(reason='Request GET Inventory looks wrong in Store controller')
@pytest.mark.petstore_store
class TestStoreGetInventory:
    @staticmethod
    @pytest.mark.scenario_positive
    def test_get_store_inventory_success(store_get_inventory):
        assert store_get_inventory.status_code == 200
