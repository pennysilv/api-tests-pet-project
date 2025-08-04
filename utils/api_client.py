import requests
from config.config import Config

class APIClient:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.timeout = Config.TIMEOUT
        self.session = requests.Session()
    
    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, params=params, timeout=self.timeout)
        return response
    
    def post(self, endpoint, json=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, json=json, timeout=self.timeout)
        return response
