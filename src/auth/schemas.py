from pydantic import BaseModel, Field, computed_field

from src.auth.utils import hash_password


class UserSchema(BaseModel):
    username: str = Field(
        min_length=1,
        max_length=255,
        json_schema_extra={"strip_whitespace": True},
    )
    password: str = Field(
        min_length=1,
        max_length=255,
        exclude=True,
        json_schema_extra={"strip_whitespace": True},
    )

    @computed_field
    @property
    def password_hash(cls) -> bytes:
        return hash_password(cls.password)
