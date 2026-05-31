from pydantic_settings import BaseSettings, SettingsConfigDict
from settings.paths import ROOT_DIR


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
    )
    APP: str
    PORT: int
    HOST: str
    RELOAD: bool = True


settings: AppSettings = AppSettings()  # type: ignore[call-arg]
