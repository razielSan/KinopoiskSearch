from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.responses import JSONResponse as StarletteJsonResponse

from domain.exceptions import AppException


def register_exceptions(
    root_router: FastAPI,
) -> None:
    @root_router.exception_handler(AppException)
    async def validation_error(
        request: Request,
        exc: AppException,
    ) -> StarletteJsonResponse:
        return JSONResponse(
            status_code=exc.status_code,
            content={"code": exc.code, "message": exc.user_message},
        )
