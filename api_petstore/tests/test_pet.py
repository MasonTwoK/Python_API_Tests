# Tests related to Pet controller in https://petstore.swagger.io

def test_post_user_success(user_post_success):
    assert user_post_success.status_code == 200
