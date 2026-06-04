import pytest
from fastapi.testclient import TestClient

from app.kinopoisk.backend.core.startup import create_app


@pytest.mark.api
def test_search_movies_by_name():
    app = create_app()
    with TestClient(app) as client:
        response = client.get("/api/get/search-by-name?name=поиск&page=1")
    assert response.status_code == 200
