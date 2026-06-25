import pytest
from jsonschema import validate

from config.config import Config
from utils.schemas import POST_SCHEMA, USER_SCHEMA


class TestParametrized:
    @pytest.mark.regression
    @pytest.mark.contract
    @pytest.mark.parametrize("user_id", [1, 2, 3, 5, 10])
    def test_get_multiple_users(self, api_client, user_id):
        """Get several known users by ID."""
        response = api_client.get(f"{Config.USERS_ENDPOINT}/{user_id}")

        api_client.assert_status_code(response, 200)
        user = response.json()
        validate(instance=user, schema=USER_SCHEMA)
        assert user["id"] == user_id
        assert "@" in user["email"]

    @pytest.mark.regression
    @pytest.mark.contract
    @pytest.mark.parametrize("post_id", [1, 5, 10, 25, 50])
    def test_get_multiple_posts(self, api_client, post_id):
        """Get several known posts by ID."""
        response = api_client.get(f"{Config.POSTS_ENDPOINT}/{post_id}")

        api_client.assert_status_code(response, 200)
        post = response.json()
        validate(instance=post, schema=POST_SCHEMA)
        assert post["id"] == post_id
        assert len(post["title"]) > 0
        assert len(post["body"]) > 0

    @pytest.mark.negative
    @pytest.mark.parametrize("invalid_id", [0, -1, 999, 1000])
    def test_invalid_user_ids(self, api_client, invalid_id):
        """Missing user IDs return 404."""
        response = api_client.get(f"{Config.USERS_ENDPOINT}/{invalid_id}")

        api_client.assert_status_code(response, 404)

    @pytest.mark.regression
    @pytest.mark.parametrize("user_id,expected_posts_count", [
        (1, 10),
        (2, 10),
        (3, 10),
    ])
    def test_user_posts_count(self, api_client, user_id, expected_posts_count):
        """Known users have ten posts in JSONPlaceholder's static data set."""
        response = api_client.get(Config.POSTS_ENDPOINT, params={"userId": user_id})

        api_client.assert_status_code(response, 200)
        posts = response.json()
        assert len(posts) == expected_posts_count

        for post in posts:
            assert post["userId"] == user_id
