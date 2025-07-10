from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from typing import List


from modules.load_vectorstore import load_vectorstore
from logger import logger

router = APIRouter()


@router.post("/upload-pdfs")
async def upload_pdfs(files: List[UploadFile] = File(...)):
    try:
        logger.info("Uploading PDFs...")
        load_vectorstore(files)
        logger.info("PDFs uploaded successfully!")
        return {"message": "Files processed and vectorstore updated!"}
    except Exception as e:
        logger.exception(f"Error on upload_pdfs: {e}")
        return JSONResponse(
            status_code=500,
            content={"error": str(e)},
        )
