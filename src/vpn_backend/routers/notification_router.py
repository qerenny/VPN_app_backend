from typing import List
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from vpn_backend.configs.database.engine import get_db_connection
from vpn_backend.models.notification import Notification
from vpn_backend.services.notification_service import NotificationService
from vpn_backend.schemas.notification_schema import NotificationCreateSchema, NotificationUpdateSchema
from vpn_backend.utils.auth_handler import auth_handler

NotificationRouter = APIRouter(prefix="/notifications", tags=["notification"])

def get_notification_service(session: AsyncSession = Depends(get_db_connection)) -> NotificationService:
    return NotificationService(session)

@NotificationRouter.get("/get-all", response_model=List[Notification])
async def get_all(
    service: NotificationService = Depends(get_notification_service),
):
    return await service.list()

@NotificationRouter.get("/get-one/{id}", response_model=Notification)
async def get_user(
    id: int,
    service: NotificationService = Depends(get_notification_service),
):
    return await service.get(id)

@NotificationRouter.post("/create", response_model=Notification)
async def create(
    notification: NotificationCreateSchema,
    service: NotificationService = Depends(get_notification_service),
):
    return await service.create(notification)

@NotificationRouter.delete("/delete/{id}")
async def delete(
    id: int,
    service: NotificationService = Depends(get_notification_service),
):
    return await service.delete(id)

@NotificationRouter.patch("/update/{id}", response_model=Notification)
async def update(
    id: int,
    updates: NotificationUpdateSchema,
    service: NotificationService = Depends(get_notification_service),
):
    return await service.update(id, updates)
