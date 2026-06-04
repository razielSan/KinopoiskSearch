from typing import Dict, Any, Type

import httpx

from app.kinopoisk.backend.dto.external.kinopoisk import (
    DataKinopoiskModelTop250DTO,
    DataKinopoiskModelSearchByNameDTO,
    KinopoiskModelInfoMovieDTO,
)
from app.kinopoisk.backend.dto.internal.movie import (
    DataResponseModelDTO,
    ResponseModelDTO,
    ResponseModelInfoMovieDTO,
)
from app.kinopoisk.backend.settings.settings import get_settings
from app.kinopoisk.backend.clients.base import BaseClient


class KinopoiskApiClient:
    def __init__(self, client: httpx.AsyncClient, api_client: BaseClient):
        self.client: httpx.AsyncClient = client
        self.api_client: BaseClient = api_client

    async def get_top_250_movies(
        self,
        page: int,
        url_path: str,
        model: Type[DataKinopoiskModelTop250DTO],
    ) -> DataResponseModelDTO:
        kinopoisk_settings = get_settings()
        response = await self.api_client._get_data_by_url(
            client=self.client,
            url=kinopoisk_settings.API_URL_TOP_250_MOVIES.format(page=page),
            headers=kinopoisk_settings.headers,
            path=url_path,
        )
        result_json: Dict[str, Any] = self.api_client._check_response(
            response=response,
            path=url_path,
        )

        validate_data: DataKinopoiskModelTop250DTO = self.api_client._validate_data(
            data=result_json,
            model=model,
            path=url_path,
        )
        validate_data
        movies = [
            ResponseModelDTO(
                kinopoisk_id=movie.kinopoiskId,
                name=movie.name,
                url_poster=movie.posterUrlPreview,
                rating=movie.ratingKinopoisk,
                genres=movie.genres,
            )
            for movie in validate_data.items
        ]
        return DataResponseModelDTO(
            total=validate_data.total,
            movies=movies,
        )

    async def get_search_movie_by_name(
        self,
        name: str,
        page: int,
        url_path: str,
        model: Type[DataKinopoiskModelSearchByNameDTO],
    ) -> DataResponseModelDTO:
        kinopoisk_settings = get_settings()
        response = await self.api_client._get_data_by_url(
            client=self.client,
            url=kinopoisk_settings.API_URL_SEARCH_MOVIE_BY_NAME.format(
                name=name,
                page=page,
            ),
            headers=kinopoisk_settings.headers,
            path=url_path,
        )

        result_json: Dict[str, Any] = self.api_client._check_response(
            response=response,
            path=url_path,
        )

        validate_data: DataKinopoiskModelSearchByNameDTO = (
            self.api_client._validate_data(
                data=result_json,
                model=model,
                path=url_path,
            )
        )
        movies = [
            ResponseModelDTO(
                kinopoisk_id=movie.filmId,
                url_poster=movie.posterUrlPreview,
                rating=movie.rating,
                genres=movie.genres,
                name=movie.name,
            )
            for movie in validate_data.films
        ]
        return DataResponseModelDTO(
            total=validate_data.pagesCount,
            movies=movies,
        )

    async def get_info_movie(
        self,
        film_id: int,
        url_path: str,
        model: Type[KinopoiskModelInfoMovieDTO],
    ) -> ResponseModelInfoMovieDTO:
        kinopoisk_settings = get_settings()
        response = await self.api_client._get_data_by_url(
            client=self.client,
            url=kinopoisk_settings.API_URL_MOVIE_KINIOPOISK_ID.format(
                id=film_id,
            ),
            headers=kinopoisk_settings.headers,
            path=url_path,
        )

        result_json: Dict[str, Any] = self.api_client._check_response(
            response=response,
            path=url_path,
        )
        validate_data: KinopoiskModelInfoMovieDTO = self.api_client._validate_data(
            data=result_json,
            model=model,
            path=url_path,
        )
        result = ResponseModelInfoMovieDTO(
            name=validate_data.name,
            year=validate_data.year,
            genres=validate_data.genres,
            site=validate_data.webUrl,
            url_poster=validate_data.posterUrlPreview,
            description=validate_data.description,
            film_length=validate_data.filmLength,
        )
        return result
