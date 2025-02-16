from pydantic import BaseModel

type ISBN = str


class Book(BaseModel):
    ISBN: ISBN
    title: str
    author: str
    published_year: int | None
    publisher: str


class User(BaseModel):
    user_id: str
    location: str
    age: int | None


class BookRating(BaseModel):
    user_id: str
    ISBN: ISBN
    rating: int | None
