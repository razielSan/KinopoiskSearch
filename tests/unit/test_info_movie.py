import pytest

from app.kinopoisk.backend.clients.kinopoisk import KinopoiskApiClient
from app.kinopoisk.backend.dto.internal.movie import ResponseModelInfoMovieDTO
from app.kinopoisk.backend.dto.external.kinopoisk import KinopoiskModelInfoMovieDTO
from tests.base_clients import FakeBaseCleintInfoMovie

@pytest.mark.unit
@pytest.mark.asyncio
@pytest.mark.parametrize(
    "name_ru, name_original, year, web_url"
    ", poster_url_preview, description, film_length, genres",
    [
        (
            "test_name_ru",
            "test_name_original",
            1,
            "test_url",
            "test_poster",
            "test_description",
            2,
            [{"genre": "test"}],
        )
    ],
)
async def test_search_movies_by_name_success(
    name_ru,
    name_original,
    year,
    web_url,
    poster_url_preview,
    description,
    film_length,
    genres,
) -> None:
    clients = KinopoiskApiClient(
        client="test",
        api_client=FakeBaseCleintInfoMovie(
            name_ru=name_ru,
            name_original=name_original,
            year=year,
            web_url=web_url,
            poster_url_preview=poster_url_preview,
            description=description,
            film_length=film_length,
            genres=genres,
        ),
    )

    result = await clients.get_info_movie(
        film_id=1, model=KinopoiskModelInfoMovieDTO, url_path="test"
    )
    assert isinstance(result, ResponseModelInfoMovieDTO)
    assert result.year == str(year)
    assert result.name == name_ru
    assert result.description == f"{description}..."
    assert result.film_length == str(film_length)
    assert result.genres == genres[0]["genre"]
    assert result.site == web_url
    assert result.url_poster == poster_url_preview

@pytest.mark.unit
@pytest.mark.asyncio
async def test_check_fields() -> None:
    name_en = "test_name_en"
    
    genre1 = "test1"
    genre2 = "test2"
    genres = [{"genre": genre1}, {"genre": genre2}]
    clients = KinopoiskApiClient(
        client="test",
        api_client=FakeBaseCleintInfoMovie(
            name_ru=None,
            name_original=name_en,
            year=None,
            web_url="test",
            poster_url_preview="test",
            description=None,
            film_length=None,
            genres=genres,
        ),
    )

    result = await clients.get_info_movie(
        film_id=1, model=KinopoiskModelInfoMovieDTO, url_path="test"
    )
    assert result.year == "Неизвестно"
    assert result.film_length == "Неизвестно"
    assert result.description == "Нет описания"
    assert result.name == name_en
    assert isinstance(result.genres, str)
    assert genre1 in result.genres
    assert genre2 in result.genres
