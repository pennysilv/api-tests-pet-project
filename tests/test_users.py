import pytest
from config.config import Config

class TestUsers:
    
    def test_get_all_users(self, api_client):
        """Тест получения всех пользователей"""
        response = api_client.get(Config.USERS_ENDPOINT)
        
        assert response.status_code == 200
        users = response.json()
        assert len(users) == 10
        assert isinstance(users, list)
    
    def test_get_user_by_id(self, api_client):
        """Тест получения пользователя по ID"""
        response = api_client.get(f"{Config.USERS_ENDPOINT}/1")
        
        assert response.status_code == 200
        user = response.json()
        assert user["id"] == 1
        assert "name" in user
        assert "email" in user
    
    def test_get_nonexistent_user(self, api_client):
        """Тест получения несуществующего пользователя"""
        response = api_client.get(f"{Config.USERS_ENDPOINT}/999")
        
        assert response.status_code == 404
    
    def test_create_user(self, api_client):
        """Тест создания пользователя"""
        new_user = {
            "name": "Test User",
            "username": "testuser", 
            "email": "test@example.com"
        }
        
        response = api_client.post(Config.USERS_ENDPOINT, json=new_user)
        
        assert response.status_code == 201
        created_user = response.json()
        assert created_user["name"] == new_user["name"]
        assert "id" in created_user
