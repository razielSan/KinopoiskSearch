from typing import Mapping

from pydantic_settings import BaseSettings, SettingsConfigDict

from app.kinopoisk.backend.settings.paths import BACKEND_DIR


class KinopoiskSettings(BaseSettings):
    API_KEY: str
    API_URL_TOP_250_MOVIES: str = (
        "https://kinopoiskapiunofficial.tech"
        "/api/v2.2/films/collections?type=TOP_250_MOVIES&page={page}"
    )
    API_URL_SEARCH_MOVIE_BY_NAME: str = (
        "https://kinopoiskapiunofficial.tech"
        "/api/v2.1/films/search-by-keyword?keyword={name}&page={page}"
    )
    API_URL_MOVIE_KINIOPOISK_ID: str = (
        "https://kinopoiskapiunofficial.tech/api/v2.2/films/{id}"
    )

    @property
    def headers(self) -> Mapping[str, str]:
        return {
            "Content-Type": "application/json",
            "X-API-KEY": self.API_KEY,
        }

    model_config = SettingsConfigDict(env_file=BACKEND_DIR / ".env")


settings: KinopoiskSettings = KinopoiskSettings()  # type: ignore[call-arg]
