# api.py
from fastapi import APIRouter
from controllers.modules.test.testcontroller import test as test_tc


# Create an instance of APIRouter
router = APIRouter()

@router.get("/")
async def root():
    return {"message": "hello World"}



@router.get("/test")
async def list_items():
    return await test_tc()
