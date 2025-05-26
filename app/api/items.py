from fastapi import APIRouter, HTTPException
from typing import List
from app.models.item import Item
from app.services.item_service import ItemService

router = APIRouter(prefix="/items", tags=["items"])
service = ItemService()

@router.get("/", response_model=List[Item])
def get_items():
    return service.list_items()

@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = service.get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item