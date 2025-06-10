from typing import Annotated

from fastapi import Header
from sqlalchemy.orm import sessionmaker

from src.database import ENGINE


def get_session():
    session = sessionmaker(bind=ENGINE)
    try:
        yield (session := session())
    finally:
        session.close()


def get_block_name(hx_request: Annotated[str | None, Header()] = None):
    return "body" if hx_request else None
