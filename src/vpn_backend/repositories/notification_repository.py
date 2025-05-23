from vpn_backend.repositories.base_repository import BaseRepository
from vpn_backend.models.notification import Notification
from sqlmodel.ext.asyncio.session import AsyncSession


class NotificationRepository(BaseRepository[Notification]):
    def __init__(self, session: AsyncSession):
        super().__init__(Notification, session)
