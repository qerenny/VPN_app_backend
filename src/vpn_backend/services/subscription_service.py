from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import HTTPException
from vpn_backend.models.subscription import Subscription
from vpn_backend.repositories.subscription_repository import SubscriptionRepository
from vpn_backend.schemas.subscription_schema import SubscriptionCreateSchema, SubscriptionUpdateSchema


class SubscriptionService:
    def __init__(self, session: AsyncSession):
        self.subscriptionRepository = SubscriptionRepository(session)

    async def get(self, id: int) -> Subscription:
        return await self.subscriptionRepository.get(id)

    async def get_all_by_id(self, user_id: int) -> List[Subscription]:
        return await self.subscriptionRepository.get_all_by_id(user_id)

    async def list(self) -> List[Subscription]:
        return await self.subscriptionRepository.get_all()

    async def create(self, subscription: SubscriptionCreateSchema) -> Subscription:
        return await self.subscriptionRepository.create(Subscription.model_validate(subscription))

    async def delete(self, id: int):
        return await self.subscriptionRepository.delete(id)

    async def update(
        self, id: int, updates: SubscriptionUpdateSchema,
    ) -> Subscription:
        db_obj = self.subscriptionRepository.get(id)
        if not db_obj:
            raise HTTPException(status_code=404, detail="Not found by this id")
        data = updates.model_dump(exclude_unset=True)
        for key, value in data.items():
            setattr(db_obj, key, value)
        return await self.subscriptionRepository.update(db_obj)

