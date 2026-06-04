from typing import Any, Dict
from abc import ABC, abstractmethod


class BaseClientInterface(ABC):
    @abstractmethod
    async def _get_data_by_url(
        self,
        client: Any,
        url: str,
        headers: Any,
        path: str,
    ) -> Any:
        pass

    @abstractmethod
    def _check_response(
        self,
        response: Any,
        path: str,
    ) -> Any:
        pass

    @abstractmethod
    def _validate_data(
        self,
        data: Dict[str, Any],
        model: Any,
        path: str,
    ) -> Any:
        pass
