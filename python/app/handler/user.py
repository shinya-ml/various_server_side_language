from datetime import datetime
from model.user import UserRequest, UserResponse

def create(user: UserRequest)-> UserResponse:
    return UserResponse(id=1, name=user.name, age=user.age, created_at=datetime.now())