from typing import List
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from vpn_backend.configs.database.engine import get_db_connection
from vpn_backend.models.vpn_key import VPNKey
from vpn_backend.services.vpn_key_service import VPNKeyService
from vpn_backend.schemas.vpn_key_schema import VPNKeyCreateSchema, VPNKeyUpdateSchema
from vpn_backend.utils.auth_handler import auth_handler

VPNKeyRouter = APIRouter(prefix="/vpn-keys", tags=["vpn-keys"])

def get_vpn_key_service(session: AsyncSession = Depends(get_db_connection)) -> VPNKeyService:
    return VPNKeyService(session)

@VPNKeyRouter.get("/get-all", response_model=List[VPNKey])
async def get_all(
    service: VPNKeyService = Depends(get_vpn_key_service),
):
    return await service.list()

@VPNKeyRouter.get("/get-one/{id}", response_model=VPNKey)
async def get_user(
    id: int,
    service: VPNKeyService = Depends(get_vpn_key_service),
):
    return await service.get(id)

@VPNKeyRouter.post("/create", response_model=VPNKey)
async def create(
    vpn_key: VPNKeyCreateSchema,
    service: VPNKeyService = Depends(get_vpn_key_service),
):
    return await service.create(vpn_key)

@VPNKeyRouter.delete("/delete/{id}")
async def delete(
    id: int,
    service: VPNKeyService = Depends(get_vpn_key_service),
):
    return await service.delete(id)

@VPNKeyRouter.patch("/update/{id}", response_model=VPNKey)
async def update(
    id: int,
    updates: VPNKeyUpdateSchema,
    service: VPNKeyService = Depends(get_vpn_key_service),
):
    return await service.update(id, updates)
