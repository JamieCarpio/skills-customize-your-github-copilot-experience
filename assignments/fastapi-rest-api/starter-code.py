from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict

app = FastAPI()


class Item(BaseModel):
    title: str
    description: Optional[str] = None


# In-memory "database"
items: Dict[int, Item] = {}
next_id = 1


@app.get("/items")
def list_items():
    return [{"id": i, **items[i].dict()} for i in items]


@app.post("/items", status_code=201)
def create_item(item: Item):
    global next_id
    items[next_id] = item
    created = {"id": next_id, **item.dict()}
    next_id += 1
    return created


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, **items[item_id].dict()}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return {"id": item_id, **item.dict()}


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return None
