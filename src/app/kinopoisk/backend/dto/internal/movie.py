from typing import Optional, List, Union

from pydantic import BaseModel, model_validator, Field, field_validator, ConfigDict

from app.kinopoisk.backend.dto.external.kinopoisk import GenerateModelDTO


# модели для возврата на фронтенд данных по поиск по имени, top 250 фильмов
class ResponseModelDTO(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    kinopoisk_id: int = Field(serialization_alias="kinopoiskId")
    name: str
    url_poster: str = Field(serialization_alias="urlPoster")
    rating: Optional[float]
    rating_color: Optional[str] = Field(default=None, serialization_alias="ratingColor")
    genres: Union[str, List[GenerateModelDTO]]

    @field_validator("genres", mode="before")
    @classmethod
    def validate_genres(cls, value: List[GenerateModelDTO]) -> str:
        return ", ".join([data.genre for data in value])

    @model_validator(mode="after")
    def chek_rating_color(self) -> "ResponseModelDTO":  # для mypy
        # валидация rating_coloer
        if self.rating is None:
            self.rating_color = None
        elif self.rating >= 8:
            self.rating_color = "green"
        elif self.rating >= 5:
            self.rating_color = "orange"
        else:
            self.rating_color = "red"

        return self


class DataResponseModelDTO(BaseModel):
    total: int
    movies: List[ResponseModelDTO]


#  модели для возврата на фронтенд данных для выдачи информации для фильма по id
class ResponseModelInfoMovieDTO(BaseModel):
    name: str
    year: Union[str, int, None]
    genres: Union[str, List[GenerateModelDTO]]
    site: str
    url_poster: str = Field(serialization_alias="urlPoster")
    description: Optional[str]
    film_length: Union[str, int, None] = Field(serialization_alias="filmLength")

    model_config = ConfigDict(populate_by_name=True)

    @field_validator("genres", mode="before")
    @classmethod
    def validate_genres(cls, value: List[GenerateModelDTO]) -> str:
        return ", ".join([data.genre for data in value])

    @field_validator("description", mode="before")
    @classmethod
    def validate_description(cls, value: Optional[str]) -> str:
        if value is None:
            return "Нет описания"
        return f"{value[0:250]}..."

    @field_validator("year", mode="before")
    @classmethod
    def validate_year(cls, value: Optional[str]) -> str:
        if value is None:
            return "Неизвестно"
        return str(value)

    @field_validator("film_length", mode="before")
    @classmethod
    def validate_filmLength(cls, value: Optional[str]) -> str:
        if value is None:
            return "Неизвестно"
        return str(value)
