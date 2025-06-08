from fastapi import APIRouter, HTTPException
from app.services.TextReaderQuestionGenerator import TextReaderQuestionGenerator
from pydantic import BaseModel
from pathlib import Path
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
    file_path = Path(__file__).resolve().parents[2] / "chunks.pkl"
    file_path2 = Path(__file__).resolve().parents[2] / "embeds.pkl"
    if file_path.exists() or file_path2.exists():
        file_path.unlink()
        file_path2.unlink()
        print("Files deleted.")
    else:
        print("File does not exist.")
    return result
