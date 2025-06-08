from abc import ABC, abstractmethod
#pdf_path, question, top_k=5
class IAnswerGenerator(ABC):
    @abstractmethod
    def answer_question(self, pdf_path: any,question:str, top_k: int = 5) -> list:
        """Splits the text into smaller chunks."""
        pass
