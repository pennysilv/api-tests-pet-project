# API Testing Portfolio Project

[![Tests](https://github.com/pennysilv/api-tests-pet-project/actions/workflows/tests.yml/badge.svg)](https://github.com/pennysilv/api-tests-pet-project/actions)

Automated REST API testing project built with Python, pytest, and requests.

This project uses [JSONPlaceholder](https://jsonplaceholder.typicode.com), a fake public REST API, as a stable demo target for practicing and presenting API test automation patterns. It is not intended to prove the quality of a real production backend. The value of the project is in the test structure, reusable client layer, pytest usage, assertions, reporting, and CI setup.

## Project Purpose

The goal is to demonstrate how a junior QA automation engineer can organize and run API tests against REST endpoints.

The tests cover examples around:

* basic API availability checks;
* response status validation;
* response body and field validation;
* simple request payloads;
* parameterized test cases;
* boundary-style behavior for known resource IDs;
* negative examples for resources that do not exist.

## Tech Stack

* **Python 3.9+**
* **pytest** for test execution
* **requests** for HTTP calls
* **jsonschema** for response schema validation
* **pytest-html** for HTML reports
* **GitHub Actions** for CI execution

## Test Categories

### Smoke

Fast checks that confirm the main public endpoints respond successfully, such as:

* `GET /users`
* `GET /users/{id}`
* `GET /posts`
* `GET /posts/{id}`

### Contract / Schema-Style Checks

The current tests verify expected response fields such as `id`, `name`, `email`, `title`, `body`, and `userId`.

JSON Schema checks are used for key user and post responses.

### CRUD-Style Examples

JSONPlaceholder supports fake write operations, so this project includes examples such as:

* `POST /users`
* `POST /posts`
* `PUT /posts/{id}`
* `PATCH /posts/{id}`
* `DELETE /posts/{id}`

These tests demonstrate request construction and response validation. JSONPlaceholder does not persist created resources, so these are not full end-to-end CRUD tests against a real database.

### Boundary Behavior

Boundary-style tests check known valid and invalid resource IDs, for example:

* first and last expected user IDs;
* first and last expected post IDs;
* zero, negative, and out-of-range IDs.

These tests document observed JSONPlaceholder behavior. They should not be interpreted as validation rules for a real backend.

## JSONPlaceholder Limitations

JSONPlaceholder is useful for demo automation, but it has important limitations:

* it is a fake public API, not a production system;
* write operations return successful responses but do not persist data;
* input validation is intentionally limited;
* business rules are minimal;
* data is static and publicly shared;
* tests depend on internet access and the availability of a third-party service.

Because of this, the project should be read as an automation portfolio sample, not as evidence that a real API has been tested comprehensively.

## Project Structure

```text
api-tests-pet-project/
├── .github/
│   └── workflows/
│       └── tests.yml
├── config/
│   ├── __init__.py
│   └── config.py
├── .env.example
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
├── pytest.ini
├── requirements.txt
├── setup.py
└── README.md
```

## Setup

Clone the repository:

```bash
git clone https://github.com/pennysilv/api-tests-pet-project.git
cd api-tests-pet-project
```

Create and activate a virtual environment:

```bash
python3 -m venv test_env
source test_env/bin/activate
```

On Windows:

```powershell
python -m venv test_env
test_env\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Optionally install the project in editable mode:

```bash
pip install -e .
```

### Configuration

The framework reads configuration from environment variables:

* `API_BASE_URL`
* `API_TIMEOUT`

Default values are defined in `config/config.py`, so the tests run against JSONPlaceholder without extra setup.

Use `.env.example` as a reference:

```bash
API_BASE_URL=https://jsonplaceholder.typicode.com
API_TIMEOUT=10
```

To override values for one test run:

```bash
API_BASE_URL=https://jsonplaceholder.typicode.com API_TIMEOUT=5 pytest
```

## Running Tests

Run the full test suite:

```bash
pytest
```

Run with verbose output:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest tests/test_users.py -v
```

Run a specific test by name:

```bash
pytest tests/test_posts.py::TestPosts::test_get_post_by_id -v
```

### Marker-Based Runs

The test suite uses these pytest markers:

* `smoke`
* `contract`
* `negative`
* `regression`

Run selected categories:

```bash
pytest -m smoke
pytest -m contract
pytest -m negative
pytest -m regression
```

To exclude slow or broader checks:

```bash
pytest -m "smoke or contract"
pytest -m "not regression"
```

## Reports

The project uses `pytest-html`.

The default pytest configuration generates an HTML report at:

```text
reports/report.html
```

Run tests and generate the default report:

```bash
pytest
```

Generate a custom report:

```bash
pytest -v --html=reports/api_report.html --self-contained-html
```

The `reports/` directory is intended for generated artifacts and should not be committed.

## Continuous Integration

GitHub Actions is configured in:

```text
.github/workflows/tests.yml
```

The workflow installs dependencies and runs the pytest suite on pushes and pull requests to `main`.

Current CI coverage is intentionally simple. Useful improvements would include:

* pinning a specific Python version or running a small version matrix;
* caching pip dependencies;
* uploading HTML or JUnit test reports as CI artifacts;
* adding linting with tools such as ruff;
* separating smoke checks from the full suite.

## What This Project Demonstrates For Interviews

This project demonstrates:

* organizing API tests with pytest;
* using fixtures for a reusable API client;
* reading base URL and timeout settings from environment variables;
* separating configuration, utilities, and test cases;
* writing readable positive, negative, parameterized, and boundary-style tests;
* using JSON Schema validation for important response shapes;
* validating response status codes and response bodies;
* generating test reports;
* running tests in CI;
* understanding the limits of testing against a public fake API.

It is a compact portfolio project, not a complete enterprise API framework.

## Possible Improvements

Good next improvements include:

* adding more detailed schemas for nested user fields;
* loading local `.env` files with `python-dotenv` if desired;
* adding clearer reusable assertion helpers;
* adding JUnit XML output for CI;
* improving CI artifacts and reporting.

## Author

**Polina Serebrennikova**

* GitHub: [pennysilv](https://github.com/pennysilv)
