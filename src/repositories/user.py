from sqlalchemy.orm import Session

from src.auth.models import User
from src.auth.utils import hash_password


class UserRepo:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(
        self,
        username: str,
        password: str,
    ) -> None:
        user = User(username=username, password_hash_sum=hash_password(password))
        self.session.add(user)
        self.session.commit()
