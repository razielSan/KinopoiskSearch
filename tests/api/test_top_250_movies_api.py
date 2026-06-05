import pytest
from fastapi.testclient import TestClient

from app.kinopoisk.backend.core.startup import create_app


@pytest.mark.api
def test_top_250_movies_api():
    app = create_app()
    with TestClient(app) as client:
        response = client.get("/api/get/top-250?page=1")
    assert response.status_code == 200
