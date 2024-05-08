# routes/test_routes.py

from fastapi import APIRouter, FastAPI, Request
from controllers.modules.test.test_controller import test_f

# Create an instance of APIRouter
router = APIRouter()

@router.get("/test")
async def test(request: Request):
    return await test_f(request)
