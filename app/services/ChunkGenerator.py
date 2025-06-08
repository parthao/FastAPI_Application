from .interface.IChunkGenerator import IChunkGenerator
import nltk
from nltk.tokenize import sent_tokenize
class ChunkGenerator(IChunkGenerator):
        def chunk_text(self, text: str,max_words: int=100) -> list:
            sentences = sent_tokenize(text)
            chunks, chunk = [], []
            word_count = 0

            for sentence in sentences:
                word_count += len(sentence.split())
                chunk.append(sentence)
                if word_count >= max_words:
                    chunks.append(" ".join(chunk))
                    chunk = []
                    word_count = 0

            if chunk:
                chunks.append(" ".join(chunk))

            return chunks