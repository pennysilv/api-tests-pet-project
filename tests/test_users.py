import pytest
from jsonschema import validate

from config.config import Config
from utils.schemas import CREATE_USER_RESPONSE_SCHEMA, USER_SCHEMA


class TestUsers:
    @pytest.mark.smoke
    @pytest.mark.contract
    def test_get_all_users(self, api_client):
        """Get all users and validate the shape of a user object."""
        response = api_client.get(Config.USERS_ENDPOINT)

        api_client.assert_status_code(response, 200)
        users = response.json()
        assert isinstance(users, list)
        assert len(users) == 10

        validate(instance=users[0], schema=USER_SCHEMA)

    @pytest.mark.smoke
    @pytest.mark.contract
    def test_get_user_by_id(self, api_client):
        """Get one existing user by ID."""
        response = api_client.get(f"{Config.USERS_ENDPOINT}/1")

        api_client.assert_status_code(response, 200)
        user = response.json()
        validate(instance=user, schema=USER_SCHEMA)
        assert user["id"] == 1

    @pytest.mark.negative
    def test_get_nonexistent_user(self, api_client):
        """Requesting a missing user returns 404."""
        response = api_client.get(f"{Config.USERS_ENDPOINT}/999")

        api_client.assert_status_code(response, 404)

    @pytest.mark.regression
    @pytest.mark.contract
    def test_create_user(self, api_client):
        """Create a fake user and validate the echo response."""
        new_user = {
            "name": "Test User",
            "username": "testuser",
            "email": "test@example.com"
        }

        response = api_client.post(Config.USERS_ENDPOINT, json=new_user)

        api_client.assert_status_code(response, 201)
        created_user = response.json()
        validate(instance=created_user, schema=CREATE_USER_RESPONSE_SCHEMA)
        assert created_user["name"] == new_user["name"]
        assert created_user["username"] == new_user["username"]
        assert created_user["email"] == new_user["email"]
