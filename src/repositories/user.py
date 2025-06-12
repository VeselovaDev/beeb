from sqlalchemy import select
from sqlalchemy.orm import Session

from src.auth.exceptions import UserNotFound, WrongPassword
from src.auth.models import User


class UserRepo:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(
        self,
        username: str,
        password_hash: str,
    ) -> None:
        user = User(username=username, password_hash=password_hash)
        self.session.add(user)
        self.session.commit()

    def get_by_name(self, username: str) -> User | None:
        statement = select(User).where(User.username == username)
        result = self.session.execute(statement)
        return result.scalars().one_or_none()

    def login(self, username: str, password_hash: str) -> User:
        user = self.get_by_name(username)
        if not user:
            raise UserNotFound()
        if not password_hash == user.password_hash:
            raise WrongPassword()
        return user
