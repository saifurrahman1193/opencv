# api.py
from fastapi import APIRouter

# Create an instance of APIRouter
router = APIRouter()

@router.get("/")
async def root():
    return {"message": "hello World"}

@router.post("/")
async def post():
    return {"message": "hello World"}

@router.put("/")
async def put():
    return {"message": "hello World"}

@router.get("/items")
async def list_items():
    return {"message": "hello World"}

@router.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}