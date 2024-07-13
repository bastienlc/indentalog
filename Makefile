install:
	poetry install
	poetry run pre-commit install
	sudo apt-get install ttyrec ttygif

build:
	poetry build

publish:
	poetry publish --build

test:
	poetry run pytest

lint:
	poetry run black progress_decorator/
	poetry run isort progress_decorator/

gifs:
	bash assets/record.sh
