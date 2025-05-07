from vpn_backend.repositories.base_repository import BaseRepository
from vpn_backend.models.notification import Notification

class NotificationRepository(BaseRepository[Notification]):
    def __init__(self):
        super().__init__(Notification)