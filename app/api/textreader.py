from fastapi import APIRouter, HTTPException
from app.services.TextReaderQuestionGenerator import TextReaderQuestionGenerator
from pydantic import BaseModel

router = APIRouter(prefix="/txt", tags=["items"])
service = TextReaderQuestionGenerator()

# Define the request model
class TextRequest(BaseModel):
    txt: str

@router.post("/read_text")
async def read_text(request: TextRequest):
    if not request.txt:
        raise HTTPException(status_code=400, detail="No text provided")
    result = await service.textreader_question_generator(request.txt)
    return result
