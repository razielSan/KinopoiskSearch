import pytest

from app.kinopoisk.backend.clients.kinopoisk import KinopoiskApiClient
from app.kinopoisk.backend.dto.internal.movie import DataResponseModelDTO
from app.kinopoisk.backend.dto.external.kinopoisk import DataKinopoiskModelTop250DTO
from tests.base_clients import FakeBaseCleintTop250Movies


@pytest.mark.unit
@pytest.mark.asyncio
@pytest.mark.parametrize(
    "total, total_pages, "
    "kinopoisk_id, name_ru, "
    "poster_url_preview, genres, rating_kinopoisk",
    [
        (
            1,
            2,
            3,
            "test_name_ru",
            "test_rating_kinopoisk",
            [{"genre": "test"}],
            4,
        )
    ],
)
async def test_250_movies_success(
    total,
    total_pages,
    kinopoisk_id,
    name_ru,
    poster_url_preview,
    genres,
    rating_kinopoisk,
) -> None:
    clients = KinopoiskApiClient(
        client="test",
        api_client=FakeBaseCleintTop250Movies(
            total=total,
            total_pages=total_pages,
            kinopoisk_id=kinopoisk_id,
            name_ru=name_ru,
            poster_url_previiew=poster_url_preview,
            genres=genres,
            rating_kinopoisk=rating_kinopoisk,
        ),
    )

    result = await clients.get_top_250_movies(
        page=1, url_path="test", model=DataKinopoiskModelTop250DTO
    )
    assert isinstance(result, DataResponseModelDTO)
    assert result.total == total
    movie = result.movies[0]

    assert movie.kinopoisk_id == kinopoisk_id
    assert movie.genres == genres[0]["genre"]
    assert movie.rating == rating_kinopoisk
    assert movie.name == name_ru
    assert movie.rating == rating_kinopoisk
    assert movie.url_poster == poster_url_preview


@pytest.mark.unit
@pytest.mark.asyncio
@pytest.mark.parametrize(
    "rating, color",
    [
        (1, "red"),
        (6, "orange"),
        (9, "green"),
        (None, None),
    ],
)
async def test_validate_rating_color(rating, color) -> None:
    clients = KinopoiskApiClient(
        client="test",
        api_client=FakeBaseCleintTop250Movies(
            total=1,
            total_pages=1,
            kinopoisk_id=1,
            name_ru="test",
            poster_url_previiew="test",
            genres=[{"genre": "test"}],
            rating_kinopoisk=rating,
        ),
    )

    result = await clients.get_top_250_movies(
        page=1, url_path="test", model=DataKinopoiskModelTop250DTO
    )
    movie = result.movies[0]
    assert movie.rating == rating
    assert movie.rating_color == color
