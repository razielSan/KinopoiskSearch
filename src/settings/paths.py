from pathlib import Path


BASE_DIR: Path = Path(__file__).resolve().parents[1]
ROOT_DIR: Path = BASE_DIR.parent
LOG_DIR:  Path = ROOT_DIR / "logs"
