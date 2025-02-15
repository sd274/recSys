from abc import ABC, abstractmethod


class BaseEmbedder(ABC):

    @abstractmethod
    def embed_batch_strings(self, texts: list[str]) -> list[list[float]]:
        """Override this with emebdding logic"""

    def embed_single_string(self, text: str) -> list[float]:
        embedded = self.embed_batch_strings([text])
        assert len(embedded) > 0, "Something went wrong when embedded the string"
        return embedded[0]
