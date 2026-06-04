import pytest

from app.kinopoisk.backend.domain.exceptions import ValidationAppError
from domain.exceptions import AppException
from app.kinopoisk.backend.clients.kinopoisk import KinopoiskApiClient
from app.kinopoisk.backend.dto.external.kinopoisk import DataKinopoiskModelTop250DTO
from tests.errors import (
    FakeCheckResponseClientErrors,
    FakeHttp500ClientErrors,
    FakeCheckValidateData,
)


@pytest.mark.unit
@pytest.mark.asyncio
async def test_http_500_errors() -> None:
    with pytest.raises(AppException) as exc:
        client = KinopoiskApiClient(
            client="test",
            api_client=FakeHttp500ClientErrors(),
        )
        await client.get_top_250_movies(
            page=1, url_path="test", model=DataKinopoiskModelTop250DTO
        )
    assert exc.value.status_code == AppException().status_code
    assert exc.value.code == AppException().code
    assert exc.value.message == AppException().message


@pytest.mark.unit
@pytest.mark.asyncio
async def test_check_response() -> None:
    with pytest.raises(ValidationAppError) as exc:
        client = KinopoiskApiClient(
            client="test", api_client=FakeCheckResponseClientErrors()
        )
        await client.get_top_250_movies(
            page=1, url_path="test", model=DataKinopoiskModelTop250DTO
        )
    assert exc.value.status_code == ValidationAppError().status_code
    assert exc.value.code == ValidationAppError().code
    assert exc.value.message == ValidationAppError().message


@pytest.mark.unit
@pytest.mark.asyncio
async def test_check_validate_data() -> None:
    with pytest.raises(ValidationAppError) as exc:
        client = KinopoiskApiClient(client="test", api_client=FakeCheckValidateData())
        await client.get_top_250_movies(
            page=1, url_path="test", model=DataKinopoiskModelTop250DTO
        )
    assert exc.value.status_code == ValidationAppError().status_code
    assert exc.value.code == ValidationAppError().code
    assert exc.value.message == ValidationAppError().message
