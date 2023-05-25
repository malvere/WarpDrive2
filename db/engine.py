from typing import Union

from sqlalchemy import MetaData, inspect
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker as sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine as create_engine


def create_async_engine(url: Union[URL, str]) -> AsyncEngine:
    return create_engine(url=url, echo=True, pool_pre_ping=True)


def check_tables(conn):
    inspector = inspect(conn)
    return inspector.get_table_names()


async def proceed_schemas(engine: AsyncEngine, metadata: MetaData, table) -> None:
    async with engine.begin() as conn:
        tables = await conn.run_sync(check_tables)
        if table not in tables:
            print("\n\nNot in DB\n\n")
            await conn.run_sync(metadata.create_all)
        else:
            print("\n\nTable Exists\n\n")


def get_session_maker(engine: AsyncEngine) -> sessionmaker:
    return sessionmaker(engine)
