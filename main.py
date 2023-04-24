from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="E-shop"
)
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000/",
    'http://212.109.195.83:8080/',
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = [
    {"id": 1, "image": "1.webp", "name": "T-shirt 1", "price": 150, "article": "0001", "available": 1},
    {"id": 2, "image": "2.webp", "name": "T-shirt 2", "price": 210, "article": "0002", "available": 1},
    {"id": 3, "image": "3.webp", "name": "T-shirt 3", "price": 180, "article": "0003", "available": 1},
    {"id": 4, "image": "4.webp", "name": "T-shirt 4", "price": 4000, "article": "0004", "available": 1},
    {"id": 5, "image": "5.webp", "name": "T-shirt 5", "price": 350, "article": "0005", "available": 1},
    {"id": 6, "image": "6.webp", "name": "T-shirt 6", "price": 250, "article": "0006", "available": 1},
    {"id": 7, "image": "6.webp", "name": "T-shirt 7", "price": 2550, "article": "0007", "available": 1},
    {"id": 8, "image": "6.webp", "name": "T-shirt 8", "price": 288, "article": "0008", "available": 1}
]


@app.get('/products')
def products():
    return db


@app.get('/')
def home():
    return db
