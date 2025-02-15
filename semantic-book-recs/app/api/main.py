from sentence_transformers import SentenceTransformer
from app.api.book_app import BookApp
from app.api.utils.logging import configure_logger
from app.book_info_dao.book_info_dao import BookInfoDAO
from app.embedder.model_embedder import ModelEmbedder

configure_logger()


embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
embedder = ModelEmbedder(embedding_model)

book_info_dao = BookInfoDAO.load_from_file(embedder)

app = BookApp(embedder=embedder, book_info_dao=book_info_dao)
