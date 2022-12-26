from datetime import datetime
from model.user import UserRequest, UserResponse
from repository.user import UserRepository


class UserHandler:
    def __init__(self, repo: UserRepository):
        self.repository = repo
    def create(self, user: UserRequest)-> None:
        return self.repository.create(user.name, user.age)