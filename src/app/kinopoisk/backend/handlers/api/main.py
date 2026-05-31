import httpx
from fastapi import APIRouter, Depends

from app.kinopoisk.backend.core.dependecies import get_http_client

from app.kinopoisk.backend.dto.internal.movie import (
    DataResponseModelDTO,
    ResponseModelInfoMovieDTO,
)
from app.kinopoisk.backend.clients.kinopoisk import KinopoiskApiClient
from app.kinopoisk.backend.clients.base import BaseClient

router = APIRouter(tags=["api"])


class UrlPaths:
    API_TOP_250: str = "/api/get/top-250"
    API_SEARCH_BY_NAME: str = "/api/get/search-by-name"
    API_MOVIE: str = "/api/get/movie"


@router.get(
    path=UrlPaths.API_TOP_250,
    response_model=DataResponseModelDTO,
)
async def get_top_250_movies(
    page: int,
    client: httpx.AsyncClient = Depends(get_http_client),
) -> DataResponseModelDTO:
    kinopoisk_client: KinopoiskApiClient = KinopoiskApiClient(
        client=client,
        api_client=BaseClient(),
    )
    return await kinopoisk_client.get_top_250_movies(
        page=page,
        url_path=f"{UrlPaths.API_TOP_250}?page={page}",
    )


@router.get(
    path=UrlPaths.API_SEARCH_BY_NAME,
    response_model=DataResponseModelDTO,
)
async def get_movie_search_movie_by_name(
    name: str,
    page: int,
    client: httpx.AsyncClient = Depends(get_http_client),
) -> DataResponseModelDTO:
    kinopoisk_client: KinopoiskApiClient = KinopoiskApiClient(
        client=client,
        api_client=BaseClient(),
    )
    return await kinopoisk_client.get_search_movie_by_name(
        page=page,
        name=name,
        url_path=f"{UrlPaths.API_SEARCH_BY_NAME}?name={name}&page={page}",
    )


@router.get(
    UrlPaths.API_MOVIE,
    response_model=ResponseModelInfoMovieDTO,
)
async def get_movie_info(
    film_id: int,
    client: httpx.AsyncClient = Depends(get_http_client),
) -> ResponseModelInfoMovieDTO:
    kinopoisk_client: KinopoiskApiClient = KinopoiskApiClient(
        client=client,
        api_client=BaseClient(),
    )
    return await kinopoisk_client.get_info_movie(
        film_id=film_id,
        url_path=f"{UrlPaths.API_SEARCH_BY_NAME}?id={film_id}",
    )
