from transformers import pipeline
from .IQuestionGenerator import IQuestionGenerator
from app.services.SentenceCheck import SentenceCheck
from app.models.AIParamModel import AIParam
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"[QuestionGenerator] Using device: {device}")

qg_simple = pipeline("text2text-generation", model="valhalla/t5-small-qg-hl", device=0 if torch.cuda.is_available() else -1)
qg_advanced = pipeline("text2text-generation", model="iarfmoose/t5-base-question-generator", device=0 if torch.cuda.is_available() else -1)

sentenceCheck = SentenceCheck()

class QuestionGenerator(IQuestionGenerator):    
    def generate_questions_advance(self, text: str, aIParam: AIParam) -> list:
        input_text = f"generate questions: {text}"
        outputs = qg_advanced(
            input_text,
            max_length=aIParam.max_length,
            num_return_sequences=aIParam.num_return_sequences,
            do_sample=aIParam.do_sample,
            top_k=aIParam.top_k,
            top_p=aIParam.top_p,
            temperature=aIParam.temperature
        )
        raw_sentences = [o["generated_text"] for o in outputs]
        filtered = [s for s in raw_sentences if sentenceCheck.IsSentenceCorrect(s)]
        return filtered

    def generate_questions_simple(self, text: str, aIParam: AIParam) -> list:
        input_text = f"generate questions: {text}"
        outputs = qg_simple(
            input_text,
            max_length=aIParam.max_length,
            num_return_sequences=aIParam.num_return_sequences,
            do_sample=aIParam.do_sample,
            top_k=aIParam.top_k,
            top_p=aIParam.top_p,
            temperature=aIParam.temperature
        )
        return [o["generated_text"] for o in outputs]
