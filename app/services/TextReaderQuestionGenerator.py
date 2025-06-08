from app.services.DataReader import DataReader
from app.services.ChunkGenerator import ChunkGenerator
from app.services.QuestionGenerator import QuestionGenerator
from app.models.AIParamModel import AIParam
from app.models.AIResponseModel import AIResponseModel, AIResult
import os
import uuid
from typing import Dict, Any


class TextReaderQuestionGenerator:
    def __init__(self):
        self.upload_dir = "uploaded_files"
        self.reader = DataReader()
        self.chunker = ChunkGenerator()
        self.qgen = QuestionGenerator()
        
        
    async def textreader_question_generator(self, text: str) -> AIResponseModel:
        ai_param = AIParam()
        unique_filename = f"{uuid.uuid4()}.txt"
        file_path = os.path.join(self.upload_dir, unique_filename)
        with open(file_path, "w", encoding="utf-8") as f:
                f.write(text)
        if len(text) <= 100:
            print("Text length is less than 100 characters.")
            all_questions = []
            questions = self.qgen.generate_questions_advance(text, ai_param)
            all_questions.append({
                "questions": questions
            })
            responsemodel = AIResponseModel(
                OriginalFileName="",
                StoredFileName=unique_filename,
                ContentSize=0,
                SavedTo=file_path,
                AIResult=all_questions
            )
            return responsemodel
        else:
            print("Text is greater than 100 characters.")
            all_questions = []
            chunks = self.chunker.chunk_text(text, 100)
            for idx, chunk in enumerate(chunks):
                questions = self.qgen.generate_questions_advance(chunk, ai_param)
                if (questions !=[]):
                    all_questions.append({
                        "questions": questions
                        })
            all_questions.append({
                "questions": questions
            })
                
            responsemodel = AIResponseModel(
                OriginalFileName="",
                StoredFileName=unique_filename,
                ContentSize=0,
                SavedTo=file_path,
                AIResult=all_questions
            )
            return responsemodel