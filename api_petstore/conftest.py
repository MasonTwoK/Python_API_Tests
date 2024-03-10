import pytest
import requests
import content


@pytest.fixture
def store_post_order():
    resp = requests.post(
        url='https://petstore.swagger.io/v2/store/order',
        json=content.preset_store_order_1)
    yield resp


@pytest.fixture
def store_post_order_without_body():
    resp = requests.post(
        url='https://petstore.swagger.io/v2/store/order')
    yield resp


@pytest.fixture
def store_post_order_with_empty_body():
    resp = requests.post(
        url='https://petstore.swagger.io/v2/store/order',
        json={})
    yield resp


@pytest.fixture
def store_get_order():
    resp = requests.get(
        url=f'https://petstore.swagger.io/v2/store/order/{content.preset_store_order_1["id"]}'
    )
    yield resp


@pytest.fixture
def store_delete_order():
    resp = requests.delete(
        url='https://petstore.swagger.io/v2/store/order/100'
    )
    yield resp


@pytest.fixture
def store_get_inventory():
    resp = requests.get(url='https://petstore.swagger.io/v2/store/inventory')
    yield resp


@pytest.fixture
def user_post_success():
    resp = requests.post(url='https://petstore.swagger.io/v2/user', json=content.preset_user)
    yield resp
