# service/ChunkGeneratorService.py
import os
import pickle
import textwrap
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
from .interface.ICacheChunkGenerator import ICacheChunkGenerator
from .PDFQuestionService import PDFQuestionService
PDFQuestionService = PDFQuestionService()
class CacheChunkGenerator(ICacheChunkGenerator):
    def __init__(self):
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")

    def extract_text_from_pdf(self, pdf_path: str) -> str:
        text = ""
        with open(pdf_path, "rb") as f:
            reader = PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text

    def chunk_text(self, text: str, max_len: int = 400):
        return textwrap.wrap(text, max_len, break_long_words=False)

    def load_or_create_chunks(self, pdf_path, chunk_cache="chunks.pkl", embed_cache="embeds.pkl"):
        if os.path.exists(chunk_cache) and os.path.exists(embed_cache):
            with open(chunk_cache, "rb") as f1, open(embed_cache, "rb") as f2:
                return pickle.load(f1), pickle.load(f2)

        #text = self.extract_text_from_pdf(pdf_path)
        text = PDFQuestionService.read_file(pdf_path)
        chunks = self.chunk_text(text)
        embeddings = self.embedder.encode(chunks, convert_to_tensor=True)

        with open(chunk_cache, "wb") as f1, open(embed_cache, "wb") as f2:
            pickle.dump(chunks, f1)
            pickle.dump(embeddings, f2)

        return chunks, embeddings
