from pydantic import BaseModel, \
    ValidationError, validator, root_validator
from datetime import date


class Genre(BaseModel):
    name: str

    @validator('name')
    def name_not_empty(cls, v: str) -> str:
        if v == '':
            raise ValueError("Empty Genre was got")
        return v

    @validator('name')
    def name_length_limit(cls, v: str) -> str:
        if len(v) > 50:
            raise ValueError("Length of Genre.name is too big")
        return v


class Book(BaseModel):
    title: str
    writer: str
    date: date
    genres: list[Genre]
    pages: int

    @root_validator
    def check_len_limits(cls, values):
        title, writer = values.get('title'), values.get('writer')
        pages, genres = values.get('pages'), values.get('genres')
        if not 1 < len(title) < 50 \
                or not 1 < len(writer) < 50 \
                or not 5 < pages < 5000 \
                or not 0 < len(genres) < 10:
            raise ValueError("Length is not correct")

        return values
