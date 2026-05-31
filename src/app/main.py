import uvicorn

from fastapi import FastAPI

from app.kinopoisk.backend.core.startup import create_app
from app.settings import settings as app_settings


app: FastAPI = create_app()


def run() -> None:
    uvicorn.run(
        app=app_settings.APP,
        reload=app_settings.RELOAD,
        port=app_settings.PORT,
        host=app_settings.HOST,
    )
