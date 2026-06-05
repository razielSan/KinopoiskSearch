from typing import Dict, TypedDict

from domain.exceptions import AppException


class ErrorsData(TypedDict):
    code: str
    message: str
    user_message: str


ERROR_HTTP_STATUS_CODES: Dict[int, ErrorsData] = {
    401: {
        "code": "INVALID_API_KEY",
        "message": "invalid api key",
        "user_message": "the service is temporarily unavailable",
    },
    500: {
        "code": "INTERNAL_SERVER_ERROR",
        "message": "an unexpected failure has occurred",
        "user_message": "an unexpected failure has occurred"
        ", try making the request again",
    },
    502: {
        "code": "BAD GATEWAY",
        "message": "invalid response",
        "user_message": "invalid response",
    },
}


def format_errors_message(
    message: str,
    name_function: str,
    quantity: int = 50,
    separator: str = "-",
    path: str = "Неизвестно",
) -> str:
    return (
        f"{message}\n"
        f"Api Path: {path}\n"
        f"Function: {name_function}\n{separator * quantity}"
    )


def get_error_details(status_code: int) -> ErrorsData:
    data = ERROR_HTTP_STATUS_CODES.get(status_code, None)
    if data is not None:
        return data
    return {
        "code": "UNKNOWN STATUS CODE",
        "message": "an unexpected error has occurred",
        "user_message": "an unexpected error has occurred, try making "
        "the request again",
    }


class ValidationAppError(AppException):
    def __init__(self) -> None:
        super().__init__(
            status_code=500,
            code="VALIDATION_ERROR",
            message="failed validate",
            user_message="error on the server, try making the request again",
        )
