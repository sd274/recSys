from typing import Any
from app.embedder.base_embedder import BaseEmbedder

SentenceTransformersModel = Any

class ModelEmbedder(BaseEmbedder):
    model: SentenceTransformersModel

    def __init__(self, model: SentenceTransformersModel):
        self.model = model

    def embed_batch_strings(self, texts: list[str]) -> list[list[float]]:
        embeddings = self.model.encode(texts)
        return embeddings
