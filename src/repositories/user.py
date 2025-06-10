from sqlalchemy import select
from sqlalchemy.orm import Session

from src.auth.exceptions import UserNotFound, WrongPassword
from src.auth.models import User
from src.auth.utils import hash_password, is_same_password


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

    def fetch_by(self, username: str) -> User | None:
        statement = select(User).where(User.username == username)
        result = self.session.execute(statement)
        return result.scalars().one_or_none()

    def login(self, username: str, password: str) -> User:
        user = self.fetch_by(username)
        if not user:
            raise UserNotFound()
        if not is_same_password(password, user.password_hash_sum):
            raise WrongPassword()
        return user
