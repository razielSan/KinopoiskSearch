from pathlib import Path

from settings.paths import BASE_DIR

KINOPOISK_DIR: Path = BASE_DIR / "app" / "kinopoisk"
FRONTEND_DIR: Path = KINOPOISK_DIR / "frontend"
BACKEND_DIR: Path = KINOPOISK_DIR / "backend"
STATIC_DIR: Path = FRONTEND_DIR / "static"
TEMPLATES_DIR: Path = FRONTEND_DIR / "templates"
