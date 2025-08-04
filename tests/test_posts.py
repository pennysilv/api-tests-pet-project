import pytest
from config.config import Config

class TestPosts:
    
    def test_get_all_posts(self, api_client):
        """Тест получения всех постов"""
        response = api_client.get(Config.POSTS_ENDPOINT)
        
        assert response.status_code == 200
        posts = response.json()
        assert len(posts) == 100  # JSONPlaceholder возвращает 100 постов
        
        # Проверяем структуру первого поста
        first_post = posts[0]
        assert "id" in first_post
        assert "userId" in first_post
        assert "title" in first_post
        assert "body" in first_post
    
    def test_get_post_by_id(self, api_client):
        """Тест получения поста по ID"""
        post_id = 1
        response = api_client.get(f"{Config.POSTS_ENDPOINT}/{post_id}")
        
        assert response.status_code == 200
        post = response.json()
        assert post["id"] == post_id
        assert len(post["title"]) > 0
        assert len(post["body"]) > 0
    
    def test_get_posts_by_user_id(self, api_client):
        """Тест получения постов конкретного пользователя"""
        user_id = 1
        response = api_client.get(Config.POSTS_ENDPOINT, params={"userId": user_id})
        
        assert response.status_code == 200
        posts = response.json()
        assert len(posts) > 0
        
        # Проверяем что все посты принадлежат нужному пользователю
        for post in posts:
            assert post["userId"] == user_id
    
    def test_create_post(self, api_client):
        """Тест создания нового поста"""
        new_post = {
            "title": "Test Post Title",
            "body": "This is a test post body",
            "userId": 1
        }
        
        response = api_client.post(Config.POSTS_ENDPOINT, json=new_post)
        
        assert response.status_code == 201
        created_post = response.json()
        assert created_post["title"] == new_post["title"]
        assert created_post["body"] == new_post["body"]
        assert created_post["userId"] == new_post["userId"]
        assert "id" in created_post
