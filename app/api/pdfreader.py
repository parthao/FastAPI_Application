from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.pdfreader_service import PDFService

router = APIRouter(prefix="/pdfreader", tags=["items"])
service = PDFService()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    result = await service.process_uploaded_pdf(file)
    return result
