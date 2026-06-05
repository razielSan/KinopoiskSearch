class AppException(Exception):
    def __init__(
        self,
        status_code: int = 500,
        code: str = "APP_ERROR",
        message: str = "application error",
        user_message: str = "error on the server, try making the request again",
    ) -> None:
        self.status_code: int = status_code
        self.code: str = code
        self.message: str = message
        self.user_message: str = user_message
