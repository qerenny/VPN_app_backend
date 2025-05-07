from vpn_backend.repositories.base_repository import BaseRepository
from sqlmodel.ext.asyncio.session import AsyncSession
from vpn_backend.models.user import User

class UserRepository(BaseRepository[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(User, session)