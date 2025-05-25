from typing import List
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from vpn_backend.configs.database.engine import get_db_connection
from vpn_backend.models.subscription import Subscription
from vpn_backend.services.subscription_service import SubscriptionService
from vpn_backend.schemas.subscription_schema import SubscriptionCreateSchema, SubscriptionUpdateSchema
from vpn_backend.utils.auth_handler import auth_handler

SubscriptionRouter = APIRouter(prefix="/subscriptions", tags=["subscription"])


def get_subscription_service(session: AsyncSession = Depends(get_db_connection)) -> SubscriptionService:
    return SubscriptionService(session)


@SubscriptionRouter.get("/get-all", response_model=List[Subscription])
async def get_all(
    service: SubscriptionService = Depends(get_subscription_service),
):
    return await service.list()


@SubscriptionRouter.get("/get-one/{id}", response_model=Subscription)
async def get_user(
    id: int,
    service: SubscriptionService = Depends(get_subscription_service),
):
    return await service.get(id)


@SubscriptionRouter.post("/create", response_model=Subscription)
async def create(
    subscription: SubscriptionCreateSchema,
    service: SubscriptionService = Depends(get_subscription_service),
):
    return await service.create(subscription)


@SubscriptionRouter.delete("/delete/{id}")
async def create(
    id: int,
    service: SubscriptionService = Depends(get_subscription_service),
):
    return await service.delete(id)


@SubscriptionRouter.patch("/update/{id}", response_model=Subscription)
async def update(
    id: int,
    updates: SubscriptionUpdateSchema,
    service: SubscriptionService = Depends(get_subscription_service),
):
    return await service.update(id, updates)

