from fastapi import FastAPI

from ai_career_navigator.api.routes import router
from ai_career_navigator.config import settings
from ai_career_navigator.core.logging import configure_logging

configure_logging()

app = FastAPI(title=settings.app_name)

app.include_router(router, prefix="/api/v1")
