from typing import NoReturn, Any, Dict

from app.kinopoisk.backend.domain.exceptions import ValidationAppError
from domain.exceptions import AppException
from domain.base_client import BaseClientInterface

class FakeHttp500ClientErrors(BaseClientInterface):
    async def _get_data_by_url(
        self, client: Any, url: str, headers: Dict[str, str], path: str
    ) -> NoReturn:
        raise AppException()

    def _check_response(self, response: Any, path: str) -> NoReturn:
        raise AssertionError("Функция никогда не должна быть вызвана")

    def _validate_data(self, data: Dict[str, Any], model: Any, path: str) -> NoReturn:
        raise AssertionError("Функция никогда не должна быть вызвана")


class FakeCheckResponseClientErrors(BaseClientInterface):
    async def _get_data_by_url(
        self, client: Any, url: str, headers: Dict[str, str], path: str
    ) -> bool:
        return True

    def _check_response(self, response: Any, path: str) -> NoReturn:
        raise ValidationAppError()

    def _validate_data(self, data: Dict[str, Any], model: Any, path: str) -> NoReturn:
        raise AssertionError("Функция никогда не должна быть вызвана")


class FakeCheckValidateData(BaseClientInterface):
    async def _get_data_by_url(
        self, client: Any, url: str, headers: Dict[str, str], path: str
    ) -> bool:
        return True

    def _check_response(self, response: Any, path: str) -> bool:
        return True

    def _validate_data(self, data: Dict[str, Any], model: Any, path: str) -> NoReturn:
        raise ValidationAppError()
