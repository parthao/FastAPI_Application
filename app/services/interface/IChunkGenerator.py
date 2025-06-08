from abc import ABC, abstractmethod

class IChunkGenerator(ABC):
    @abstractmethod
    def chunk_text(self, text: str,words: int=100) -> list:
        """Splits the text into smaller chunks."""
        pass