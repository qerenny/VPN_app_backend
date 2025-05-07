from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from vpn_backend.configs.env import get_environment_variables

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


async def get_db_connection() -> AsyncSession:
    async with async_session_maker() as session:
        yield session
