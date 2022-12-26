from typing import List
from psycopg import Connection
from psycopg.rows import class_row
from model.user import UserResponse


class UserRepository:
    def __init__(self, conn: Connection) -> None:
        self.conn = conn

    def create(self, name: str, age: int):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
            self.conn.commit()

    def list(self) -> List[UserResponse]:
        with self.conn.cursor(row_factory=class_row(UserResponse)) as cur:
            cur.execute("SELECT id, name, age, created_at from users")
            return cur.fetchall()

    def get_by_id(self, id: int) -> UserResponse:
        with self.conn.cursor(row_factory=class_row(UserResponse)) as cur:
            cur.execute("SELECT * from users WHERE id = %s", (id,))
            return cur.fetchone()
