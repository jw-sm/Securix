from fastapi import FastAPI
from database import Database
from app.core.config import DATABASE_URL
import logging

logger = logging.getLogger(__name__)


# using the database pkg to establish connection to the postgresql db
# once connected, attach it as _db key to the state object on the FastAPI app.
async def connect_to_db(app: FastAPI) -> None:
    database = Database(
        DATABASE_URL, min_size=2, max_size=10
    )  # can be configured in config as well

    try:
        await database.connect()
        app.state._db = database
    except Exception as e:
        logger.warn("--- DB CONNECTION ERROR ---")
        logger.warn(e)
        logger.warn("--- DB CONNECTION ERROR ---")

# this will disconnect from the database to clean things up
async def close_db_connection(app: FastAPI) -> None:
    try:
        await app.state._db.disconnect()
    except Exception as e:
        logger.warn("--- DB DISCONECT ERROR ---")
        logger.warn(e)
        logger.warn("--- DB DISCONECT ERROR ---")
