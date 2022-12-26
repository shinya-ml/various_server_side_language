from typing import List
from model.user import UserRequest, UserResponse
from repository.user import UserRepository


class UserHandler:
    def __init__(self, repo: UserRepository):
        self.repository = repo

    def create(self, user: UserRequest) -> None:
        return self.repository.create(user.name, user.age)

    def list(self) -> List[UserResponse]:
        return self.repository.list()

    def show(self, user_id: int) -> UserResponse:
        return self.repository.get_by_id(user_id)
