from abc import ABC, abstractmethod
from app.models.AIParamModel import AIParam

class IQuestionGenerator(ABC):
    @abstractmethod
    def generate_questions_advance(self, text: str, aIParam:AIParam) -> list:
        """Generates questions from the given text."""
        pass
    
    @abstractmethod
    def generate_questions_simple(self, text: str,aIParam:AIParam) -> list:
        """Generates questions from the given text."""
        pass