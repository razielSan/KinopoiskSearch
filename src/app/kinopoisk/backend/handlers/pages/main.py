from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse

from app.kinopoisk.backend.core.extensions import templates

router = APIRouter(tags=["main"])


@router.get("/")
def get_main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        "index.html",
        {"request": request},
    )
