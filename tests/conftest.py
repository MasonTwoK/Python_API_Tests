import pytest
import requests


@pytest.fixture()
def post_requests():
    resp = requests.post(
        url='https://postman-rest-api-learner.glitch.me//info',
        json={"name": "Will"})
    yield resp


@pytest.fixture()
def norris_get_categories():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/categories'
    )
    yield resp
