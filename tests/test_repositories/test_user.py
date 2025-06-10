from sqlalchemy import select
from src.auth.models import User
from src.auth.utils import hash_password
from src.repositories.user import UserRepo


def test_create_user(session):
    # check that there are no users in db
    statement = select(User)
    results = session.execute(statement)
    assert results.scalars().all() == []

    # create a user
    repo = UserRepo(session)
    repo.create("boop", hash_password("shoop"))

    # fetch the new user
    statement = select(User)
    results = session.execute(statement)
    users = results.scalars().all()

    # check that only 1 user was created
    assert len(users) == 1

    # check that correct user was created
    user = users[0]
    assert user.username == "boop"
