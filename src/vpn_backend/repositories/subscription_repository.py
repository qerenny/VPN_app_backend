from vpn_backend.repositories.base_repository import BaseRepository
from vpn_backend.models.subscription import Subscription

class SubscriptionRepository(BaseRepository[Subscription]):
    def __init__(self):
        super().__init__(Subscription)