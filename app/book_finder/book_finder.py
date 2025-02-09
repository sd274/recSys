from app.book_info_dao.book_info_dao import BookInfoDAO
from app.book_info_dao.types import Book
from app.embedder.base_embedder import BaseEmbedder


def find_similar_books(
    book_info_dao: BookInfoDAO, embedder: BaseEmbedder, text: str, n: int = 2
) -> list[Book]:
    embedded_text = embedder.embed_single_string(text)
    similar_books = book_info_dao.similarity_search(embedded_text, n=n)
    return similar_books
