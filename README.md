# REST API Test Automation

[![API Tests](https://github.com/pennysilv/python-api-test-framework/actions/workflows/tests.yml/badge.svg)](https://github.com/pennysilv/python-api-test-framework/actions/workflows/tests.yml)

Automated REST API tests written with Python, pytest, and requests. The suite uses reusable fixtures, a small HTTP client, JSON Schema checks, pytest markers, Ruff, pre-commit, and GitHub Actions.

The tests run against [JSONPlaceholder](https://jsonplaceholder.typicode.com), a fake public REST API. JSONPlaceholder is useful for demonstrating test automation practices, but it does not validate real business rules or persist created data.

## Features

- REST API tests for users and posts endpoints
- Reusable API client with logging and timeout handling
- Environment-based base URL and timeout configuration
- JSON Schema validation for key responses
- Positive, negative, boundary-style, and parametrized tests
- Pytest markers for selective test runs
- Ruff linting and formatting checks
- pre-commit hooks for local quality checks
- GitHub Actions with JUnit XML and HTML report artifacts

## Project Structure

```text
.
├── .github/
│   └── workflows/
│       └── tests.yml
├── config/
│   ├── __init__.py
│   └── config.py
├── tests/
│   ├── conftest.py
│   ├── test_boundary.py
│   ├── test_parametrized.py
│   ├── test_posts.py
│   └── test_users.py
├── utils/
│   ├── __init__.py
│   ├── api_client.py
│   └── schemas.py
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── pyproject.toml
├── pytest.ini
├── requirements.txt
└── README.md
```

## Technologies

- Python 3.12
- pytest
- requests
- jsonschema
- pytest-html
- Ruff
- pre-commit
- GitHub Actions

## Installation

Clone the repository:

```bash
git clone https://github.com/pennysilv/python-api-test-framework.git
cd python-api-test-framework
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Install local pre-commit hooks:

```bash
python -m pre_commit install
```

Run all pre-commit hooks manually:

```bash
python -m pre_commit run --all-files
```

Configured hooks:

- Ruff linting with automatic fixes
- Ruff formatting
- trailing whitespace cleanup
- end-of-file fixing
- YAML syntax checks
- TOML syntax checks

## Configuration

The test suite reads configuration from environment variables:

| Variable | Default | Purpose |
| --- | --- | --- |
| `API_BASE_URL` | `https://jsonplaceholder.typicode.com` | Base URL for API requests |
| `API_TIMEOUT` | `10` | Request timeout in seconds |

Use `.env.example` as a reference:

```bash
API_BASE_URL=https://jsonplaceholder.typicode.com
API_TIMEOUT=10
```

Override values for one run:

```bash
API_BASE_URL=https://jsonplaceholder.typicode.com API_TIMEOUT=5 python -m pytest
```

## Running Checks

Run Ruff:

```bash
python -m ruff check .
python -m ruff format --check .
```

Run the full test suite:

```bash
python -m pytest
```

Run with verbose output:

```bash
python -m pytest -v
```

Run one test file:

```bash
python -m pytest tests/test_users.py -v
```

Run one test case:

```bash
python -m pytest tests/test_posts.py::TestPosts::test_get_post_by_id -v
```

## Test Markers

| Marker | Purpose |
| --- | --- |
| `smoke` | Fast checks for core endpoint availability |
| `contract` | Response structure and JSON Schema checks |
| `negative` | Expected error responses for missing resources |
| `regression` | Broader checks for documented behavior |

Run selected groups:

```bash
python -m pytest -m smoke
python -m pytest -m contract
python -m pytest -m negative
python -m pytest -m regression
python -m pytest -m "smoke or contract"
python -m pytest -m "not regression"
```

## Reports

Normal local runs do not generate HTML reports automatically.

Generate JUnit XML and an HTML report explicitly:

```bash
python -m pytest --junitxml=reports/junit.xml --html=reports/report.html --self-contained-html
```

The `reports/` directory contains generated artifacts and is excluded from version control.

## CI

GitHub Actions is configured in `.github/workflows/tests.yml`.

The workflow runs on pushes and pull requests to `main` and performs:

- repository checkout
- Python 3.12 setup
- pip dependency caching
- dependency installation
- Ruff lint and format checks
- pytest execution
- JUnit XML report generation
- HTML report generation
- report artifact upload

The workflow fails when linting or tests fail.

## Demo API Notes

JSONPlaceholder provides predictable public resources such as users and posts. This makes it suitable for demonstrating:

- request construction
- reusable fixtures
- response status assertions
- schema validation
- parametrized tests
- marker-based test selection
- CI report generation

Important limitations:

- write operations return successful responses but do not persist data
- request validation is intentionally limited
- data is static and publicly shared
- tests require internet access
- observed behavior belongs to JSONPlaceholder, not to this repository

## Design Notes

**Reusable API client:** `utils/api_client.py` keeps request construction, base URL handling, timeouts, logging, and status assertions in one place.

**Environment configuration:** `config/config.py` keeps endpoint and environment settings separate from test logic.

**Schema validation:** `utils/schemas.py` makes response structure expectations explicit without adding unnecessary abstraction.

**Public API target:** The test suite demonstrates API test automation practices without claiming production backend coverage.
