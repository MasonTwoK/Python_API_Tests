import pytest
import requests


@pytest.fixture()
def setup():
    print('!!Pre-condition actions!')


@pytest.fixture()
def teardown():
    yield
    print('!!Post-condition actions!!')


@pytest.fixture()
def post_requests():
    resp = requests.post(
        url='https://postman-rest-api-learner.glitch.me//info',
        json={"name": "Will"})
    yield resp  # why do we not use return here?
