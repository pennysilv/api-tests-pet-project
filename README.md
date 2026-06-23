# API Testing Pet Project

[![Tests](https://github.com/pennysilv/api-tests-pet-project/actions/workflows/tests.yml/badge.svg)](https://github.com/pennysilv/api-tests-pet-project/actions)

Automated REST API testing project for [JSONPlaceholder](https://jsonplaceholder.typicode.com), built with Python, pytest, and requests.

The project demonstrates API test design, positive and negative testing, boundary-value analysis, parameterization, response validation, and automated test execution.

## Project Overview

This repository contains automated tests for the JSONPlaceholder REST API.

The test suite validates user and post endpoints, including:

* successful GET requests;
* resource retrieval by ID;
* filtering resources by query parameters;
* POST requests with valid and invalid payloads;
* handling of non-existent resources;
* boundary and negative scenarios;
* validation of related API data.

## Technology Stack

* **Python 3**
* **pytest** — test framework
* **requests** — HTTP client library
* **pytest-html** — HTML test report generation
* **GitHub Actions** — automated test execution

## Test Coverage

### User Endpoints

Tests in `test_users.py` cover:

* `GET /users` — retrieve all users;
* `GET /users/{id}` — retrieve a user by ID;
* `GET /users/999` — verify handling of a non-existent user;
* `POST /users` — create a new user.

### Post Endpoints

Tests in `test_posts.py` cover:

* `GET /posts` — retrieve all posts;
* `GET /posts/{id}` — retrieve a post by ID;
* `GET /posts?userId={id}` — retrieve posts associated with a specific user;
* `POST /posts` — create a new post.

### Parameterized Tests

Tests in `test_parametrized.py` include:

* validation of five different user IDs;
* validation of five different post IDs;
* negative scenarios with invalid resource IDs;
* verification of relationships between users and posts.

### Boundary and Input Validation Tests

Tests in `test_boundary.py` cover:

* minimum and maximum valid IDs;
* IDs outside the expected range;
* zero and negative IDs;
* empty fields;
* long string values;
* special characters and Unicode input;
* SQL-like input strings.

## Test Suite

The project currently contains **40 automated tests**.

The tests verify:

* HTTP status codes;
* JSON response structure;
* response field values;
* request and response data consistency;
* API behaviour for positive, negative, and boundary scenarios.

## Project Structure

```text
api-tests-pet-project/
├── tests/
│   ├── test_users.py
│   ├── test_posts.py
│   ├── test_parametrized.py
│   └── test_boundary.py
├── requirements.txt
├── pytest.ini
└── README.md
```

Update this section if the actual repository structure is different.

## Getting Started

### Prerequisites

* Python 3.9 or later
* Git

### Installation

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
test_env\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

If the project is configured as an installable Python package, also run:

```bash
pip install -e .
```

## Running the Tests

Run the complete test suite:

```bash
pytest -v
```

Run a specific test module:

```bash
pytest tests/test_users.py -v
```

Run tests and generate an HTML report:

```bash
pytest -v --html=report.html --self-contained-html
```

The generated report will be saved as:

```text
report.html
```

## Continuous Integration

The test suite is configured to run automatically with GitHub Actions.

The workflow can be used to:

* install project dependencies;
* execute the pytest test suite;
* detect test failures on repository updates;
* verify that the project remains stable after changes.

## Key QA Practices Demonstrated

* REST API testing
* Positive and negative testing
* Boundary-value analysis
* Parameterized testing
* HTTP status code validation
* JSON response validation
* Test data validation
* Automated test reporting
* Continuous integration

## Possible Improvements

Future improvements may include:

* adding `PUT`, `PATCH`, and `DELETE` request coverage;
* introducing reusable fixtures for test data and API clients;
* adding JSON Schema validation;
* separating configuration from test logic;
* generating Allure reports;
* adding test execution for multiple Python versions;
* expanding response-time and performance checks.

## Author

**Polina Serebrennikova**

* GitHub: [pennysilv](https://github.com/pennysilv)
