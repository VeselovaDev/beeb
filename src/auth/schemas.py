from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    username: str = Field(
        max_length=255,
        json_schema_extra={"strip_whitespace": True},
    )
    password: str = Field(
        max_length=255,
        exclude=True,
        json_schema_extra={"strip_whitespace": True},
    )
