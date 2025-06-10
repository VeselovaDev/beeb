from pathlib import Path

import pytest
from sqlalchemy import text


@pytest.fixture(scope="session")
def migrate_auth(session):
    migration = Path("src/migrations") / "0001_user.sql"
    with open(file=migration, mode="r") as migration_file:
        with session.begin():
            session.execute(text(migration_file.read()))
