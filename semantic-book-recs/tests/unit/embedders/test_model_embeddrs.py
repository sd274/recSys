from rich import print
from sentence_transformers import SentenceTransformer

from app.embedder.model_embedder import ModelEmbedder


def test_model_embedder():
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    embedder = ModelEmbedder(model)
    texts = ["hello, there stu day", "good, does this work"]
    vectors = embedder.embed_batch_strings(texts)
    print(vectors)
