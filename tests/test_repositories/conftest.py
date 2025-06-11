import pytest

from src.repositories.user import UserRepo


@pytest.fixture()
def user_repo(session):
    return UserRepo(session)
