from sqlalchemy.engine import URL

import envars as env

from .engine import create_async_engine

postgres_url = URL.create(
    drivername="postgresql+asyncpg",
    username=env.DB_USER,
    database=env.DB_NAME,
    password=env.DB_PASS,
    host=env.DB_HOST,
)

async_engine = create_async_engine(postgres_url)
