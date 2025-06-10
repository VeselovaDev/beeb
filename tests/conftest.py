from pathlib import Path

import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from src.application import build_app
from src.database import ENGINE, AlchemyBaseModel


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv(dotenv_path="tests/.env", override=True)


@pytest.fixture(scope="function")
def authenticated_client():
    return TestClient(
        app=build_app(),
        follow_redirects=False,
        cookies={"token": "lol"},
    )


@pytest.fixture(scope="function")
def unauthenticated_client():
    return TestClient(
        app=build_app(),
        follow_redirects=False,
    )


@pytest.fixture(scope="session", autouse=True)
def session():
    sa_session = sessionmaker(bind=ENGINE)
    with sa_session() as session:
        yield session
    AlchemyBaseModel.metadata.drop_all(ENGINE)
    ENGINE.dispose()


@pytest.fixture(scope="session", autouse=True)
def migrate(session):
    migration = Path("src/migrations") / "0000_init.sql"
    with open(file=migration, mode="r") as migration_file:
        with session.begin():
            session.execute(text(migration_file.read()))
