from starlette.config import Config
from starlette.datastructures import Secret
from dotenv import load_dotenv

load_dotenv(".env.local")  # load local overrides
load_dotenv(".env")        # fallback

config = Config(".env")

PROJECT_NAME = "securix"
VERSION = "1.0.0"
API_PREFIX = "/api"

SECRET_KEY = config("SECRET_KEY", cast=Secret, default="CHANGEME")

POSTGRES_USER = config("POSTGRES_USER", cast=str)
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=str)
POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="db")
POSTGRES_PORT = config("POSTGRES_PORT", cast=int, default=5432)
POSTGRES_DB = config("POSTGRES_DB", cast=str)

DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

