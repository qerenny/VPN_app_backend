from typing import List
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from vpn_backend.configs.database.engine import get_db_connection
from vpn_backend.models.subscription import Subscription
from vpn_backend.services.subscription_service import SubscriptionService
from vpn_backend.schemas.subscription_schema import SubscriptionCreateSchema, SubscriptionUpdateSchema
from vpn_backend.utils.auth_handler import auth_handler
from vpn_backend.utils.check_ownership import check_ownership, get_admin_user

SubscriptionRouter = APIRouter(prefix="/subscriptions", tags=["subscription"])


def get_subscription_service(session: AsyncSession = Depends(get_db_connection)) -> SubscriptionService:
    return SubscriptionService(session)


@SubscriptionRouter.get("/get-all", response_model=List[Subscription], description="Locked to admin users")
async def get_all(
    auth_admin_id: int = get_admin_user(),
    service: SubscriptionService = Depends(get_subscription_service),
):
    return await service.list()


@SubscriptionRouter.get("/get-one/{id}", response_model=Subscription, description="Locked to user who owns the subscription")
async def get(
    id: int,
    auth_user_id: int = check_ownership(model=Subscription, get_user_field="user_id"),
    service: SubscriptionService = Depends(get_subscription_service),
):
    return await service.get(id)


@SubscriptionRouter.post("/create", response_model=Subscription, description="Locked to admin users")
async def create(
    subscription: SubscriptionCreateSchema,
    auth_admin_id: int = get_admin_user(),
    service: SubscriptionService = Depends(get_subscription_service),
):
    return await service.create(subscription)


@SubscriptionRouter.delete("/delete/{id}", description="Locked to admin users")
async def delete(
    id: int,
    auth_admin_id: int = get_admin_user(),
    service: SubscriptionService = Depends(get_subscription_service),
):
    return await service.delete(id)


@SubscriptionRouter.patch("/update/{id}", response_model=Subscription, description="Locked to admin users")
async def update(
    id: int,
    updates: SubscriptionUpdateSchema,
    auth_admin_id: int = get_admin_user(),
    service: SubscriptionService = Depends(get_subscription_service),
):
    return await service.update(id, updates)

