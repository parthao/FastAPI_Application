from fastapi import APIRouter, HTTPException
from app.services.AnswerGenerator import AnswerGenerator
from pydantic import BaseModel

router = APIRouter(prefix="/get", tags=["answer"])
service = AnswerGenerator()

# Define the request model
class TextRequest(BaseModel):
    FilePath: str
    Question: str

@router.post("/answer_text")
async def read_text(request: TextRequest):
    if not request.FilePath or not request.Question:
        raise HTTPException(status_code=400, detail="No text provided")
    result = await service.answer_question("uploaded_files/"+request.FilePath, request.Question)
    return result
