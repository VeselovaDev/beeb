import os

from src.auth.utils import hash_password


def test_hash_password():
    password_hash = hash_password("hamanahamana")
    assert isinstance(password_hash, bytes)


def test_hash_password_adds_salt():
    password_hash = hash_password("hamanahamana")

    # change SALT
    os.environ["SALT"] = "new salt is better"
    password_hash_new_salt = hash_password("hamanahamana")

    assert password_hash != password_hash_new_salt
