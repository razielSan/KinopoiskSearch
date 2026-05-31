class AppException(Exception):
    def __init__(
        self,
        status_code: int = 500,
        code: str = "APP_ERROR",
        message: str = "application error",
    ) -> None:
        self.status_code: int = status_code
        self.code: str = code
        self.message: str = message
