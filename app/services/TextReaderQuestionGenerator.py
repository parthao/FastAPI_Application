from app.services.DataReader import DataReader
from app.services.ChunkGenerator import ChunkGenerator
from app.services.QuestionGenerator import QuestionGenerator
from app.models.AIParamModel import AIParam
from app.models.AIResponseModel import AIResult


class TextReaderQuestionGenerator:
    def __init__(self):
        self.reader = DataReader()
        self.chunker = ChunkGenerator()
        self.qgen = QuestionGenerator()
        
        
    async def textreader_question_generator(self, text: str) -> dict:
        ai_param = AIParam()
        if len(text) <= 100:
            print("Text length is less than 100 characters.")
            all_questions = []
            questions = self.qgen.generate_questions_advance(text, ai_param)
            all_questions.append({
                "questions": questions
            })
                
            return  all_questions
        else:
            print("Text length is less than 100 characters.")
            all_questions = []
            questions = self.qgen.generate_questions_advance(text, ai_param)
            all_questions.append({
                "questions": questions
            })
                
            return  all_questions