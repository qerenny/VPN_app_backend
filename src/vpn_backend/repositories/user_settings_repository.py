from vpn_backend.repositories.base_repository import BaseRepository
from vpn_backend.models.user_settings import UserSettings
from sqlmodel.ext.asyncio.session import AsyncSession


class UserSettingsRepository(BaseRepository[UserSettings]):
    def __init__(self, session: AsyncSession):
        super().__init__(UserSettings, session)