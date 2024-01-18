import pytest
import requests


@pytest.fixture
def post_requests():
    resp = requests.post(
        url='https://postman-rest-api-learner.glitch.me//info',
        json={"name": "Will"})
    yield resp


@pytest.fixture
def norris_get_categories():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/categories'
    )
    yield resp


@pytest.fixture
def norris_get_by_empty_category():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random?category='
    )
    yield resp


@pytest.fixture
def norris_get_by_wrong_category():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random?category=[]'
    )
    yield resp


@pytest.fixture
def norris_get_random():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random'
    )
    yield resp


@pytest.fixture
def norris_get_by_query():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/search?query=Chuck'
    )
    yield resp
