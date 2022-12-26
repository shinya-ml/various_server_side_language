from psycopg import Connection
from model.user import UserResponse

class UserRepository:
    def __init__(self, conn: Connection) -> None:
        self.conn = conn
    def create(self, name: str, age: int):
        with self.conn.cursor() as cur:
            cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
            self.conn.commit()