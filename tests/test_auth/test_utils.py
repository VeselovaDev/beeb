import os
from src.auth.utils import hash_password, is_same_password


def test_hash_password():
    password_hash = hash_password("hamanahamana")
    assert isinstance(password_hash, bytes)


def test_hash_password_adds_salt():
    password_hash = hash_password("hamanahamana")

    # change SALT
    os.environ["SALT"] = "new salt is better"
    password_hash_new_salt = hash_password("hamanahamana")

    assert password_hash != password_hash_new_salt


def test_is_same_password_pass():
    password_hash = hash_password("hamanahamana")
    assert is_same_password("hamanahamana", password_hash)


def test_is_same_password_fail():
    password_hash = hash_password("hamanahamana")
    assert not is_same_password("", password_hash)
