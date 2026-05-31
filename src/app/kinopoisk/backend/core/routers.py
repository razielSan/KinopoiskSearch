from typing import Sequence
from fastapi import APIRouter, FastAPI


def setup_routers(
    root_router: FastAPI,
    include_routers: Sequence[APIRouter],
) -> None:
    for router in include_routers:
        root_router.include_router(router)
