from __future__ import annotations

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

from .core import add, clamp_price, calc_tax

app = FastAPI(title="Portfolio Test API", version="1.0.0")

class ItemIn(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: float

class ItemOut(BaseModel):
    id: int
    name: str
    price: float
    tax: float

_DB: list[ItemOut] = []

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/calc/add")
def calc_add(a: int = Query(...), b: int = Query(...)):
    return {"a": a, "b": b, "sum": add(a, b)}

@app.post("/items", response_model=ItemOut, status_code=201)
def create_item(item: ItemIn):
    try:
        price = clamp_price(item.price)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    out = ItemOut(
        id=len(_DB) + 1,
        name=item.name,
        price=price,
        tax=calc_tax(price),
    )
    _DB.append(out)
    return out

@app.get("/items/{item_id}", response_model=ItemOut)
def get_item(item_id: int):
    for it in _DB:
        if it.id == item_id:
            return it
    raise HTTPException(status_code=404, detail="item not found")
