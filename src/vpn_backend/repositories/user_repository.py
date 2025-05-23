from vpn_backend.repositories.base_repository import BaseRepository
from sqlmodel.ext.asyncio.session import AsyncSession
from vpn_backend.models.user import User
from typing import TypeVar, Generic, Optional, Type, List
from sqlmodel import select, SQLModel


class UserRepository(BaseRepository[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(User, session)

    async def get_by_email(self, email: str) -> Optional[User]:
        result = await self.session.exec(select(self.model).where(self.model.email == email))
        return result.first()