import os
from pathlib import Path

from fastapi.testclient import TestClient
import pytest
from dotenv import load_dotenv
from sqlalchemy import URL, MetaData, create_engine, text
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from src.main import build_app


class AlchemyBaseModel(DeclarativeBase):
    metadata = MetaData(schema="main")


@pytest.fixture(scope="function")
def client():
    return TestClient(
        app=build_app(),
        follow_redirects=False,
    )


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv(dotenv_path="tests/.env", override=True)


@pytest.fixture(scope="session", autouse=True)
def session():
    connection_url = URL.create(
        os.getenv("DATABASE_DIALECT"),
        username=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD"),
        host=os.getenv("DATABASE_HOST"),
        port=os.getenv("DATABASE_PORT"),
        database=os.getenv("DATABASE_NAME"),
    )
    engine = create_engine(connection_url, echo=True)
    sa_session = sessionmaker(bind=engine)
    with sa_session() as session:
        yield session
    AlchemyBaseModel.metadata.drop_all(engine)
    engine.dispose()


@pytest.fixture(scope="session", autouse=True)
def migrate(session):
    migrations_dir = Path("src/budget/migrations")
    migrations_list = list(migrations_dir.iterdir())
    for migration in sorted(migrations_list):
        with open(file=migration, mode="r") as migration_file:
            with session.begin():
                session.execute(text(migration_file.read()))
