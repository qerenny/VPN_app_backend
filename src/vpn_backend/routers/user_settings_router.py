from typing import List
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from vpn_backend.configs.database.engine import get_db_connection
from vpn_backend.models.user_settings import UserSettings
from vpn_backend.services.user_settings_service import UserSettingsService
from vpn_backend.schemas.user_settings_schema import UserSettingsCreateSchema, UserSettingsUpdateSchema
from vpn_backend.utils.auth_handler import auth_handler
from vpn_backend.utils.check_ownership import check_ownership, get_admin_user

UserSettingsRouter = APIRouter(prefix="/user-settings", tags=["user-settings"])

def get_user_settings_service(session: AsyncSession = Depends(get_db_connection)) -> UserSettingsService:
    return UserSettingsService(session)

@UserSettingsRouter.get("/get-by-jwt")
async def get_by_jwt(
    authUserId=Depends(auth_handler.get_user),
    service: UserSettingsRouter = Depends(get_user_settings_service),
):
    return await service.get_all_by_id(authUserId)

@UserSettingsRouter.get("/get-all", response_model=List[UserSettings], description="Locked to admin users")
async def get_all(
    auth_admin_id: int = get_admin_user(),
    service: UserSettingsService = Depends(get_user_settings_service),
):
    return await service.list()

@UserSettingsRouter.get("/get-one/{id}", response_model=UserSettings, description="Locked to user who owns the settings")
async def get_user(
    id: int,
    auth_user_id: int = check_ownership(model=UserSettings, get_user_field="user_id"),
    service: UserSettingsService = Depends(get_user_settings_service),
):
    return await service.get(id)

@UserSettingsRouter.post("/create", response_model=UserSettings, description="Locked to admin users")
async def create(
    user_settings: UserSettingsCreateSchema,
    auth_admin_id: int = get_admin_user(),
    service: UserSettingsService = Depends(get_user_settings_service),
):
    return await service.create(user_settings)

@UserSettingsRouter.delete("/delete/{id}", description="Locked to admin users")
async def delete(
    id: int,
    auth_admin_id: int = get_admin_user(),
    service: UserSettingsService = Depends(get_user_settings_service),
):
    return await service.delete(id)

@UserSettingsRouter.patch("/update/{id}", response_model=UserSettings, description="Locked to admin users")
async def update(
    id: int,
    updates: UserSettingsUpdateSchema,
    auth_admin_id: int = get_admin_user(),
    service: UserSettingsService = Depends(get_user_settings_service),
):
    return await service.update(id, updates)
