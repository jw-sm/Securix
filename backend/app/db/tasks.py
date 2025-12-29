import asyncio
import logging
from fastapi import FastAPI 
from databases import Database
from app.core.config import DATABASE_URL

logger = logging.getLogger(__name__)

MAX_RETRIES = 5
RETRY_DELAY = 3  

def create_database() -> Database:
    """Factory for creating Database instances."""
    return Database(DATABASE_URL, min_size=2, max_size=10)

async def connect_to_db(app: FastAPI) -> None:
    """Connect to the database with retries."""
    db = create_database()
    attempt = 0

    while attempt < MAX_RETRIES:
        try:
            await db.connect()
            app.state._db = db
            logger.info("✅ Connected to database")
            return
        except Exception as e:
            attempt += 1
            logger.warning(f"--- DB CONNECTION ERROR (attempt {attempt}) ---")
            logger.exception(e)
            if attempt < MAX_RETRIES:
                logger.info(f"Retrying in {RETRY_DELAY} seconds...")
                await asyncio.sleep(RETRY_DELAY)
            else:
                logger.error("Could not connect to database after multiple attempts.")
                raise

async def close_db_connection(app: FastAPI) -> None:
    """Disconnect from the database safely."""
    db = getattr(app.state, "_db", None)
    if db:
        try:
            await db.disconnect()
            logger.info("✅ Disconnected from database")
        except Exception as e:
            logger.warning("--- DB DISCONNECT ERROR ---")
            logger.exception(e)

