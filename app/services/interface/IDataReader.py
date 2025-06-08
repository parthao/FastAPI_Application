from abc import ABC, abstractmethod

class IDataReader(ABC):
    @abstractmethod
    def read_pdf(self, file_path: str) -> str:
        pass
    @abstractmethod
    def read_docx(self, file_path: str) -> str:
        pass
    @abstractmethod
    def read_txt(self, file_path: str) -> str:
        pass