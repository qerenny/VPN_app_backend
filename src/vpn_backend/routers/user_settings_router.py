from typing import List
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from vpn_backend.configs.database.engine import get_db_connection
from vpn_backend.models.user_settings import UserSettings
from vpn_backend.services.user_settings_service import UserSettingsService
from vpn_backend.schemas.user_settings_schema import UserSettingsCreateSchema, UserSettingsUpdateSchema
from vpn_backend.utils.auth_handler import auth_handler

UserSettingsRouter = APIRouter(prefix="/user-settings", tags=["user-settings"])

def get_user_settings_service(session: AsyncSession = Depends(get_db_connection)) -> UserSettingsService:
    return UserSettingsService(session)

@UserSettingsRouter.get("/get-all", response_model=List[UserSettings])
async def get_all(
    service: UserSettingsService = Depends(get_user_settings_service),
):
    return await service.list()

@UserSettingsRouter.get("/get-one/{id}", response_model=UserSettings)
async def get_user(
    id: int,
    service: UserSettingsService = Depends(get_user_settings_service),
):
    return await service.get(id)

@UserSettingsRouter.post("/create", response_model=UserSettings)
async def create(
    user_settings: UserSettingsCreateSchema,
    service: UserSettingsService = Depends(get_user_settings_service),
):
    return await service.create(user_settings)

@UserSettingsRouter.delete("/delete/{id}")
async def delete(
    id: int,
    service: UserSettingsService = Depends(get_user_settings_service),
):
    return await service.delete(id)

@UserSettingsRouter.patch("/update/{id}", response_model=UserSettings)
async def update(
    id: int,
    updates: UserSettingsUpdateSchema,
    service: UserSettingsService = Depends(get_user_settings_service),
):
    return await service.update(id, updates)
