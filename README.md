# API Tests Pet Project

Автотесты для тестирования JSONPlaceholder API с использованием pytest

## 📝 Описание
Проект содержит автотесты для проверки REST API сервиса [JSONPlaceholder](https://jsonplaceholder.typicode.com).
Тесты покрывают основные CRUD операции для пользователей и проверяют корректность работы API.

## 🚀 Технологии
- **Python 3.x**
- **pytest** - фреймворк для тестирования
- **requests** - библиотека для HTTP запросов
- **pytest-html** - генерация HTML отчетов

## Что тестируем
- GET /users - получение пользователей
- GET /users/{id} - получение по ID  
- GET /users/999 - ошибка 404
- POST /users - создание пользователя

## Запуск
```bash
git clone https://github.com/pennysilv/api-tests-pet-project.git
cd api-tests-pet-project
python3 -m venv test_env
source test_env/bin/activate
pip install -r requirements.txt
pip install -e .
pytest -v
