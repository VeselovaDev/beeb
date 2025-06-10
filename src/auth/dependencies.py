from fastapi import Depends
from sqlalchemy.orm import Session

from src.dependencies import get_session
from src.repositories.user import UserRepo


def user_repo(session: Session = Depends(get_session)) -> UserRepo:
    return UserRepo(session)
