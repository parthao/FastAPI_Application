from fastapi import APIRouter, UploadFile, File, HTTPException, Request
from pathlib import Path
from app.services.pdfreader_service import PDFService
import os
router = APIRouter(prefix="/pdfreader", tags=["items"])
service = PDFService()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        if not file.filename.endswith(".pdf"):
            raise HTTPException(status_code=400, detail="Only PDF files are allowed")

        result = await service.process_uploaded_pdf(file)
        file_path = Path(__file__).resolve().parents[2] / "chunks.pkl"
        file_path2 = Path(__file__).resolve().parents[2] / "embeds.pkl"
        if file_path.exists() or file_path2.exists():
            file_path.unlink()
            file_path2.unlink()
            print("Files deleted.")
        else:
            print("File does not exist.")
        return result
    except Exception as e:
        print(f"Error processing PDF: {e}")
        raise e
    


@router.post("/regenerator")
async def regen(request: Request):
    data = await request.json()
    fileName = data.get("fileName")
    print(f"Received fileName: {fileName}")
    if not fileName.endswith(".txt"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    result = await service.process_regen(fileName)
    return result