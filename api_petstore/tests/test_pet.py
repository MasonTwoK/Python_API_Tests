# Tests related to Pet controller in https://petstore.swagger.io

def test_post_user_success(post_user_success):
    assert post_user_success.status_code == 200
