# routes/test_routes.py

from fastapi import APIRouter
from controllers.modules.test.test_controller import test

# Create an instance of APIRouter
router = APIRouter()

@router.get("/")
async def root():
    return {"message": "hello World"}

@router.get("/test")
async def test():
    return await test()
