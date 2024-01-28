# Home Task:
# + 1. Покрити api chuck norris https://api.chucknorris.io/
# + 2. Тести створити атомарі
# + 3. Зробити фікстуру
# + 4. Зробити маркери (лейбли)
# + 5. Прописати їх в pytest.ini
# + 6. Проранити через terminal pytest використовуючи оператори AND, OR, NOT
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


@pytest.mark.norris_get_by_category
def test_norris_get_by_category_animal(norris_get_by_category_animal):
    assert norris_get_by_category_animal.status_code == 200


@pytest.mark.norris_get_by_category
def test_norris_get_by_category_career(norris_get_by_category_career):
    assert norris_get_by_category_career.status_code == 200


@pytest.mark.norris_get_by_category
def test_norris_get_by_category_celebrity(norris_get_by_category_celebrity):
    assert norris_get_by_category_celebrity.status_code == 200


@pytest.mark.norris_get_by_category
def test_norris_get_by_category_dev(norris_get_by_category_dev):
    assert norris_get_by_category_dev.status_code == 200


@pytest.mark.norris_get_by_category
def test_norris_get_by_category_explicit(norris_get_by_category_explicit):
    assert norris_get_by_category_explicit.status_code == 200


@pytest.mark.norris_get_by_category
def test_norris_get_by_category_fashion(norris_get_by_category_fashion):
    assert norris_get_by_category_fashion.status_code == 200


@pytest.mark.norris_get_by_category
def test_norris_get_by_category_food(norris_get_by_category_food):
    assert norris_get_by_category_food.status_code == 200


@pytest.mark.norris_get_by_category
def test_norris_get_by_category_history(norris_get_by_category_history):
    assert norris_get_by_category_history.status_code == 200


@pytest.mark.norris_get_by_category
def test_norris_get_by_category_money(norris_get_by_category_money):
    assert norris_get_by_category_money.status_code == 200


@pytest.mark.norris_get_by_category
def test_norris_get_by_category_movie(norris_get_by_category_movie):
    assert norris_get_by_category_movie.status_code == 200


@pytest.mark.norris_get_by_category
def test_norris_get_by_category_music(norris_get_by_category_music):
    assert norris_get_by_category_music.status_code == 200


@pytest.mark.norris_get_by_category
def test_norris_get_by_category_political(norris_get_by_category_political):
    assert norris_get_by_category_political.status_code == 200


@pytest.mark.norris_get_by_category
def test_norris_get_by_category_religion(norris_get_by_category_religion):
    assert norris_get_by_category_religion.status_code == 200


@pytest.mark.norris_get_by_category
def test_norris_get_by_category_science(norris_get_by_category_science):
    assert norris_get_by_category_science.status_code == 200


@pytest.mark.norris_get_by_category
def test_norris_get_by_category_sport(norris_get_by_category_sport):
    assert norris_get_by_category_sport.status_code == 200


@pytest.mark.norris_get_by_category
def test_norris_get_by_category_travel(norris_get_by_category_travel):
    assert norris_get_by_category_travel.status_code == 200


@pytest.mark.norris_get_by_empty_category
def test_norris_get_by_empty_category_code(norris_get_by_empty_category):
    assert norris_get_by_empty_category.status_code == 404


@pytest.mark.norris_get_by_empty_category
def test_norris_get_by_empty_category_error_type(norris_get_by_empty_category):
    assert norris_get_by_empty_category.json()['error'] == 'Not Found'


@pytest.mark.norris_get_by_empty_category
def test_norris_get_by_empty_category_message(norris_get_by_empty_category):
    assert norris_get_by_empty_category.json()['message'] == 'No jokes for category "" found.'


@pytest.mark.norris_get_by_empty_category
def test_norris_get_by_empty_category_timestamp(norris_get_by_empty_category):
    assert norris_get_by_empty_category.json()['timestamp'] != ''


@pytest.mark.skip(reason='404 is present where it should be 400')
@pytest.mark.norris_get_by_wrong_category
def test_norris_get_by_wrong_category_code(norris_get_by_wrong_category):
    assert norris_get_by_wrong_category.status_code == 400


@pytest.mark.norris_get_by_wrong_category
def test_norris_get_by_wrong_category_error_type(norris_get_by_wrong_category):
    assert norris_get_by_wrong_category.json()['error'] == 'Not Found'


