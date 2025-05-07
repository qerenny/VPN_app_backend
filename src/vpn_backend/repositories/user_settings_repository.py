from vpn_backend.repositories.base_repository import BaseRepository
from vpn_backend.models.user_settings import UserSettings


class UserSettingsRepository(BaseRepository[UserSettings]):
    def __init__(self):
        super().__init__(UserSettings)
