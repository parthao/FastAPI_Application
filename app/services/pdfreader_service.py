import os
import uuid
from fastapi import UploadFile, HTTPException
from typing import Dict, Any
from app.services.PDFQuestionService import PDFQuestionService  # AI logic class
from app.models.AIResponseModel import AIResponseModel  # AI response model
class PDFService:
    def __init__(self):
        self.upload_dir = "uploaded_files"
        os.makedirs(self.upload_dir, exist_ok=True)
        self.question_service = PDFQuestionService()
        
    def list_items(self):
        # Your existing list logic
        return []

    async def process_uploaded_pdf(self, file: UploadFile) -> AIResponseModel:
        ext = os.path.splitext(file.filename)[1].lower()
        if ext not in [".pdf", ".txt", ".docx"]:
            raise HTTPException(status_code=400, detail="Unsupported file format")

        contents = await file.read()

        # Generate unique filename with original extension
        unique_filename = f"{uuid.uuid4()}{ext}"
        file_path = os.path.join(self.upload_dir, unique_filename)

        with open(file_path, "wb") as f:
            f.write(contents)

        # Call the AI processing logic
        try:
            result = self.question_service.react_generate_questions(file_path)
            responsemodel = AIResponseModel(
                OriginalFileName=file.filename,
                StoredFileName=unique_filename,
                ContentSize=len(contents),
                SavedTo=file_path,
                AIResult=result
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error during AI processing: {str(e)}")

        return responsemodel
