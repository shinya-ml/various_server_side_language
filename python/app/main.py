from fastapi import FastAPI
import psycopg2

from model.user import UserRequest, UserResponse
from handler.user import create

app = FastAPI()

conn = psycopg2.connect('')


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/users", response_model=UserResponse)
def create_user(user: UserRequest):
    return create(user)
