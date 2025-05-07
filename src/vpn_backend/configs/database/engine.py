from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker, AsyncSession
from vpn_backend.configs.env import get_environment_variables
from contextlib import asynccontextmanager

env = get_environment_variables()

engine: AsyncEngine = create_async_engine(
    env.DATABASE_URL,
    echo=True,
    future=True,
)

async_session_maker = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


@asynccontextmanager
async def get_db_connection():
    async with async_session_maker() as session:
        yield session