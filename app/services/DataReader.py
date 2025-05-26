from .IDataReader import IDataReader
from PyPDF2 import PdfReader
from docx import Document

class DataReader(IDataReader):
    def read_pdf(self, file_path: str) -> str:
        """
        Reads a PDF file and returns its text content.
        
        :param file_path: Path to the PDF file.
        :return: Text content of the PDF file.
        """
        try:
            text = ""
            with open(file_path, "rb") as f:
                reader = PdfReader(f)
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
            return text
        except Exception as e:
            print(f"Error reading PDF file: {e}")
            return ""
        
    def read_docx(self, file_path: str) -> str:
        """
        Reads a DOCX file and returns its text content.
        
        :param file_path: Path to the DOCX file.
        :return: Text content of the DOCX file.
        """
        try:
            doc = Document(file_path)
            text = "\n".join([para.text for para in doc.paragraphs])
            return text
        except Exception as e:
            print(f"Error reading DOCX file: {e}")
            return ""
        
    def read_txt(self, file_path: str) -> str:
        """
        Reads a TXT file and returns its text content.
        
        :param file_path: Path to the TXT file.
        :return: Text content of the TXT file.
        """
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
            return text
        except Exception as e:
            print(f"Error reading TXT file: {e}")
            return ""    
