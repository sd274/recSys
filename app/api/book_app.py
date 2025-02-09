from fastapi import FastAPI

from app.api.routes.health.endpoint import router as health_router
from app.api.routes.find_books.endpoints import router as book_router
from app.book_info_dao.book_info_dao import BookInfoDAO
from app.embedder.base_embedder import BaseEmbedder


class BookApp(FastAPI):
    embedder: BaseEmbedder
    book_info_dao: BookInfoDAO

    def __init__(self, embedder: BaseEmbedder, book_info_dao: BookInfoDAO):
        self.embedder = embedder
        self.book_info_dao = book_info_dao
        super().__init__(title="What ya wanna read?")
        self.include_router(health_router)
        self.include_router(book_router)
