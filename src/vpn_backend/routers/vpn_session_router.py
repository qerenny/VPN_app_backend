from typing import List
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from vpn_backend.configs.database.engine import get_db_connection
from vpn_backend.models.vpn_session import VPNSession
from vpn_backend.services.vpn_session_service import VPNSessionService
from vpn_backend.schemas.vpn_session_schema import VPNSessionCreateSchema, VPNSessionUpdateSchema
from vpn_backend.utils.auth_handler import auth_handler

VPNSessionRouter = APIRouter(prefix="/vpn-sessions", tags=["vpn-sessions"])

def get_vpn_session_service(session: AsyncSession = Depends(get_db_connection)) -> VPNSessionService:
    return VPNSessionService(session)

@VPNSessionRouter.get("/get-all", response_model=List[VPNSession])
async def get_all(
    service: VPNSessionService = Depends(get_vpn_session_service),
):
    return await service.list()

@VPNSessionRouter.get("/get-one/{id}", response_model=VPNSession)
async def get_user(
    id: int,
    service: VPNSessionService = Depends(get_vpn_session_service),
):
    return await service.get(id)

@VPNSessionRouter.post("/create", response_model=VPNSession)
async def create(
    vpn_session: VPNSessionCreateSchema,
    service: VPNSessionService = Depends(get_vpn_session_service),
):
    return await service.create(vpn_session)

@VPNSessionRouter.delete("/delete/{id}")
async def delete(
    id: int,
    service: VPNSessionService = Depends(get_vpn_session_service),
):
    return await service.delete(id)

@VPNSessionRouter.patch("/update/{id}", response_model=VPNSession)
async def update(
    id: int,
    updates: VPNSessionUpdateSchema,
    service: VPNSessionService = Depends(get_vpn_session_service),
):
    return await service.update(id, updates)
