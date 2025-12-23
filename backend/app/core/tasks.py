from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.db.tasks import connect_to_db, close_db_connection


async def start_app(app: FastAPI):
    await connect_to_db(app)


async def stop_app(app: FastAPI):
    await close_db_connection(app)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # run start app handler
    await start_app(app)
    yield
    # run shutdown handler
    await stop_app(app)
