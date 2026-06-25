import logging

import pytest
from utils.api_client import APIClient


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)


@pytest.fixture
def api_client():
    return APIClient()
