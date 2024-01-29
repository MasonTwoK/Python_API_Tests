import pytest
import requests
import content


@pytest.fixture
def petstore_post_store_order():
    resp = requests.post(
        url='https://petstore.swagger.io/v2/store/order',
        json=content.preset_store_order_1)
    yield resp


@pytest.fixture
def petstore_post_store_order_without_body():
    resp = requests.post(
        url='https://petstore.swagger.io/v2/store/order')
    yield resp


@pytest.fixture
def petstore_post_store_order_with_empty_body():
    resp = requests.post(
        url='https://petstore.swagger.io/v2/store/order',
        json={})
    yield resp



@pytest.fixture
def petstore_get_store_order():
    resp = requests.get(
        url='https://petstore.swagger.io/v2/store/order/100'
    )
    yield resp


@pytest.fixture
def petstore_delete_store_order():
    resp = requests.delete(
        url='https://petstore.swagger.io/v2/store/order/100'
    )
    yield resp
