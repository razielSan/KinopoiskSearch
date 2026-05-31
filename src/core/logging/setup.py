import logging

from settings.paths import LOG_DIR

LOG_DIR.mkdir(exist_ok=True)


def setup_logging(fmt: str, date_fmt: str) -> None:    
    formatter = logging.Formatter(
        fmt=fmt,
        datefmt=date_fmt,
    )
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(
        filename=LOG_DIR / "app.log",
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    root_logging = logging.getLogger()
    root_logging.setLevel(logging.INFO)
    
    if root_logging.handlers: # во избежания повторного создания handlers
        root_logging.handlers.clear()
        
    root_logging.addHandler(console_handler)
    root_logging.addHandler(file_handler)
