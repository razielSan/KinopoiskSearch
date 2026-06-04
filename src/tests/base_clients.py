from typing import Any, Dict, List, Optional, Mapping

from domain.base_client import BaseClientInterface


class FakeBaseCleintTop250Movies(BaseClientInterface):
    def __init__(
        self,
        total: int,
        total_pages: int,
        kinopoisk_id: int,
        name_ru: str,
        poster_url_previiew: str,
        genres: List[Dict[str, str]],
        rating_kinopoisk: int,
    ) -> None:
        self.total = total
        self.total_pages = total_pages
        self.kinopoisk_id = kinopoisk_id
        self.name_ru = name_ru
        self.poster_url_previeiw = poster_url_previiew
        self.genres = genres
        self.rating_kinopoisk = rating_kinopoisk

    async def _get_data_by_url(
        self,
        client: Any,
        url: str,
        headers: Mapping[str, str],
        path: str,
    ) -> bool:
        return True

    def _check_response(
        self,
        response: Any,
        path: str,
    ) -> Dict[str, Any]:
        return {
            "total": self.total,
            "totalPages": self.total_pages,
            "items": [
                {
                    "kinopoiskId": self.kinopoisk_id,
                    "nameRu": self.name_ru,
                    "posterUrlPreview": self.poster_url_previeiw,
                    "ratingKinopoisk": self.rating_kinopoisk,
                    "genres": self.genres,
                }
            ],
        }

    def _validate_data(
        self,
        data: Dict[str, Any],
        model: Any,
        path: str,
    ) -> Any:
        validate_data = model.model_validate(data)
        return validate_data


class FakeBaseCleintInfoMovie(BaseClientInterface):
    def __init__(
        self,
        name_ru: Optional[str],
        name_original: Optional[str],
        year: int,
        web_url: str,
        poster_url_preview: str,
        description: Optional[str],
        film_length: Optional[int],
        genres: List[Dict[str, str]],
    ) -> None:
        self.name_ru = name_ru
        self.year = year
        self.name_origingal = name_original
        self.genres = genres
        self.web_url = web_url
        self.poster_url_prview = poster_url_preview
        self.description = description
        self.film_length = film_length

    async def _get_data_by_url(
        self,
        client: Any,
        url: str,
        headers: Mapping[str, str],
        path: str,
    ) -> bool:
        return True

    def _check_response(
        self,
        response: Any,
        path: str,
    ) -> Dict[str, Any]:
        return {
            "nameRu": self.name_ru,
            "nameOriginal": self.name_origingal,
            "year": self.year,
            "genres": self.genres,
            "webUrl": self.web_url,
            "posterUrlPreview": self.poster_url_prview,
            "description": self.description,
            "filmLength": self.film_length,
        }

    def _validate_data(
        self,
        data: Dict[str, Any],
        model: Any,
        path: str,
    ) -> Any:
        validate_data = model.model_validate(data)
        return validate_data


class FakeBaseCleintSearchMovieByName(BaseClientInterface):
    def __init__(
        self,
        pages_count: int,
        film_id: int,
        poster_url_preview: str,
        genres: Dict[str, str],
        name_ru: str,
        name_en: str,
        rating: int,
    ):
        self.page_count = pages_count
        self.film_id = film_id
        self.poster_url_preview = poster_url_preview
        self.genres = genres
        self.name_ru = name_ru
        self.name_en = name_en
        self.rating = rating

    async def _get_data_by_url(
        self,
        client: Any,
        url: str,
        headers: Mapping[str, str],
        path: str,
    ) -> bool:
        return True

    def _check_response(
        self,
        response: Any,
        path: str,
    ) -> Dict[str, Any]:
        return {
            "pagesCount": self.page_count,
            "films": [
                {
                    "filmId": self.film_id,
                    "nameRu": self.name_ru,
                    "nameEn": self.name_en,
                    "rating": self.rating,
                    "posterUrlPreview": self.poster_url_preview,
                    "genres": self.genres,
                }
            ],
        }

    def _validate_data(
        self,
        data: Dict[str, Any],
        model: Any,
        path: str,
    ) -> Any:
        validate_data = model.model_validate(data)
        return validate_data
