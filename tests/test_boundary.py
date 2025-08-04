import pytest
from config.config import Config

class TestBoundary:
    """Граничные тесты - проверка крайних значений"""
    
    def test_first_user(self, api_client):
        """Тест первого пользователя (минимальная граница)"""
        response = api_client.get(f"{Config.USERS_ENDPOINT}/1")
        
        assert response.status_code == 200
        user = response.json()
        assert user["id"] == 1
        assert len(user["name"]) > 0
    
    def test_last_user(self, api_client):
        """Тест последнего пользователя (максимальная граница)"""
        response = api_client.get(f"{Config.USERS_ENDPOINT}/10")
        
        assert response.status_code == 200
        user = response.json()
        assert user["id"] == 10
        assert len(user["name"]) > 0
    
    def test_first_post(self, api_client):
        """Тест первого поста (минимальная граница)"""
        response = api_client.get(f"{Config.POSTS_ENDPOINT}/1")
        
        assert response.status_code == 200
        post = response.json()
        assert post["id"] == 1
        assert post["userId"] >= 1
    
    def test_last_post(self, api_client):
        """Тест последнего поста (максимальная граница)"""
        response = api_client.get(f"{Config.POSTS_ENDPOINT}/100")
        
        assert response.status_code == 200
        post = response.json()
        assert post["id"] == 100
        assert post["userId"] <= 10
    
    @pytest.mark.parametrize("boundary_id", [0, 11, 101, -1])
    def test_beyond_boundaries(self, api_client, boundary_id):
        """Тест значений за границами допустимых ID"""
        # Для пользователей (1-10)
        if boundary_id in [0, 11, -1]:
            response = api_client.get(f"{Config.USERS_ENDPOINT}/{boundary_id}")
            assert response.status_code == 404
        
        # Для постов (1-100)  
        if boundary_id in [0, 101, -1]:
            response = api_client.get(f"{Config.POSTS_ENDPOINT}/{boundary_id}")
            assert response.status_code == 404
    
    def test_create_user_empty_fields(self, api_client):
        """Тест создания пользователя с пустыми полями"""
        empty_user = {
            "name": "",
            "username": "",
            "email": ""
        }
        
        response = api_client.post(Config.USERS_ENDPOINT, json=empty_user)
        # JSONPlaceholder принимает пустые поля, но в реальном API это была бы ошибка
        assert response.status_code == 201
        created_user = response.json()
        assert "id" in created_user
    
    def test_create_user_very_long_name(self, api_client):
        """Тест создания пользователя с очень длинным именем"""
        long_name = "A" * 1000  # Строка из 1000 символов
        
        long_user = {
            "name": long_name,
            "username": "testuser",
            "email": "test@example.com"
        }
        
        response = api_client.post(Config.USERS_ENDPOINT, json=long_user)
        assert response.status_code == 201
        created_user = response.json()
        assert created_user["name"] == long_name
    
    def test_create_post_empty_title_body(self, api_client):
        """Тест создания поста с пустыми заголовком и телом"""
        empty_post = {
            "title": "",
            "body": "",
            "userId": 1
        }
        
        response = api_client.post(Config.POSTS_ENDPOINT, json=empty_post)
        assert response.status_code == 201
        created_post = response.json()
        assert created_post["title"] == ""
        assert created_post["body"] == ""
    
    @pytest.mark.parametrize("special_char", ["<script>", "'; DROP TABLE users; --", "🚀🎉", "null"])
    def test_special_characters_in_name(self, api_client, special_char):
        """Тест специальных символов в имени пользователя"""
        special_user = {
            "name": special_char,
            "username": "testuser",
            "email": "test@example.com"
        }
        
        response = api_client.post(Config.USERS_ENDPOINT, json=special_user)
        assert response.status_code == 201
        created_user = response.json()
        assert created_user["name"] == special_char
