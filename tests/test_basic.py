# Home Task:
# + 1. Покрити api chuck norris https://api.chucknorris.io/
# + 2. Тести створити атомарі
# + 3. Зробити фікстуру
# 4. Зробити маркери (лейбли)
# 5. Прописати їх в pytest.ini
# 6. Проранити через terminal pytest використовуючи оператори AND, OR, NOT
# 7. Flask simple REST API

# Questions:
# 1. Should I check data type for response fields?
# 2. Is it OK that for getting joke I get key categories NOT category, and data type is list
# 3. I cannot get 400 error code 'https://api.chucknorris.io/jokes/random?category={}'
# 4. Is it ok that I cannot understand 90% of what I read there https://docs.pytest.org/en/7.1.x/example/markers.html ?
# 5. Why do we not use return in conftest.py line 21 ?
# 6. Difference between iterator and generator
# 7. Check what is yield

import pytest
import requests


# DONE! Info request
@pytest.mark.info_request
def test_post_info_request(post_requests):
    assert post_requests.status_code == 200
    assert post_requests.json()['data']['name'] == 'Will'


# DONE! Jokes Categories
@pytest.mark.norris_get_categories
def test_norris_get_categories_success_code_check(norris_get_categories):
    assert norris_get_categories.status_code == 200


@pytest.mark.norris_get_categories
def test_norris_get_categories_response_body_check(norris_get_categories):
    assert norris_get_categories.json() == ['animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', 'food',
                                            'history', 'money',
                                            'movie', 'music', 'political', 'religion', 'science', 'sport', 'travel']


@pytest.mark.norris_get_categories
def test_norris_get_categories_amount_check(norris_get_categories):
    resp = norris_get_categories
    assert len(resp.json()) == 16


# DONE! Jokes Category
def test_norris_get_by_category():
    categories = ['animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', 'food', 'history', 'money',
                  'movie', 'music', 'political', 'religion', 'science', 'sport', 'travel']

    for category in categories:
        resp = requests.get(
            url=f'https://api.chucknorris.io/jokes/random?category={category}')

        assert resp.status_code == 200


def test_norris_get_by_empty_category_code():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random?category='
    )
    assert resp.status_code == 404


def test_norris_get_by_empty_category_error_type():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random?category='
    )
    assert resp.json()['error'] == 'Not Found'


def test_norris_get_by_empty_category_message():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random?category='
    )
    assert resp.json()['message'] == 'No jokes for category "" found.'


def test_norris_get_by_empty_category_timestamp():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random?category='
    )
    assert resp.json()['timestamp'] != ''


@pytest.mark.skip(reason='404 is present where it should be 400')
def test_norris_get_by_wrong_category_code():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random?category=[]'
    )
    assert resp.status_code == 400


def test_norris_get_by_wrong_category_error_type():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random?category=[]'
    )
    assert resp.json()['error'] == 'Not Found'


def test_norris_get_by_wrong_category_message():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random?category=[]'
    )
    assert resp.json()['message'] == 'No jokes for category "[]" found.'


def test_norris_get_by_wrong_category_timestamp():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random?category=[]'
    )
    assert resp.json()['timestamp'] != ''


# Jokes Random
def test_norris_get_random_success_code():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random')

    assert resp.status_code == 200, 'Returned status code is not 200'


@pytest.mark.skip(reason='BUG #1: Empty Category could be present')
def test_norris_get_random_success_category_presence():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random')
    assert resp.json()['categories'] != [], 'Category is not set'


@pytest.mark.skip(reason='BUG #1: Empty Category could be present')
def test_norris_get_random_success_categories_amount_for_joke():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random')
    assert len(resp.json()['categories']) == 1, 'Length of categories is not equal 1'


def test_norris_get_random_response_body_amount():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random')
    assert len(resp.json()) == 7, 'Length of response body size is not 7'


def test_norris_get_random_success_creation_date_presence():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random')
    assert resp.json()['created_at'] is not None


def test_norris_get_random_success_icon_presence():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random')
    assert resp.json()['icon_url'] is not None


def test_norris_get_random_success_id_presence():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random')
    assert resp.json()['id'] is not None


def test_norris_get_random_success_update_field_presence():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random')
    assert resp.json()['updated_at'] is not None


def test_norris_get_random_success_url_presence():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random')
    assert resp.json()['url'] is not None


def test_norris_get_random_success_value_presence():
    resp = requests.get(
        url='https://api.chucknorris.io/jokes/random')
    assert resp.json()['value'] is not None


# Jokes by Query
def test_norris_get_by_query_success_code():
    test_query = 'Chuck'
    resp = requests.get(
        url=f'https://api.chucknorris.io/jokes/search?query={test_query}'
    )
    assert resp.status_code == 200


def test_norris_get_by_query_success_response_presence():
    test_query = 'Chuck'
    resp = requests.get(
        url=f'https://api.chucknorris.io/jokes/search?query={test_query}'
    )
    assert resp.json() is not None


def test_norris_get_by_query_success_total_amount_jokes():
    test_query = 'Chuck'
    resp = requests.get(
        url=f'https://api.chucknorris.io/jokes/search?query={test_query}'
    )
    assert resp.json()['total'] != 0


def test_norris_get_by_query_success_result_presence():
    test_query = 'Chuck'
    resp = requests.get(
        url=f'https://api.chucknorris.io/jokes/search?query={test_query}'
    )
    assert resp.json()['result'] is not None


def test_norris_get_by_query_success_creation_date_presence():
    test_query = 'Chuck'
    resp = requests.get(
        url=f'https://api.chucknorris.io/jokes/search?query={test_query}'
    )
    assert resp.json()['result'][0]['created_at'] is not None


def test_norris_get_by_query_success_icon_presence():
    test_query = 'Chuck'
    resp = requests.get(
        url=f'https://api.chucknorris.io/jokes/search?query={test_query}'
    )
    assert resp.json()['result'][0]['icon_url'] is not None


def test_norris_get_by_query_success_id_presence():
    test_query = 'Chuck'
    resp = requests.get(
        url=f'https://api.chucknorris.io/jokes/search?query={test_query}'
    )
    assert resp.json()['result'][0]['id'] is not None


def test_norris_get_by_query_success_update_date_presence():
    test_query = 'Chuck'
    resp = requests.get(
        url=f'https://api.chucknorris.io/jokes/search?query={test_query}'
    )
    assert resp.json()['result'][0]['updated_at'] is not None


def test_norris_get_by_query_success_url_presence():
    test_query = 'Chuck'
    resp = requests.get(
        url=f'https://api.chucknorris.io/jokes/search?query={test_query}'
    )
    assert resp.json()['result'][0]['url'] is not None


def test_norris_get_by_query_success_value_presence():
    test_query = 'Chuck'
    resp = requests.get(
        url=f'https://api.chucknorris.io/jokes/search?query={test_query}'
    )
    assert resp.json()['result'][0]['value'] is not None


@pytest.mark.skip("BUG #1: Empty Category is present")
def test_norris_get_by_query_category_field_check():
    test_query = 'Chuck'
    resp = requests.get(
        url=f'https://api.chucknorris.io/jokes/search?query={test_query}'
    )
    assert resp.json()['result'][0]['categories'] != [], 'Category is be empty'
