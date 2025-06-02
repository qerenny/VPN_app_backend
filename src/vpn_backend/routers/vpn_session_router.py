from typing import List
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from vpn_backend.configs.database.engine import get_db_connection
from vpn_backend.models.vpn_session import VPNSession
from vpn_backend.services.vpn_session_service import VPNSessionService
from vpn_backend.schemas.vpn_session_schema import VPNSessionCreateSchema, VPNSessionUpdateSchema
from vpn_backend.utils.auth_handler import auth_handler
from vpn_backend.utils.check_ownership import check_ownership, get_admin_user

VPNSessionRouter = APIRouter(prefix="/vpn-sessions", tags=["vpn-sessions"])

def get_vpn_session_service(session: AsyncSession = Depends(get_db_connection)) -> VPNSessionService:
    return VPNSessionService(session)

@VPNSessionRouter.get("/get-all", response_model=List[VPNSession], description="Locked to admin users")
async def get_all(
    auth_admin_id: int = get_admin_user(),
    service: VPNSessionService = Depends(get_vpn_session_service),
):
    return await service.list()

@VPNSessionRouter.get("/get-one/{id}", response_model=VPNSession, description="Locked to user who owns the VPN session")
async def get(
    id: int,
    auth_user_id: int = check_ownership(model=VPNSession, get_user_field="user_id"),
    service: VPNSessionService = Depends(get_vpn_session_service),
):
    return await service.get(id)

@VPNSessionRouter.post("/create", response_model=VPNSession, description="Locked to admin users")
async def create(
    vpn_session: VPNSessionCreateSchema,
    auth_admin_id: int = get_admin_user(),
    service: VPNSessionService = Depends(get_vpn_session_service),
):
    return await service.create(vpn_session)

@VPNSessionRouter.delete("/delete/{id}", description="Locked to admin users")
async def delete(
    id: int,
    auth_admin_id: int = get_admin_user(),
    service: VPNSessionService = Depends(get_vpn_session_service),
):
    return await service.delete(id)

@VPNSessionRouter.patch("/update/{id}", response_model=VPNSession, description="Locked to admin users")
async def update(
    id: int,
    updates: VPNSessionUpdateSchema,
    auth_admin_id: int = get_admin_user(),
    service: VPNSessionService = Depends(get_vpn_session_service),
):
    return await service.update(id, updates)
