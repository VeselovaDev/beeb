from hashlib import sha256
import os


def hash_password(password: str) -> bytes:
    password_encrypted = sha256(
        (f"{os.getenv('SALT')}{password}").encode("utf-8")
    ).hexdigest()
    return str.encode(password_encrypted)
