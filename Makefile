install:
	poetry install
	poetry run pre-commit install

build:
	poetry build

publish:
	poetry publish --build

test:
	poetry run pytest

lint:
	poetry run black progress_decorator/
	poetry run isort progress_decorator/
