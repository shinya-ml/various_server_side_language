from typing import List
from fastapi import FastAPI, status
import psycopg

from model.user import UserRequest, UserResponse
from handler.user import UserHandler
from repository.user import UserRepository

app = FastAPI()

conn = psycopg.connect('')
user_handler = UserHandler(UserRepository(conn))


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: UserRequest):
    return user_handler.create(user)


@app.get("/users", response_model=List[UserResponse])
def list_users():
    return list(user_handler.list())


@app.get("/users/{user_id}", response_model=UserResponse)
def show_user(user_id: int):
    return user_handler.show(user_id)
