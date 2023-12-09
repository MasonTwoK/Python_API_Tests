# Home Task:
# 1. Покрити api chuck norris https://api.chucknorris.io/
# 2. тести створити атомарі
# 3. зробити фікстуру
# 4. зробити маркери (лейбли)
# 5. прописати їх в pytest.ini
# 6. проранити через terminal pytest використовуючи оператори AND, OR, NOT

# Questions:
# 1. Should I check data type for response fields?
# 2. Is it OK that for getting joke I get key categories NOT category, and data type is list

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
    assert len(resp.json()) == 16
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


# Jokes Random
def test_norris_get_random_success_code():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random')

    assert resp.status_code == 200, 'Returned status code is not 200'
    assert len(resp.json()) == 7, 'Length of response body size is not 7'
    # assert resp.json()['categories'] != [], 'Category is not set' #  "BUG #1: Empty Category is present"
    # assert len(resp.json()['categories']) == 1, 'Length of categories is not equal 1'
    assert resp.json()['created_at'] is not None
    assert resp.json()['icon_url'] is not None
    assert resp.json()['id'] is not None
    assert resp.json()['updated_at'] is not None
    assert resp.json()['url'] is not None
    assert resp.json()['value'] is not None


def test_norris_get_by_query_success_code():
    test_query = 'Chuck'
    resp = requests.get(
        url=f'https://api.chucknorris.io/jokes/search?query={test_query}'
    )

    assert resp.status_code == 200
    assert resp.json() is not None
    assert resp.json()['total'] != 0
    assert resp.json()['result'] is not None
    assert resp.json()['result'][0]['created_at'] is not None
    assert resp.json()['result'][0]['icon_url'] is not None
    assert resp.json()['result'][0]['id'] is not None
    assert resp.json()['result'][0]['updated_at'] is not None
    assert resp.json()['result'][0]['url'] is not None
    assert resp.json()['result'][0]['value'] is not None


@pytest.mark.skip("BUG #1: Empty Category is present")
def test_norris_get_by_query_category_field_check():
    test_query = 'Chuck'
    resp = requests.get(
        url=f'https://api.chucknorris.io/jokes/search?query={test_query}'
    )

    assert resp.json()['result'][0]['categories'] != [], 'Category is be empty'



