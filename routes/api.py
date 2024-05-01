# api.py
from fastapi import APIRouter
from controllers.modules.test.test_controller import list_items, get_item

# Create an instance of APIRouter
router = APIRouter()

@router.get("/")
async def root():
    return {"message": "hello World"}



@router.get("/items")
async def list_items():
    return await list_items

@router.get("/items/{item_id}")
async def get_item(item_id: int):
    return await get_item(item_id)