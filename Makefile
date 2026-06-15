dev:
	uv run uvicorn ai_career_navigator.main:app --reload

test:
	uv run pytest

lint:
	uv run ruff check .
	uv run mypy src tests

format:
	uv run ruff format .
	uv run ruff check . --fix

up:
	docker compose up --build

down:
	docker compose down