# routes/ocr_routes.py

from fastapi import APIRouter, FastAPI, Request
from controllers.modules.ocr.ocr_controller import ocr_f

# Create an instance of APIRouter
router = APIRouter()


@router.get("/ocr")
async def ocr(request: Request):
    return await ocr_f(request)
