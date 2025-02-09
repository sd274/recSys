from fastapi import Request, APIRouter
from pydantic import BaseModel

from app.book_finder.book_finder import find_similar_books

router = APIRouter()

class SimilarBookRequest(BaseModel):
    text: str
    n: int = 2

def find_similar(request: Request, request_body: SimilarBookRequest):
    similar_books = find_similar_books(
        book_info_dao=request.app.book_info_dao,
        embedder=request.app.embedder,
        text=request_body.text,
        n=request_body.n
    )
    return [
        {
            "title": book.title,
            "description": book.description
        }
        for book in similar_books
    ]

router.add_api_route(
    path="/find-similar",
    endpoint=find_similar,
    methods=["POST"],
    tags=["book"],
)
