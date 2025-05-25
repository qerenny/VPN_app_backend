from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import HTTPException
from vpn_backend.models.notification import Notification
from vpn_backend.repositories.notification_repository import NotificationRepository
from vpn_backend.schemas.notification_schema import NotificationCreateSchema, NotificationUpdateSchema


class NotificationService:
    def __init__(self, session: AsyncSession):
        self.notificationRepository = NotificationRepository(session)

    async def get(self, id: int) -> Notification:
        return await self.notificationRepository.get(id)

    async def list(self) -> List[Notification]:
        return await self.notificationRepository.get_all()

    async def create(self, notification: NotificationCreateSchema) -> Notification:
        return await self.notificationRepository.create(Notification.model_validate(notification))

    async def delete(self, id: int):
        return await self.notificationRepository.delete(id)

    async def update(
        self, id: int, updates: NotificationUpdateSchema,
    ) -> Notification:
        db_obj = await self.notificationRepository.get(id)
        if not db_obj:
            raise HTTPException(status_code=404, detail="Not found by this id")
        data = updates.model_dump(exclude_unset=True)
        for key, value in data.items():
            setattr(db_obj, key, value)
        return await self.notificationRepository.update(db_obj)
