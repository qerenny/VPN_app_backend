from typing import List
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from vpn_backend.configs.database.engine import get_db_connection
from vpn_backend.models.route_profile import RouteProfile
from vpn_backend.services.route_profile_service import RouteProfileService
from vpn_backend.schemas.route_profile_schema import RouteProfileCreateSchema, RouteProfileUpdateSchema
from vpn_backend.utils.auth_handler import auth_handler

RouteProfileRouter = APIRouter(prefix="/route-profiles", tags=["route_profile"])


def get_route_profile_service(session: AsyncSession = Depends(get_db_connection)) -> RouteProfileService:
    return RouteProfileService(session)


@RouteProfileRouter.get("/get-all", response_model=List[RouteProfile])
async def get_all(
    service: RouteProfileService = Depends(get_route_profile_service),
):
    return await service.list()


@RouteProfileRouter.get("/get-one/{id}", response_model=RouteProfile)
async def get_user(
    id: int,
    service: RouteProfileService = Depends(get_route_profile_service),
):
    return await service.get(id)


@RouteProfileRouter.post("/create", response_model=RouteProfile)
async def create(
    route_profile: RouteProfileCreateSchema,
    service: RouteProfileService = Depends(get_route_profile_service),
):
    return await service.create(route_profile)


@RouteProfileRouter.delete("/delete/{id}")
async def delete(
    id: int,
    service: RouteProfileService = Depends(get_route_profile_service),
):
    return await service.delete(id)


@RouteProfileRouter.patch("/update/{id}", response_model=RouteProfile)
async def update(
    id: int,
    updates: RouteProfileUpdateSchema,
    service: RouteProfileService = Depends(get_route_profile_service),
):
    return await service.update(id, updates)
