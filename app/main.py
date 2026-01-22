from fastapi import FastAPI
from typing import List

app = FastAPI(
    title="EKS Sample REST API",
    description="Simple REST API for Kubernetes deployment",
    version="1.0.0"
)

# In-memory sample data
items = [
    {"id": 1, "name": "Item One"},
    {"id": 2, "name": "Item Two"},
]

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/items")
def get_items() -> List[dict]:
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}

