import os
import uuid
from fastapi import UploadFile, HTTPException
from typing import Dict, Any
from app.services.PDFQuestionService import PDFQuestionService
from app.models.AIResponseModel import AIResponseModel

# Add the necessary imports
from PyPDF2 import PdfReader
from docx import Document

class PDFService:
    def __init__(self):
        self.upload_dir = "uploaded_files"
        os.makedirs(self.upload_dir, exist_ok=True)
        self.question_service = PDFQuestionService()

    def list_items(self):
        return []

    async def process_uploaded_pdf(self, file: UploadFile) -> AIResponseModel:
        ext = os.path.splitext(file.filename)[1].lower()
        if ext not in [".pdf", ".txt", ".docx"]:
            raise HTTPException(status_code=400, detail="Unsupported file format")

        contents = await file.read()
        saved_ext = ".txt"
        unique_filename = f"{uuid.uuid4()}{saved_ext}"
        file_path = os.path.join(self.upload_dir, unique_filename)

        # Extract text based on file type
        try:
            if ext == ".pdf":
                # Save temporarily to extract content
                print(f"inside pdf1")
                temp_path = os.path.join(self.upload_dir, f"{uuid.uuid4()}.pdf")
                print(f"inside pdf2")
                with open(temp_path, "wb") as f:
                    print(f"inside pdf3")
                    f.write(contents)
                    print(f"inside pdf4")
                    
                print(f"inside pdf5")
                reader = PdfReader(temp_path)
                print(reader)
                print(f"inside pdf6")
                extracted_text = "\n".join(page.extract_text() or "" for page in reader.pages)
                print(extracted_text)
                os.remove(temp_path)  # clean up
            elif ext == ".docx":
                temp_path = os.path.join(self.upload_dir, f"{uuid.uuid4()}.docx")
                with open(temp_path, "wb") as f:
                    f.write(contents)
                doc = Document(temp_path)
                extracted_text = "\n".join([p.text for p in doc.paragraphs])
                os.remove(temp_path)
            else:  # .txt
                extracted_text = contents.decode("utf-8", errors="ignore")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error reading uploaded file: {str(e)}")

        # Save extracted text to .txt file
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(extracted_text)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error saving file: {str(e)}")

        # Call the AI logic
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
    
    async def process_regen(self, fileName: str) -> AIResponseModel:
            # Call the AI logic
            file_path = os.path.join(self.upload_dir, fileName)
            try:
                result = self.question_service.react_generate_questions(file_path)
                responsemodel = AIResponseModel(
                    OriginalFileName=fileName,
                    StoredFileName=fileName,
                    ContentSize=0,
                    SavedTo=file_path,
                    AIResult=result
                )
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error during AI processing: {str(e)}")

            return responsemodel
