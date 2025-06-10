import os
from pathlib import Path

from dotenv import load_dotenv


def test_connection_to_correct_db(load_env):
    assert os.environ["DATABASE_NAME"] == "beeb-test"
