import logging
from urllib.parse import urljoin

import requests
from config.config import Config


logger = logging.getLogger(__name__)


class APIClient:
    def __init__(self, base_url=Config.BASE_URL, timeout=Config.TIMEOUT):
        self.base_url = base_url.rstrip("/") + "/"
        self.timeout = timeout
        self.session = requests.Session()

    def request(self, method, endpoint, **kwargs):
        url = urljoin(self.base_url, endpoint.lstrip("/"))
        kwargs.setdefault("timeout", self.timeout)

        logger.info("%s %s", method.upper(), url)
        response = self.session.request(method, url, **kwargs)
        logger.info(
            "%s %s -> %s",
            method.upper(),
            url,
            response.status_code,
        )
        return response

    def get(self, endpoint, params=None):
        return self.request("GET", endpoint, params=params)

    def post(self, endpoint, json=None):
        return self.request("POST", endpoint, json=json)

    def put(self, endpoint, json=None):
        return self.request("PUT", endpoint, json=json)

    def patch(self, endpoint, json=None):
        return self.request("PATCH", endpoint, json=json)

    def delete(self, endpoint):
        return self.request("DELETE", endpoint)

    @staticmethod
    def assert_status_code(response, expected_status):
        assert response.status_code == expected_status, (
            f"Expected status {expected_status}, got {response.status_code}. "
            f"Response body: {response.text}"
        )
