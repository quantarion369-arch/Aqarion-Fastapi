from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class Item(BaseModel):
    id: int
    name: str


_DB: dict[int, Item] = {}


@router.get("/", response_model=list[Item])
async def list_items() -> list[Item]:
    return list(_DB.values())


@router.post("/", response_model=Item, status_code=201)
async def create_item(item: Item) -> Item:
    if item.id in _DB:
        raise HTTPException(status_code=409, detail="Item already exists")
    _DB[item.id] = item
    return item


@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int) -> Item:
    if item_id not in _DB:
        raise HTTPException(status_code=404, detail="Not found")
    return _DB[item_id]
