import pytest

from config.config import Config


class TestBoundary:
    """Boundary-style checks for JSONPlaceholder's static resource IDs."""

    @pytest.mark.regression
    def test_first_user(self, api_client):
        """The first known user can be retrieved."""
        response = api_client.get(f"{Config.USERS_ENDPOINT}/1")

        api_client.assert_status_code(response, 200)
        user = response.json()
        assert user["id"] == 1
        assert len(user["name"]) > 0

    @pytest.mark.regression
    def test_last_user(self, api_client):
        """The last known user in the static data set can be retrieved."""
        response = api_client.get(f"{Config.USERS_ENDPOINT}/10")

        api_client.assert_status_code(response, 200)
        user = response.json()
        assert user["id"] == 10
        assert len(user["name"]) > 0

    @pytest.mark.regression
    def test_first_post(self, api_client):
        """The first known post can be retrieved."""
        response = api_client.get(f"{Config.POSTS_ENDPOINT}/1")

        api_client.assert_status_code(response, 200)
        post = response.json()
        assert post["id"] == 1
        assert post["userId"] >= 1

    @pytest.mark.regression
    def test_last_post(self, api_client):
        """The last known post in the static data set can be retrieved."""
        response = api_client.get(f"{Config.POSTS_ENDPOINT}/100")

        api_client.assert_status_code(response, 200)
        post = response.json()
        assert post["id"] == 100
        assert post["userId"] <= 10

    @pytest.mark.negative
    @pytest.mark.parametrize("user_id", [0, 11, -1])
    def test_user_id_outside_known_range(self, api_client, user_id):
        """User IDs outside the known range return 404."""
        response = api_client.get(f"{Config.USERS_ENDPOINT}/{user_id}")

        api_client.assert_status_code(response, 404)

    @pytest.mark.negative
    @pytest.mark.parametrize("post_id", [0, 101, -1])
    def test_post_id_outside_known_range(self, api_client, post_id):
        """Post IDs outside the known range return 404."""
        response = api_client.get(f"{Config.POSTS_ENDPOINT}/{post_id}")

        api_client.assert_status_code(response, 404)
