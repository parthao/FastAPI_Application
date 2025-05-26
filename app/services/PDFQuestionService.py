from app.services.DataReader import DataReader
from app.services.ChunkGenerator import ChunkGenerator
from app.services.QuestionGenerator import QuestionGenerator
from app.models.AIParamModel import AIParam
from app.models.AIResponseModel import AIResult
from pathlib import Path
import time

class PDFQuestionService:
    def __init__(self):
        self.reader = DataReader()
        self.chunker = ChunkGenerator()
        self.qgen = QuestionGenerator()

    def read_file(self, filename: str) -> str:
        ext = Path(filename).suffix.lower()
        if ext == ".txt":
            return self.reader.read_txt(filename)
        elif ext == ".pdf":
            return self.reader.read_pdf(filename)
        elif ext == ".docx":
            return self.reader.read_docx(filename)
        else:
            raise ValueError("Unsupported file format")

    def generate_questions(self, filepath: str) -> dict:
        ai_param = AIParam()
        text = self.read_file(filepath)

        if len(text) <= 100:
            
            total_chunks = len(text)

            sample_size = min(2, total_chunks)
            sample_chunks = chunks[:sample_size]

            start_time = time.time()
            for chunk in sample_chunks:
                self.qgen.generate_questions_advance(text, ai_param)
            elapsed = time.time() - start_time
            avg_time = elapsed / sample_size
            est_total_time = avg_time * total_chunks

            all_questions = []
            for idx, chunk in enumerate(chunks):
                questions = self.qgen.generate_questions_advance(chunk, ai_param)
                all_questions.append({
                    "chunk": idx + 1,
                    "questions": questions
                })

            return {
                "estimated_total_time_seconds": round(est_total_time, 2),
                "estimated_minutes": round(est_total_time / 60, 2),
                "total_chunks": total_chunks,
                "chunks": all_questions
            }

        chunks = self.chunker.chunk_text(text, 100)
        total_chunks = len(chunks)

        sample_size = min(2, total_chunks)
        sample_chunks = chunks[:sample_size]

        start_time = time.time()
        for chunk in sample_chunks:
            self.qgen.generate_questions_advance(chunk, ai_param)
        elapsed = time.time() - start_time
        avg_time = elapsed / sample_size
        est_total_time = avg_time * total_chunks

        all_questions = []
        for idx, chunk in enumerate(chunks):
            questions = self.qgen.generate_questions_advance(chunk, ai_param)
            all_questions.append({
                "chunk": idx + 1,
                "questions": questions
            })

        return {
            "estimated_total_time_seconds": round(est_total_time, 2),
            "estimated_minutes": round(est_total_time / 60, 2),
            "total_chunks": total_chunks,
            "chunks": all_questions
        }

    def react_generate_questions(self, filepath: str) -> AIResult:
        ai_param = AIParam()
        text = self.read_file(filepath)

        if len(text) <= 100:
            
            total_chunks = len(text)

            sample_size = min(2, total_chunks)
            sample_chunks = chunks[:sample_size]

            start_time = time.time()
            for chunk in sample_chunks:
                self.qgen.generate_questions_advance(text, ai_param)
            elapsed = time.time() - start_time
            avg_time = elapsed / sample_size
            est_total_time = avg_time * total_chunks

            all_questions = []
            for idx, chunk in enumerate(chunks):
                questions = self.qgen.generate_questions_advance(chunk, ai_param)
                all_questions.append({
                    "questions": questions
                })

            return  AIResult(
                    EstimatedTotalTimeSeconds=round(est_total_time, 2),
                    EstimatedMinutes=round(est_total_time / 60, 2),
                    TotalChunks=total_chunks,
                    Chunks=all_questions
                )

        chunks = self.chunker.chunk_text(text, 100)
        total_chunks = len(chunks)

        sample_size = min(2, total_chunks)
        sample_chunks = chunks[:sample_size]

        start_time = time.time()
        for chunk in sample_chunks:
            self.qgen.generate_questions_advance(chunk, ai_param)
        elapsed = time.time() - start_time
        avg_time = elapsed / sample_size
        est_total_time = avg_time * total_chunks

        all_questions = []
        for idx, chunk in enumerate(chunks):
            questions = self.qgen.generate_questions_advance(chunk, ai_param)
            if (questions !=[]):
                all_questions.append({
                    "questions": questions
                    })

        return AIResult(
                    EstimatedTotalTimeSeconds=round(est_total_time, 2),
                    EstimatedMinutes=round(est_total_time / 60, 2),
                    TotalChunks=total_chunks,
                    Chunks=all_questions
                )
            
