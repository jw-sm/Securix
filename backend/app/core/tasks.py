from typing import Callable
from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.db.tasks import connect_to_db, close_db_connection


# These functions will run when the application starts up
# and when the application shuts down.


def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        await connect_to_db(app)

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        await close_db_connection(app)

    return stop_app

@asynccontextmanager
async def lifespan(app: FastAPI):
    # run start app handler
    await create_start_app_handler(app)()
    yield
    # run shutdown handler
    await create_stop_app_handler(app)()
