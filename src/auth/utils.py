import os
from hashlib import sha256


def hash_password(password: str) -> bytes:
    # Encode the password as bytes
    password_bytes = (f"{os.getenv('SALT')}{password}").encode("utf-8")

    # Use SHA-256 hash function to create a hash object
    hash_object = sha256(password_bytes)

    # Get the hexadecimal representation of the hash
    password_hash = hash_object.hexdigest()

    return str.encode(password_hash)
