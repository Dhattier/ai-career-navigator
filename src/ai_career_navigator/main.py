import logging

from fastapi import FastAPI

from ai_career_navigator.config import settings
from ai_career_navigator.core.logging import configure_logging

configure_logging()

logger = logging.getLogger(__name__)

app = FastAPI(title=settings.app_name)


@app.get("/health")
async def health() -> dict[str, str]:
    logger.info("Health check requested")
    return {"status": "ok"}
