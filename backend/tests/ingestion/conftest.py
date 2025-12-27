import pytest
from sqlalchemy import create_engine

TEST_DB_URL = "postgresql://postgres:postgres@db:5432/securix_test"

@pytest.fixture(scope="session")
def engine():
    engine = create_engine(TEST_DB_URL, echo=True,)
    return engine


@pytest.fixture(scope="session", autouse=True)
def setup_schema():
    from alembic import command
    from alembic.config import Config

    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option(
    "sqlalchemy.url",
    "postgresql://postgres:postgres@db:5432/securix_test"
    )
    command.upgrade(alembic_cfg, "head")


@pytest.fixture
def db_conn(engine):
    conn = engine.connect()
    trans = conn.begin()

    yield conn

    trans.rollback()
    conn.close()
