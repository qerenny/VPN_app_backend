from typing import List
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from vpn_backend.configs.database.engine import get_db_connection
from vpn_backend.models.notification import Notification
from vpn_backend.services.notification_service import NotificationService
from vpn_backend.schemas.notification_schema import NotificationCreateSchema, NotificationUpdateSchema
from vpn_backend.utils.auth_handler import auth_handler
from vpn_backend.utils.check_ownership import check_ownership, get_admin_user

NotificationRouter = APIRouter(prefix="/notifications", tags=["notification"])

def get_notification_service(session: AsyncSession = Depends(get_db_connection)) -> NotificationService:
    return NotificationService(session)

@NotificationRouter.get("/get-all", response_model=List[Notification], description="Locked to admin users")
async def get_all(
    auth_admin_id: int = get_admin_user(),
    service: NotificationService = Depends(get_notification_service),
):
    return await service.list()

@NotificationRouter.get("/get-one/{id}", response_model=Notification, description="Locked to user who owns the notification")
async def get(
    id: int,
    auth_user_id: int = check_ownership(model=Notification, get_user_field="user_id"),
    service: NotificationService = Depends(get_notification_service),
):
    return await service.get(id)

@NotificationRouter.post("/create", response_model=Notification, description="Locked to admin users")
async def create(
    notification: NotificationCreateSchema,
    auth_admin_id: int = get_admin_user(),
    service: NotificationService = Depends(get_notification_service),
):
    return await service.create(notification)

@NotificationRouter.delete("/delete/{id}", description="Locked to admin users")
async def delete(
    id: int,
    auth_admin_id: int = get_admin_user(),
    service: NotificationService = Depends(get_notification_service),
):
    return await service.delete(id)

@NotificationRouter.patch("/update/{id}", response_model=Notification, description="Locked to admin users")
async def update(
    id: int,
    updates: NotificationUpdateSchema,
    auth_user_id: int = check_ownership(model=Notification, get_user_field="user_id"),
    service: NotificationService = Depends(get_notification_service),
):
    return await service.update(id, updates)
