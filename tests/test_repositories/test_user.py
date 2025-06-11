import pytest
from sqlalchemy import select

from src.auth.exceptions import UserNotFound, WrongPassword
from src.auth.models import User
from src.auth.utils import hash_password
from src.repositories.user import UserRepo


def test_create_user(user_repo, session):
    # check that there are no users in db
    statement = select(User)
    results = session.execute(statement)
    assert results.scalars().all() == []

    # create a user
    user_repo.create("boop", "shoop")

    # fetch the new user
    statement = select(User)
    results = session.execute(statement)
    users = results.scalars().all()

    # check that only 1 user was created
    assert len(users) == 1

    # check that correct user was created
    user = users[0]
    assert user.username == "boop"

    # check that password is stored correctly

    assert user.password_hash_sum == hash_password("shoop")


def test_fetch_user_by_name_when_user_exists(user_repo):
    user_repo.create("shlorp", hash_password("blorp"))

    user = user_repo.get_by_name("shlorp")
    assert user.username == "shlorp"


def test_fetch_user_by_name_when_no_such_user_exists(user_repo):
    user = user_repo.get_by_name("glorp")
    assert not user


def test_user_login_success(user_repo):
    user_repo.create("imauser", "verysecret")

    user = user_repo.login("imauser", "verysecret")

    assert user.username == "imauser"


def test_user_login_no_user(user_repo):
    with pytest.raises(UserNotFound):
        user_repo.login("nosuchuser", "password")


def test_user_login_wrong_password(user_repo):
    user_repo.create("forgetful_user", "strongpassword")
    with pytest.raises(WrongPassword):
        user_repo.login("forgetful_user", "whatwasit")
