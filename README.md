# AI Career Navigator

AI Career Navigator is an Applied AI Engineering project that analyzes AI and Data Science job market trends using a combination of structured analytics and Retrieval-Augmented Generation (RAG).

## Project Goal

Build a production-oriented Applied AI platform that combines structured analytics and Retrieval-Augmented Generation (RAG) to help users understand AI hiring trends, skill demand, and job requirements.

## Current Status

Project is in active development.

Current features:

- FastAPI application
- Configuration management with Pydantic Settings
- Automated testing with pytest
- Linting with Ruff

## Tech Stack

- Python 3.12
- FastAPI
- Pydantic
- UV
- Pytest
- Ruff

## Run Locally

```bash
uv sync
uv run uvicorn ai_career_navigator.main:app --reload
```

## The API will be available at:

```text
http://127.0.0.1:8000
```

## Interactive docs:

```text
http://127.0.0.1:8000/docs
```

## Run Tests

```bash
uv run pytest
```