from typing import Optional
from app.utils.utils import metadata

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_home():
    return ("Hello 👋, Siddhant Here")


@app.get("/api/{id}")
def get_metadata(id: str):
    meta = metadata(id)
    return meta