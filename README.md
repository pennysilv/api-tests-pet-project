# Python API Testing Framework

[![Tests](https://github.com/pennysilv/python-api-test-framework/actions/workflows/tests.yml/badge.svg)](https://github.com/pennysilv/python-api-test-framework/actions)

A lightweight REST API automation framework built with Python, pytest and requests. It demonstrates modern API testing practices including reusable API clients, schema validation, environment-based configuration and GitHub Actions.

This repository is a portfolio project for Junior QA Automation interviews. It is intentionally compact, readable and honest about its scope.

## Features

✔ REST API automation

✔ Reusable API client

✔ JSON Schema validation

✔ Environment configuration

✔ CRUD examples

✔ Pytest markers

✔ HTML reports

✔ GitHub Actions CI

✔ Logging

## Architecture

The project separates test intent from HTTP implementation details:

- `tests/` contains readable pytest test cases grouped by API behavior.
- `utils/api_client.py` provides a small reusable wrapper around `requests`.
- `utils/schemas.py` stores JSON Schema definitions used for response validation.
- `config/config.py` centralizes base URL, timeout and endpoint settings.
- `.github/workflows/tests.yml` runs linting and tests in CI.

The structure is deliberately simple so interviewers can quickly understand the automation approach without navigating an oversized framework.

## Project Structure

```text
python-api-test-framework/
├── .github/
│   └── workflows/
│       └── tests.yml          # GitHub Actions workflow for linting, tests and reports
├── config/
│   ├── __init__.py
│   └── config.py             # Environment-based API configuration
├── tests/
│   ├── conftest.py           # Shared pytest fixtures and logging setup
│   ├── test_boundary.py      # Boundary-style checks for known resource IDs
│   ├── test_parametrized.py  # Parametrized API test examples
│   ├── test_posts.py         # Posts endpoint tests
│   └── test_users.py         # Users endpoint tests
├── utils/
│   ├── __init__.py
│   ├── api_client.py         # Reusable HTTP client
│   └── schemas.py            # JSON Schema definitions
├── .env.example              # Example environment variables
├── .gitignore
├── .pre-commit-config.yaml   # Local quality checks before commit
├── pyproject.toml            # Project metadata and Ruff configuration
├── pytest.ini                # Pytest discovery, markers and default report options
├── requirements.txt          # Runtime and test dependencies
└── README.md
```

## Technologies

- **Python 3.12**
- **pytest** for test execution
- **requests** for HTTP communication
- **jsonschema** for response schema validation
- **pytest-html** for HTML reports
- **Ruff** for linting and formatting checks
- **pre-commit** for local quality gates
- **GitHub Actions** for CI/CD

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
python -m pip install -e .
```

Optional local pre-commit setup:

```bash
pre-commit install
```

## Configuration

The framework reads configuration from environment variables:

| Variable | Default | Purpose |
| --- | --- | --- |
| `API_BASE_URL` | See `config/config.py` | Base URL for API requests |
| `API_TIMEOUT` | `10` | Request timeout in seconds |

Use `.env.example` as a reference:

```bash
API_BASE_URL=https://example.test
API_TIMEOUT=10
```

Override values for one run:

```bash
API_BASE_URL=https://example.test API_TIMEOUT=5 pytest
```

## Running Tests

Run Ruff:

```bash
ruff check .
ruff format --check .
```

Run the full test suite:

```bash
pytest
```

Run with verbose output:

```bash
pytest -v
```

Run one test file:

```bash
pytest tests/test_users.py -v
```

Run one test case:

```bash
pytest tests/test_posts.py::TestPosts::test_get_post_by_id -v
```

## Test Markers

The test suite uses these pytest markers:

| Marker | Purpose |
| --- | --- |
| `smoke` | Fast checks for core endpoint availability |
| `contract` | Response structure and JSON Schema checks |
| `negative` | Expected error responses for missing resources |
| `regression` | Broader checks for existing documented behavior |

Run selected groups:

```bash
pytest -m smoke
pytest -m contract
pytest -m negative
pytest -m regression
pytest -m "smoke or contract"
pytest -m "not regression"
```

## Reports

The project uses `pytest-html` for local HTML reports.

The default pytest configuration creates:

```text
reports/report.html
```

Generate both JUnit XML and HTML reports, matching CI:

```bash
pytest --junitxml=reports/junit.xml --html=reports/report.html --self-contained-html
```

The `reports/` directory contains generated artifacts and is excluded from version control.

## CI/CD

GitHub Actions is configured in `.github/workflows/tests.yml`.

The workflow runs on pushes and pull requests to `main` and performs:

- checkout with the current GitHub-supported action version;
- Python 3.12 setup;
- pip dependency caching;
- dependency installation;
- Ruff lint and format checks;
- pytest execution;
- JUnit XML report generation;
- HTML report generation;
- report artifact upload.

The workflow fails when linting or tests fail, which keeps the repository feedback clear for reviewers.

## Demo API

This project uses [JSONPlaceholder](https://jsonplaceholder.typicode.com) as a stable public endpoint for demonstrating API automation techniques.

JSONPlaceholder is useful for portfolio testing because it provides predictable REST resources such as users and posts. It is not a real backend owned by this project, and the tests do not prove backend validation, data persistence or business rules.

Default local configuration:

```bash
API_BASE_URL=https://jsonplaceholder.typicode.com
API_TIMEOUT=10
```

Important limitations:

- write operations return successful responses but do not persist data;
- request validation is intentionally limited;
- data is static and publicly shared;
- tests require internet access;
- observed behavior belongs to the public service, not to this repository.

## Design Decisions

**Reusable API client:** The client keeps request construction, base URL handling, timeouts, logging and status assertions in one place. This makes tests shorter and easier to read.

**Environment configuration:** Base URL and timeout values can change without editing tests. This mirrors how QA automation projects usually separate test code from environment details.

**Schema validation:** JSON Schema checks make response structure expectations explicit. They are useful for catching contract-style changes beyond status codes.

**Public endpoint limitations:** The target API is intentionally limited. The tests demonstrate automation patterns, but they do not claim full backend coverage or production readiness.

## What This Project Demonstrates

- REST API test automation with Python and pytest.
- Reusable fixtures and a small API client layer.
- Positive, negative, boundary-style and parametrized tests.
- JSON Schema validation for important response shapes.
- Environment-based configuration.
- Clear pytest marker usage.
- Local HTML report generation.
- CI execution with linting, test reports and uploaded artifacts.
- Practical understanding of the limits of testing against a public API.

This is a focused Junior QA Automation portfolio project, not an enterprise test platform.
