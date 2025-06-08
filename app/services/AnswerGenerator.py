from .interface.IAnswerGenerator import IAnswerGenerator
from .CacheChunkGenerator import CacheChunkGenerator
from sentence_transformers import SentenceTransformer, util
from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
embedder = SentenceTransformer("all-MiniLM-L6-v2")  # Fast and small
CacheChunkGenerator = CacheChunkGenerator()
class AnswerGenerator(IAnswerGenerator):

    async def answer_question(self, pdf_path: any, question: str, top_k: int = 5) -> list:
            chunks, chunk_embeddings = CacheChunkGenerator.load_or_create_chunks(pdf_path)
            question_embedding = embedder.encode(question, convert_to_tensor=True)
            
            # Find top-k relevant chunks
            hits = util.semantic_search(question_embedding, chunk_embeddings, top_k=top_k)[0]
            
            best_answer = {"score": 0, "answer": "Not found"}
            for hit in hits:
                chunk = chunks[hit["corpus_id"]]
                try:
                    result = qa_pipeline(question=question, context=chunk)
                    if result["score"] > best_answer["score"]:
                        best_answer = result
                except:
                    continue
            return best_answer["answer"]