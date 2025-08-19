from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import declarative_base

Base = declarative_base()

# DATABASE_URL = "postgresql+asyncpg://postgres:root@host:port/smart_fit"

DATABASE_URL = "sqlite+aiosqlite:///database.db"


engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    future=True,
)

async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_db():
    with async_session(engine) as conn:
        yield conn