@pytest.mark.norris_get_by_wrong_category
def test_norris_get_by_wrong_category_message(norris_get_by_wrong_category):
    assert norris_get_by_wrong_category.json()['message'] == 'No jokes for category "[]" found.'


@pytest.mark.norris_get_by_wrong_category
def test_norris_get_by_wrong_category_timestamp(norris_get_by_wrong_category):
    assert norris_get_by_wrong_category.json()['timestamp'] != ''


@pytest.mark.norris_get_random
def test_norris_get_random_success_code(norris_get_random):
    assert norris_get_random.status_code == 200, 'Returned status code is not 200'


@pytest.mark.skip(reason='BUG #1: Empty Category could be present')
@pytest.mark.norris_get_random
def test_norris_get_random_success_category_presence(norris_get_random):
    assert norris_get_random.json()['categories'] != [], 'Category is not set'


@pytest.mark.skip(reason='BUG #1: Empty Category could be present')
@pytest.mark.norris_get_random
def test_norris_get_random_success_categories_amount_for_joke(norris_get_random):
    resp = norris_get_random
    assert len(resp.json()['categories']) == 1, 'Length of categories is not equal 1'


@pytest.mark.norris_get_random
def test_norris_get_random_response_body_amount(norris_get_random):
    resp = norris_get_random
    assert len(resp.json()) == 7, 'Length of response body size is not 7'


@pytest.mark.norris_get_random
def test_norris_get_random_success_creation_date_presence(norris_get_random):
    assert norris_get_random.json()['created_at'] is not None


@pytest.mark.norris_get_random
def test_norris_get_random_success_icon_presence(norris_get_random):
    assert norris_get_random.json()['icon_url'] is not None


@pytest.mark.norris_get_random
def test_norris_get_random_success_id_presence(norris_get_random):
    assert norris_get_random.json()['id'] is not None


@pytest.mark.norris_get_random
def test_norris_get_random_success_update_field_presence(norris_get_random):
    assert norris_get_random.json()['updated_at'] is not None


@pytest.mark.norris_get_random
def test_norris_get_random_success_url_presence(norris_get_random):
    assert norris_get_random.json()['url'] is not None


@pytest.mark.norris_get_random
def test_norris_get_random_success_value_presence(norris_get_random):
    assert norris_get_random.json()['value'] is not None


# Jokes by Query
@pytest.mark.norris_get_by_query
def test_norris_get_by_query_success_code(norris_get_by_query):
    assert norris_get_by_query.status_code == 200


@pytest.mark.norris_get_by_query
def test_norris_get_by_query_success_response_presence(norris_get_by_query):
    assert norris_get_by_query.json() is not None


@pytest.mark.norris_get_by_query
def test_norris_get_by_query_success_total_amount_jokes(norris_get_by_query):
    assert norris_get_by_query.json()['total'] != 0


@pytest.mark.norris_get_by_query
def test_norris_get_by_query_success_result_presence(norris_get_by_query):
    assert norris_get_by_query.json()['result'] is not None


@pytest.mark.norris_get_by_query
def test_norris_get_by_query_success_creation_date_presence(norris_get_by_query):
    assert norris_get_by_query.json()['result'][0]['created_at'] is not None


@pytest.mark.norris_get_by_query
def test_norris_get_by_query_success_icon_presence(norris_get_by_query):
    assert norris_get_by_query.json()['result'][0]['icon_url'] is not None


@pytest.mark.norris_get_by_query
def test_norris_get_by_query_success_id_presence(norris_get_by_query):
    assert norris_get_by_query.json()['result'][0]['id'] is not None


@pytest.mark.norris_get_by_query
def test_norris_get_by_query_success_update_date_presence(norris_get_by_query):
    assert norris_get_by_query.json()['result'][0]['updated_at'] is not None


@pytest.mark.norris_get_by_query
def test_norris_get_by_query_success_url_presence(norris_get_by_query):
    assert norris_get_by_query.json()['result'][0]['url'] is not None


@pytest.mark.norris_get_by_query
def test_norris_get_by_query_success_value_presence(norris_get_by_query):
    assert norris_get_by_query.json()['result'][0]['value'] is not None


@pytest.mark.skip("BUG #1: Empty Category is present")
@pytest.mark.norris_get_by_query
def test_norris_get_by_query_category_field_check(norris_get_by_query):
    assert norris_get_by_query.json()['result'][0]['categories'] != [], 'Category is be empty'
