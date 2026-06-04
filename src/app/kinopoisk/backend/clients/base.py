import logging
from typing import Dict, Type, TypeVar, Any, Mapping

import httpx
import pydantic

from app.kinopoisk.backend.domain.exceptions import (
    format_errors_message,
    get_error_details,
    ValidationAppError,
)
from domain.exceptions import AppException
from domain.base_client import BaseClientInterface


T = TypeVar("T", bound=pydantic.BaseModel)


class BaseClient(BaseClientInterface):
    logger = logging.getLogger(__name__)

    async def _get_data_by_url(
        self,
        client: httpx.AsyncClient,
        url: str,
        headers: Mapping[str, str],
        path: str,
    ) -> httpx.Response:
        try:
            response = await client.get(
                url=url,
                headers=headers,
            )
            response.raise_for_status()
            return response
        except httpx.HTTPStatusError as error:
            detail = get_error_details(status_code=error.response.status_code)
            self.logger.exception(
                format_errors_message(
                    message=f"{detail['message']}- {path}",
                    name_function=self._get_data_by_url.__name__,
                )
            )
            raise AppException(
                status_code=error.response.status_code,
                code=detail["code"],
                message=detail["message"],
            )

    def _check_response(
        self,
        response: httpx.Response,
        path: str,
    ) -> Dict[str, Any]:
        try:
            result_json: Dict[str, Any] = response.json()
            return result_json
        except ValueError as err:
            self.logger.exception(
                msg=format_errors_message(
                    message=f"{err}- {path}",
                    name_function=self._get_data_by_url.__name__,
                )
            )
            raise ValidationAppError()

    def _validate_data(
        self,
        data: Dict[str, Any],
        model: Type[T],
        path: str,
    ) -> T:
        try:
            validate_data = model.model_validate(data)
            return validate_data
        except pydantic.ValidationError as err:
            self.logger.exception(
                msg=format_errors_message(
                    message=f"{err}- {path}",
                    name_function=self._get_data_by_url.__name__,
                )
            )
            raise ValidationAppError()
