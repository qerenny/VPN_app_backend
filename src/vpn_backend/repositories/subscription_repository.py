from vpn_backend.repositories.base_repository import BaseRepository
from vpn_backend.models.subscription import Subscription
from sqlmodel.ext.asyncio.session import AsyncSession


class SubscriptionRepository(BaseRepository[Subscription]):
    def __init__(self, session: AsyncSession):
        super().__init__(Subscription, session)
