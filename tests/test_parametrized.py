import pytest
from config.config import Config

class TestParametrized:
    
    @pytest.mark.parametrize("user_id", [1, 2, 3, 5, 10])
    def test_get_multiple_users(self, api_client, user_id):
        """Тест получения разных пользователей по ID"""
        response = api_client.get(f"{Config.USERS_ENDPOINT}/{user_id}")
        
        assert response.status_code == 200
        user = response.json()
        assert user["id"] == user_id
        assert "name" in user
        assert "email" in user
        assert "@" in user["email"]  # Проверяем что email валидный
    
    @pytest.mark.parametrize("post_id", [1, 5, 10, 25, 50])
    def test_get_multiple_posts(self, api_client, post_id):
        """Тест получения разных постов по ID"""
        response = api_client.get(f"{Config.POSTS_ENDPOINT}/{post_id}")
        
        assert response.status_code == 200
        post = response.json()
        assert post["id"] == post_id
        assert len(post["title"]) > 0
        assert len(post["body"]) > 0
        assert post["userId"] >= 1
    
    @pytest.mark.parametrize("invalid_id", [0, -1, 999, 1000])
    def test_invalid_user_ids(self, api_client, invalid_id):
        """Тест обработки некорректных ID пользователей"""
        response = api_client.get(f"{Config.USERS_ENDPOINT}/{invalid_id}")
        
        assert response.status_code == 404
    
    @pytest.mark.parametrize("user_id,expected_posts_count", [
        (1, 10),  # У пользователя 1 должно быть 10 постов
        (2, 10),  # У пользователя 2 должно быть 10 постов
        (3, 10),  # У пользователя 3 должно быть 10 постов
    ])
    def test_user_posts_count(self, api_client, user_id, expected_posts_count):
        """Тест количества постов у разных пользователей"""
        response = api_client.get(Config.POSTS_ENDPOINT, params={"userId": user_id})
        
        assert response.status_code == 200
        posts = response.json()
        assert len(posts) == expected_posts_count
        
        # Проверяем что все посты принадлежат нужному пользователю
        for post in posts:
            assert post["userId"] == user_id
