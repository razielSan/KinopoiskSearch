import pytest
from fastapi.testclient import TestClient

from app.kinopoisk.backend.core.startup import create_app


@pytest.mark.api
def test_info_movie():
    id_movie = 301
    app = create_app()
    with TestClient(app) as client:
        response = client.get(f"/api/get/movie?film_id={id_movie}")
    assert response.status_code == 200
