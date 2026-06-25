import pytest
from jsonschema import validate

from config.config import Config
from utils.schemas import CREATE_POST_RESPONSE_SCHEMA, POST_SCHEMA


class TestPosts:
    @pytest.mark.smoke
    @pytest.mark.contract
    def test_get_all_posts(self, api_client):
        """Get all posts and validate the shape of a post object."""
        response = api_client.get(Config.POSTS_ENDPOINT)

        api_client.assert_status_code(response, 200)
        posts = response.json()
        assert isinstance(posts, list)
        assert len(posts) == 100
        validate(instance=posts[0], schema=POST_SCHEMA)

    @pytest.mark.smoke
    @pytest.mark.contract
    def test_get_post_by_id(self, api_client):
        """Get one existing post by ID."""
        post_id = 1
        response = api_client.get(f"{Config.POSTS_ENDPOINT}/{post_id}")

        api_client.assert_status_code(response, 200)
        post = response.json()
        validate(instance=post, schema=POST_SCHEMA)
        assert post["id"] == post_id
        assert len(post["title"]) > 0
        assert len(post["body"]) > 0

    @pytest.mark.regression
    def test_get_posts_by_user_id(self, api_client):
        """Filter posts by user ID."""
        user_id = 1
        response = api_client.get(Config.POSTS_ENDPOINT, params={"userId": user_id})

        api_client.assert_status_code(response, 200)
        posts = response.json()
        assert len(posts) > 0

        for post in posts:
            validate(instance=post, schema=POST_SCHEMA)
            assert post["userId"] == user_id

    @pytest.mark.regression
    @pytest.mark.contract
    def test_create_post(self, api_client):
        """Create a fake post and validate the echo response."""
        new_post = {
            "title": "Test Post Title",
            "body": "This is a test post body",
            "userId": 1,
        }

        response = api_client.post(Config.POSTS_ENDPOINT, json=new_post)

        api_client.assert_status_code(response, 201)
        created_post = response.json()
        validate(instance=created_post, schema=CREATE_POST_RESPONSE_SCHEMA)
        assert created_post["title"] == new_post["title"]
        assert created_post["body"] == new_post["body"]
        assert created_post["userId"] == new_post["userId"]

    @pytest.mark.regression
    @pytest.mark.contract
    def test_update_post_with_put(self, api_client):
        """Update a fake post using PUT."""
        updated_post = {
            "id": 1,
            "title": "Updated Test Title",
            "body": "Updated body",
            "userId": 1,
        }

        response = api_client.put(f"{Config.POSTS_ENDPOINT}/1", json=updated_post)

        api_client.assert_status_code(response, 200)
        post = response.json()
        validate(instance=post, schema=POST_SCHEMA)
        assert post["title"] == updated_post["title"]
        assert post["body"] == updated_post["body"]

    @pytest.mark.regression
    def test_update_post_title_with_patch(self, api_client):
        """Partially update a fake post using PATCH."""
        response = api_client.patch(
            f"{Config.POSTS_ENDPOINT}/1",
            json={"title": "Partially Updated Title"},
        )

        api_client.assert_status_code(response, 200)
        post = response.json()
        assert post["id"] == 1
        assert post["title"] == "Partially Updated Title"

    @pytest.mark.regression
    def test_delete_post(self, api_client):
        """Delete a fake post. JSONPlaceholder returns an empty object."""
        response = api_client.delete(f"{Config.POSTS_ENDPOINT}/1")

        api_client.assert_status_code(response, 200)
        assert response.json() == {}
