from sqlalchemy.orm import Session

from src.auth.models import User
from src.auth.schemas import UserCreate


class UserRepo:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, user: UserCreate) -> None:
        user = User(**user.model_dump())
        self.session.add(user)
        self.session.commit()
