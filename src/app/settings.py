from pydantic_settings import BaseSettings, SettingsConfigDict
from settings.paths import ROOT_DIR


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
    )
    APP: str = "app.main:app"
    PORT: int = 5010
    HOST: str = "127.0.0.1"
    RELOAD: bool = True


settings: AppSettings = AppSettings()
