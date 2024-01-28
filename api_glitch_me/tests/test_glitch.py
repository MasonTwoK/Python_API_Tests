import pytest


@pytest.mark.info_request
def test_post_info_request(post_requests):
    assert post_requests.status_code == 200
    assert post_requests.json()['data']['name'] == 'Will'
