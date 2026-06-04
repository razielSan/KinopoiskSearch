import pytest

from app.kinopoisk.backend.clients.kinopoisk import KinopoiskApiClient
from app.kinopoisk.backend.dto.external.kinopoisk import (
    DataKinopoiskModelSearchByNameDTO,
)
from app.kinopoisk.backend.dto.internal.movie import DataResponseModelDTO
from tests.base_clients import FakeBaseCleintSearchMovieByName


@pytest.mark.unit
@pytest.mark.asyncio
@pytest.mark.parametrize(
    "pages_count, film_id, poster_url_preview, name_ru, name_en, genres, rating",
    [(1, 2, "test url", "test name ru", "test name en", [{"genre": "test genre"}], 3)],
)
async def test_search_movies_by_name_success(
    pages_count, film_id, poster_url_preview, name_ru, name_en, genres, rating
) -> None:
    client = KinopoiskApiClient(
        client="test",
        api_client=FakeBaseCleintSearchMovieByName(
            pages_count=pages_count,
            film_id=film_id,
            poster_url_preview=poster_url_preview,
            name_ru=name_ru,
            name_en=name_en,
            genres=genres,
            rating=rating,
        ),
    )
    result = await client.get_search_movie_by_name(
        name="test_name",
        page=10,
        url_path="test url path",
        model=DataKinopoiskModelSearchByNameDTO,
    )
    movie = result.movies[0]
    assert isinstance(result, DataResponseModelDTO)
    assert result.total == pages_count
    assert movie.genres == genres[0]["genre"]
    assert movie.kinopoisk_id == film_id
    assert movie.url_poster == poster_url_preview
    assert movie.name == name_ru
    assert movie.rating == rating


@pytest.mark.unit
@pytest.mark.asyncio
@pytest.mark.parametrize(
    "rating, color",
    [
        (0, "red"),
        (4.9, "red"),
        (5, "orange"),
        (7.9, "orange"),
        (8, "green"),
        (10, "green"),
        (None, None),
    ],
)
async def test_validate_rating_color(rating, color) -> None:
    client = KinopoiskApiClient(
        client="test",
        api_client=FakeBaseCleintSearchMovieByName(
            pages_count=1,
            film_id=2,
            poster_url_preview="test_url",
            name_ru="test name ru",
            name_en="test name en",
            genres=[{"genre": "test genre"}],
            rating=rating,
        ),
    )
    result = await client.get_search_movie_by_name(
        name="test_name",
        page=10,
        url_path="test url path",
        model=DataKinopoiskModelSearchByNameDTO,
    )
    movie = result.movies[0]
    assert isinstance(result, DataResponseModelDTO)
    assert movie.rating == rating
    assert movie.rating_color == color


@pytest.mark.unit
@pytest.mark.asyncio
@pytest.mark.parametrize(
    "name_ru, name_en, name, genres",
    [
        (
            "test name ru",
            "test name en",
            "test name ru",
            [{"genre": "genre1"}, {"genre": "genre2"}],
        ),
        (
            None,
            "test name en",
            "test name en",
            [{"genre": "genre3"}, {"genre": "genre4"}],
        ),
    ],
)
async def test_validate_fields(name_ru, name_en, name, genres):
    client = KinopoiskApiClient(
        client="test",
        api_client=FakeBaseCleintSearchMovieByName(
            pages_count=1,
            film_id=2,
            poster_url_preview="test_url",
            name_ru=name_ru,
            name_en=name_en,
            genres=genres,
            rating=3,
        ),
    )
    result = await client.get_search_movie_by_name(
        name="test_name",
        page=10,
        url_path="test url path",
        model=DataKinopoiskModelSearchByNameDTO,
    )

    movie = result.movies[0]
    assert isinstance(result, DataResponseModelDTO)
    genre1 = genres[0]["genre"]
    genre2 = genres[1]["genre"]
    assert movie.name == name
    assert genre1 in movie.genres
    assert genre2 in movie.genres
