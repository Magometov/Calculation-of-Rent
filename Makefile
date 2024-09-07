lint:
	poetry run black .
	poetry run ruff check .
	poetry run isort .

build-dev:
	docker-compose -f docker-compose.yml up -d --build
