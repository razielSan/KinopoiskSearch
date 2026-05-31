from fastapi.templating import Jinja2Templates

from app.kinopoisk.backend.settings.paths import TEMPLATES_DIR


templates = Jinja2Templates(directory=TEMPLATES_DIR)
