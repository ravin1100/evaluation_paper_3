from asyncio import futures
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql+asyncpg://postgres:root@host:port/smart_fit"

engine = create_async_engine(url=DATABASE_URL)

AsyncSessionLocal = declarative_base(engine)


async def get_db():
    async with engine.connect() as conn:
        yield conn
