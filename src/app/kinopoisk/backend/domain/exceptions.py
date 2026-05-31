from typing import Dict, TypedDict

from domain.exceptions import AppException


class ErrorsData(TypedDict):
    code: str
    message: str


ERROR_HTTP_STATUS_CODES: Dict[int, ErrorsData] = {
    500: {
        "code": "INTERNAL_SERVER_ERROR",
        "message": "an unexpected failure has occurred",
    },
    502: {
        "code": "BAD GATEWAY",
        "message": "invalid response",
    },
    503: {
        "code": "SERVICE UNAVAILABLE",
        "message": "the service is temporarily unavailable",
    },
}


def format_errors_message(
    message: str, name_function: str, quantity: int = 50, separator: str = "-"
) -> str:
    return f"{message}\nFunction: {name_function}\n{separator * quantity}"


def get_error_details(status_code: int) -> ErrorsData:
    data = ERROR_HTTP_STATUS_CODES.get(status_code, None)
    if data is not None:
        return data
    return {
        "code": "UNKNOWN STATUS CODE",
        "message": "an unexpected error has occurred",
    }


class ValidationAppError(AppException):
    def __init__(self) -> None:
        super().__init__(
            status_code=500,
            code="VALIDATION_ERROR",
            message="failed_validate",
        )
