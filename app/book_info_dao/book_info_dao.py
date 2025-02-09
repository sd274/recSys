from pathlib import Path
from jaxtyping import Array, Float
import jax.numpy as jnp
import csv

from app.book_info_dao.types import Book
from app.embedder.base_embedder import BaseEmbedder
from app.api.utils.logging import get_logger

logger = get_logger()

EmbeddingArray = Float[Array, "items embedding-dimension"]


class BookInfoDAO:
    """
    Using an in memory vector db for now
    """

    embeddings: EmbeddingArray
    items: list[Book]

    def __init__(self, embeddings: list[list[float]], items: list[Book]):
        embeddings_jnp = jnp.array(embeddings, dtype=jnp.float32)
        self.embeddings = embeddings_jnp
        self.items = items

    def similarity_search(self, vector: list[float], n: int = 5) -> list[Book]:
        vector_jnp = jnp.array(vector)
        similarity_scores = self._compute_similarity(vector_jnp, self.embeddings)
        top_idx = jnp.argsort(similarity_scores, descending=True)
        return [self.items[idx] for idx in top_idx[:n]]

    @classmethod
    def _compute_similarity(
        cls,
        vector: Float[Array, "embedding-dimension"],
        embeddings: Float[Array, "items embedding-dimension"],
    ) -> Float[Array, "items"]:
        embedding_norms = jnp.linalg.norm(embeddings, axis=1)
        vector_norm = jnp.linalg.norm(vector)
        dot_prods = jnp.dot(embeddings, vector)
        return dot_prods / (embedding_norms.squeeze() * vector_norm)

    @classmethod
    def load_from_file(cls, embedder: BaseEmbedder) -> "BookInfoDAO":
        raw_data = cls._load_raw_data()
        to_embedd = [book.description for book in raw_data]
        embedded = embedder.embed_batch_strings(to_embedd)
        return BookInfoDAO(embedded, raw_data)

    @classmethod
    def _load_raw_data(cls) -> list[Book]:
        filepath = Path(__file__).parent.joinpath("data").joinpath("data.csv").resolve()
        logger.info(f"Loading data from {filepath}")
        with open(filepath, "r") as file:
            raw_data = csv.reader(file, delimiter=",")
            raw_data_as_list = list(raw_data)
            headers = raw_data_as_list[0]
            parsed_data = [
                {key: value for key, value in zip(headers, row)}
                for row in raw_data_as_list
            ]
        return [
            Book(
                title=row.get("title", ""),
                description=row.get("description", ""),
                # categories=row.get("categories", ""),
                # authors=row.get("authors", ""),
                # published_year=row.get("published_year", ""),
            )
            for row in parsed_data
        ]
