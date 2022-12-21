from fastapi import FastAPI

from model.user import UserRequest, UserResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/users", response_model=UserResponse)
def create_user(user: UserRequest):
    return {"id": 1, "name": "string", "age": 24, "created_at": "hoge"}
