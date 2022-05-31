from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from main import fetchAllNodes, shortestPath

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/list")
def list():
    return fetchAllNodes()

@app.get("/path")
def shortest_path(start: int, end: int):
    return shortestPath(start, end)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
