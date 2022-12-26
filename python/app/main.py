from fastapi import FastAPI
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


@app.post("/users")
def create_user(user: UserRequest):
    return user_handler.create(user)
