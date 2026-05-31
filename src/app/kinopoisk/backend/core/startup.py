from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import httpx

from app.kinopoisk.backend.handlers.api import api_main_router
from app.kinopoisk.backend.handlers.pages import pages_main_router
from app.kinopoisk.backend.core.routers import setup_routers
from app.kinopoisk.backend.core.exceptions import register_exceptions
from app.kinopoisk.backend.settings.paths import STATIC_DIR
from core.logging.setup import setup_logging
from core.logging.format import LogFormat


def create_app() -> FastAPI:
    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
        app.state.http_client = httpx.AsyncClient()
        yield
        await app.state.http_client.aclose()

    root_router = FastAPI(lifespan=lifespan)
    root_router.mount(
        path="/static",
        app=StaticFiles(directory=STATIC_DIR),
        name="static",
    )
    setup_routers(
        root_router=root_router, include_routers=[api_main_router, pages_main_router]
    )
    register_exceptions(root_router=root_router)

    setup_logging(fmt=LogFormat.FMT, date_fmt=LogFormat.DATE_FMT)
    return root_router
