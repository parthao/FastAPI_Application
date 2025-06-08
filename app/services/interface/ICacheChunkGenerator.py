from abc import ABC, abstractmethod

class ICacheChunkGenerator(ABC):
    @abstractmethod
    def extract_text_from_pdf(self, pdf_path: str) -> str:
        pass

    @abstractmethod
    def chunk_text(self, text: str, max_len: int = 400) -> list[str]:
        pass