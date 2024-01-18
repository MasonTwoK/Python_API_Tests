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


@pytest.fixture
def norris_get_by_category_animal():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random?category=animal'
    )
    yield resp


@pytest.fixture
def norris_get_by_category_career():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random?category=career'
    )
    yield resp


@pytest.fixture
def norris_get_by_category_celebrity():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random?category=celebrity'
    )
    yield resp


@pytest.fixture
def norris_get_by_category_dev():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random?category=dev'
    )
    yield resp


@pytest.fixture
def norris_get_by_category_explicit():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random?category=explicit'
    )
    yield resp


@pytest.fixture
def norris_get_by_category_fashion():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random?category=fashion'
    )
    yield resp


@pytest.fixture
def norris_get_by_category_food():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random?category=food'
    )
    yield resp


@pytest.fixture
def norris_get_by_category_history():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random?category=history'
    )
    yield resp


@pytest.fixture
def norris_get_by_category_money():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random?category=money'
    )
    yield resp


@pytest.fixture
def norris_get_by_category_movie():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random?category=movie'
    )
    yield resp


@pytest.fixture
def norris_get_by_category_music():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random?category=music'
    )
    yield resp


@pytest.fixture
def norris_get_by_category_political():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random?category=political'
    )
    yield resp


@pytest.fixture
def norris_get_by_category_religion():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random?category=religion'
    )
    yield resp


@pytest.fixture
def norris_get_by_category_science():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random?category=science'
    )
    yield resp


@pytest.fixture
def norris_get_by_category_sport():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random?category=sport'
    )
    yield resp


@pytest.fixture
def norris_get_by_category_travel():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random?category=travel'
    )
    yield resp
