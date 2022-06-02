# Import untuk membuat server
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import algoritma
from main import fetchAllNodes, shortestPath, shortestPathtoAllNode

# Inisialisasi server
app = FastAPI()

# Mengatur supaya server bisa diakses dari mana saja
origins = ["*"]
app.add_middleware(CORSMiddleware,allow_origins=origins,allow_credentials=True,allow_methods=["*"],allow_headers=["*"])


# Daftar URL dari server

@app.get("/list")
def list():
    return fetchAllNodes()

@app.get("/path")
def shortest_path(start: int, end: int):
    return shortestPath(start, end)

@app.get("/maranatha")
def maranatha():
    return shortestPathtoAllNode(0)