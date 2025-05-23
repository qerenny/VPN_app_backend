from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import HTTPException
from vpn_backend.models.user_settings import UserSettings
from vpn_backend.repositories.user_settings_repository import UserSettingsRepository
from vpn_backend.schemas.user_settings_schema import UserSettingsCreateSchema, UserSettingsUpdateSchema


class UserSettingsService:
    def __init__(self, session: AsyncSession):
        self.userSettingsRepository = UserSettingsRepository(session)

    async def get(self, id: int) -> UserSettings:
        return await self.userSettingsRepository.get(id)

    async def list(self) -> List[UserSettings]:
        return await self.userSettingsRepository.get_all()

    async def create(self, user_settings: UserSettingsCreateSchema) -> UserSettings:
        return await self.userSettingsRepository.create(UserSettings.model_validate(user_settings))

    async def delete(self, id: int):
        return await self.userSettingsRepository.delete(id)

    async def update(
        self, id: int, updates: UserSettingsUpdateSchema,
    ) -> UserSettings:
        db_obj = await self.userSettingsRepository.get(id)
        if not db_obj:
            raise HTTPException(status_code=404, detail="Not found by this id")
        data = updates.model_dump(exclude_unset=True)
        for key, value in data.items():
            setattr(db_obj, key, value)
        return await self.userSettingsRepository.update(db_obj)
