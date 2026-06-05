class LogFormat:
    QUANTITY: int = 50
    SEPARATOR: str = "-"
    FMT: str = (
        f"{QUANTITY * SEPARATOR}\n[%(asctime)s] - %(name)s"
        " - [%(levelname)s - %(message)s]"
    )
    DATE_FMT: str = "%Y-%m-%d %H:%M:%S"
