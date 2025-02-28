# gh-actions-python-03

## API Response Validator with GitHub Actions

This project fetches API responses, validates them, and ensures correctness with unit testing.  
It uses **pytest** for testing, **pytest-cov** for test coverage measurement, and **Ruff** for linting and formatting.

## Features

- Fetches data from an API.
- Unit testing with `pytest`.
- Test coverage reports using `pytest-cov`.
- Code linting and formatting with `Ruff`.
- Automated CI/CD with GitHub Actions.

## Setup

Install dependencies:

```sh
pip3 install -r requirements.txt
```

(Optional) Check and format code with Ruff:

```sh
ruff check .
ruff format .
```

(Optional) Run tests:

```sh
pytest --cov
```

Run the application:

```sh
python3 app.py
```
