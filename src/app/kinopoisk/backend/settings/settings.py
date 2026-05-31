from typing import Mapping, Dict

from pydantic_settings import BaseSettings, SettingsConfigDict

from app.kinopoisk.backend.settings.paths import BACKEND_DIR


class KinopoiskSettings(BaseSettings):
    API_KEY: str
    API_URL_TOP_250_MOVIES: str
    API_URL_SEARCH_MOVIE_BY_NAME: str
    API_URL_MOVIE_KINIOPOISK_ID: str

    @property
    def headers(self) -> Mapping[str, str]:
        return {
            "Content-Type": "application/json",
            "X-API-KEY": self.API_KEY,
        }

    model_config = SettingsConfigDict(env_file=BACKEND_DIR / ".env")


settings: KinopoiskSettings = KinopoiskSettings()  # type: ignore[call-arg]
