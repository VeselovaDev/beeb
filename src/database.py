import os

from sqlalchemy import URL, MetaData, create_engine
from sqlalchemy.orm import DeclarativeBase


class AlchemyBaseModel(DeclarativeBase):
    metadata = MetaData(schema="main")


connection_url = URL.create(
    os.getenv("DATABASE_DIALECT"),
    username=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASSWORD"),
    host=os.getenv("DATABASE_HOST"),
    port=os.getenv("DATABASE_PORT"),
    database=os.getenv("DATABASE_NAME"),
)

ENGINE = create_engine(connection_url, echo=True)
