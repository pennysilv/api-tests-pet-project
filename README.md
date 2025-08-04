# API Tests Pet Project

Автотесты для тестирования JSONPlaceholder API с использованием pytest

## Описание
Проект содержит автотесты для проверки REST API сервиса [JSONPlaceholder](https://jsonplaceholder.typicode.com).
Тесты покрывают основные CRUD операции для пользователей и проверяют корректность работы API.

## Технологии
- **Python 3.x**
- **pytest** - фреймворк для тестирования
- **requests** - библиотека для HTTP запросов
- **pytest-html** - генерация HTML отчетов

## Покрытие тестами

### Тесты пользователей (`test_users.py`)
- ✅ **GET /users** - получение всех пользователей
- ✅ **GET /users/{id}** - получение пользователя по ID
- ✅ **GET /users/999** - обработка несуществующего пользователя (404)
- ✅ **POST /users** - создание нового пользователя

### Тесты постов (`test_posts.py`)
- ✅ **GET /posts** - получение всех постов
- ✅ **GET /posts/{id}** - получение поста по ID
- ✅ **GET /posts?userId={id}** - посты пользователя
- ✅ **POST /posts** - создание поста

### Параметризованные тесты (`test_parametrized.py`)
- ✅ **Множественные пользователи** - тест 5 разных ID
- ✅ **Множественные посты** - тест 5 разных ID  
- ✅ **Негативные тесты** - 4 некорректных ID
- ✅ **Связанные данные** - проверка постов пользователей

### Граничные тесты (`test_boundary.py`)
- ✅ **Минимальные/максимальные значения** - ID=1, ID=10, ID=100
- ✅ **За границами** - некорректные ID (0, 11, 101, -1)
- ✅ **Пустые поля и длинные строки**
- ✅ **Специальные символы** - эмодзи, SQL инъекции

- **40 тестов** выполняется успешно

## Запуск
```bash
git clone https://github.com/pennysilv/api-tests-pet-project.git
cd api-tests-pet-project
python3 -m venv test_env
source test_env/bin/activate
pip install -r requirements.txt
pip install -e .
pytest -v
