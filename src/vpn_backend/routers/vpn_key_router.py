from typing import List
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from vpn_backend.configs.database.engine import get_db_connection
from vpn_backend.models.vpn_key import VPNKey
from vpn_backend.services.vpn_key_service import VPNKeyService
from vpn_backend.schemas.vpn_key_schema import VPNKeyCreateSchema, VPNKeyUpdateSchema
from vpn_backend.utils.auth_handler import auth_handler
from vpn_backend.utils.check_ownership import check_ownership, get_admin_user

VPNKeyRouter = APIRouter(prefix="/vpn-keys", tags=["vpn-keys"])

def get_vpn_key_service(session: AsyncSession = Depends(get_db_connection)) -> VPNKeyService:
    return VPNKeyService(session)

@VPNKeyRouter.get("/get-all", response_model=List[VPNKey], description="Locked to admin users")
async def get_all(
    auth_admin_id: int = get_admin_user(),
    service: VPNKeyService = Depends(get_vpn_key_service),
):
    return await service.list()

@VPNKeyRouter.get("/get-one/{id}", response_model=VPNKey, description="Locked to user who owns the VPN key")
async def get(
    id: int,
    auth_user_id: int = check_ownership(model=VPNKey, get_user_field="user_id"),
    service: VPNKeyService = Depends(get_vpn_key_service),
):
    return await service.get(id)

@VPNKeyRouter.post("/create", response_model=VPNKey, description="Locked to admin users")
async def create(
    vpn_key: VPNKeyCreateSchema,
    auth_admin_id: int = get_admin_user(),
    service: VPNKeyService = Depends(get_vpn_key_service),
):
    return await service.create(vpn_key)

@VPNKeyRouter.delete("/delete/{id}", description="Locked to admin users")
async def delete(
    id: int,
    auth_admin_id: int = get_admin_user(),
    service: VPNKeyService = Depends(get_vpn_key_service),
):
    return await service.delete(id)

@VPNKeyRouter.patch("/update/{id}", response_model=VPNKey, description="Locked to admin users")
async def update(
    id: int,
    updates: VPNKeyUpdateSchema,
    auth_admin_id: int = get_admin_user(),
    service: VPNKeyService = Depends(get_vpn_key_service),
):
    return await service.update(id, updates)
