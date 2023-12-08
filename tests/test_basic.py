# https://postman-rest-api-learner.glitch.me//info
# 1. Покрити api chuck norris https://api.chucknorris.io/
# 2. тести створити атомарі
# 3. зробити фікстуру
# 4. зробити маркери (лейбли)
# 5. прописати їх в pytest.ini
# 6. проранити через terminal pytest використовуючи оператори AND, OR, NOT
import pytest
import requests


# Info request
def test_post_info_request():
    resp = requests.post(
        url='https://postman-rest-api-learner.glitch.me//info',
        json={"name": "Will"})
    assert resp.status_code == 200
    assert resp.json()['data']['name'] == 'Will'


# Jokes Categories
def test_norris_get_categories_success_code_check():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/categories'
    )
    assert resp.status_code == 200


def test_norris_get_categories_response_body_check():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/categories'
    )
    assert resp.json() == ['animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', 'food', 'history', 'money',
                           'movie', 'music', 'political', 'religion', 'science', 'sport', 'travel']


# Jokes Category
def test_norris_get_by_category():
    categories = ['animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', 'food', 'history', 'money',
                  'movie', 'music', 'political', 'religion', 'science', 'sport', 'travel']

    for category in categories:
        resp = requests.get(
            url=f'https://api.chucknorris.io/jokes/random?category={category}')
        assert resp.status_code == 200
        print(resp.json())


# Jokes Random
def test_norris_get_random_success_code():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random')
    assert resp.status_code == 200


def test_norris_get_by_query_success_code():
    test_query = 'Chuck'
    resp = requests.get(
        url=f'https://api.chucknorris.io/jokes/search?query={test_query}'
    )
    assert resp.status_code == 200
    assert resp.json()['total'] != 0
    assert resp.json()['result'] != []
    assert resp.json()['result'][0]['created_at'] is not None
    assert resp.json()['result'][0]['icon_url'] is not None
    assert resp.json()['result'][0]['id'] is not None
    assert resp.json()['result'][0]['updated_at'] is not None
    assert resp.json()['result'][0]['url'] is not None
    assert resp.json()['result'][0]['value'] is not None


@pytest.mark.skip("BUG: Empty Category is present")
def test_norris_get_by_query_category_field_check():
    test_query = 'Chuck'
    resp = requests.get(
        url=f'https://api.chucknorris.io/jokes/search?query={test_query}'
    )
    assert resp.json()['result'][0]['categories'] != [], 'Category is be empty'
