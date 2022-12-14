from pydantic import BaseModel
from datetime import datetime
from dataclasses import dataclass


class UserRequest(BaseModel):
    name: str
    age: int


class UserResponse(BaseModel):
    id: int
    name: str
    age: int
    created_at: datetime
