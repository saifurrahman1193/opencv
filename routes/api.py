# routes/api.py

from fastapi import APIRouter
from routes.api_routes import test_routes, ocr_routes


# Create an instance of APIRouter
router = APIRouter()

# Include routes from other files
router.include_router(test_routes.router, prefix="/test", tags=["test"])
router.include_router(ocr_routes.router, prefix="/ocr", tags=["ocr"])
