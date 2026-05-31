from typing import Optional, List

from pydantic import BaseModel, field_validator, computed_field


class GenerateModelDTO(BaseModel):
    genre: str


# Модели для выдачи Top250 фильмов для кинописка
class KinopoiskModelTop250DTO(BaseModel):
    kinopoiskId: int
    nameRu: Optional[str] = None
    posterUrlPreview: str
    ratingKinopoisk: Optional[float] = None
    genres: List[GenerateModelDTO]

    @computed_field  # type: ignore[prop-decorator]
    @property
    def name(self) -> str:
        return self.nameRu or ""


class DataKinopoiskModelTop250DTO(BaseModel):
    total: int
    totalPages: int
    items: List[KinopoiskModelTop250DTO]


# Модели для поиска по названию для кинописка
class KinopoiskModelSearchByNameDTO(BaseModel):
    filmId: int
    posterUrlPreview: str
    genres: List[GenerateModelDTO]
    nameEn: Optional[str] = None
    nameRu: Optional[str] = None
    rating: Optional[float] = None

    @field_validator("rating", mode="before")
    @classmethod
    def validate_rating(cls, value: Optional[str]) -> Optional[str]:
        if value == "null":
            return None
        return value

    @computed_field  # type: ignore[prop-decorator]
    @property
    def name(self) -> str:
        return self.nameRu or self.nameEn or ""


class DataKinopoiskModelSearchByNameDTO(BaseModel):
    pagesCount: int
    films: List[KinopoiskModelSearchByNameDTO]


# модели для выдачи информации по фильму
class KinopoiskModelInfoMovieDTO(BaseModel):
    nameRu: Optional[str]
    nameOriginal: Optional[str]
    year: Optional[int]
    genres: List[GenerateModelDTO]
    webUrl: str
    posterUrlPreview: str
    description: Optional[str]
    filmLength: Optional[int]

    @computed_field  # type: ignore[prop-decorator]
    @property
    def name(self) -> str:
        return self.nameRu or self.nameOriginal or ""
