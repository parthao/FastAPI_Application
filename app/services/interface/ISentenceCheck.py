from abc import ABC, abstractmethod

class ISentenceCheck(ABC):

    @abstractmethod
    def IsSentenceCorrect(self, sentence: str) -> bool:
        pass