from typing import List
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from vpn_backend.configs.database.engine import get_db_connection
from vpn_backend.models.route_profile import RouteProfile
from vpn_backend.services.route_profile_service import RouteProfileService
from vpn_backend.schemas.route_profile_schema import RouteProfileCreateSchema, RouteProfileUpdateSchema
from vpn_backend.utils.auth_handler import auth_handler
from vpn_backend.utils.check_ownership import check_ownership, get_admin_user

RouteProfileRouter = APIRouter(prefix="/route-profiles", tags=["route_profile"])


def get_route_profile_service(session: AsyncSession = Depends(get_db_connection)) -> RouteProfileService:
    return RouteProfileService(session)


@RouteProfileRouter.get("/get-all", response_model=List[RouteProfile], description="Locked to admin users")
async def get_all(
    auth_admin_id: int = get_admin_user(),
    service: RouteProfileService = Depends(get_route_profile_service),
):
    return await service.list()


@RouteProfileRouter.get("/get-one/{id}", response_model=RouteProfile, description="Locked to user who owns the route profile")
async def get(
    id: int,
    auth_user_id: int = check_ownership(model=RouteProfile, get_user_field="user_id"),
    service: RouteProfileService = Depends(get_route_profile_service),
):
    return await service.get(id)


@RouteProfileRouter.post("/create", response_model=RouteProfile, description="Locked to admin users")
async def create(
    route_profile: RouteProfileCreateSchema,
    auth_admin_id: int = get_admin_user(),
    service: RouteProfileService = Depends(get_route_profile_service),
):
    return await service.create(route_profile)


@RouteProfileRouter.delete("/delete/{id}", description="Locked to admin users")
async def delete(
    id: int,
    auth_admin_id: int = get_admin_user(),
    service: RouteProfileService = Depends(get_route_profile_service),
):
    return await service.delete(id)


@RouteProfileRouter.patch("/update/{id}", response_model=RouteProfile, description="Locked to admin users")
async def update(
    id: int,
    updates: RouteProfileUpdateSchema,
    auth_admin_id: int = get_admin_user(),
    service: RouteProfileService = Depends(get_route_profile_service),
):
    return await service.update(id, updates)
