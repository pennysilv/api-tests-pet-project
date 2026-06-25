import os


class Config:
    BASE_URL = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")
    TIMEOUT = float(os.getenv("API_TIMEOUT", "10"))

    USERS_ENDPOINT = "/users"
    POSTS_ENDPOINT = "/posts"
    COMMENTS_ENDPOINT = "/comments"
