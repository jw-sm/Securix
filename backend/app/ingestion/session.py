from database import Database
from sqlalchemy import create_engine
from app.core.config import DATABASE_URL

database = Database(DATABASE_URL)

engine = create_engine(str(:))
