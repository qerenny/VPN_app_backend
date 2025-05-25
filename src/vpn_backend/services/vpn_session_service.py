from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import HTTPException
from vpn_backend.models.vpn_session import VPNSession
from vpn_backend.repositories.vpn_session_repository import VPNSessionRepository
from vpn_backend.schemas.vpn_session_schema import VPNSessionCreateSchema, VPNSessionUpdateSchema


class VPNSessionService:
    def __init__(self, session: AsyncSession):
        self.vpnSessionRepository = VPNSessionRepository(session)

    async def get(self, id: int) -> VPNSession:
        return await self.vpnSessionRepository.get(id)

    async def list(self) -> List[VPNSession]:
        return await self.vpnSessionRepository.get_all()

    async def create(self, vpn_session: VPNSessionCreateSchema) -> VPNSession:
        return await self.vpnSessionRepository.create(VPNSession.model_validate(vpn_session))

    async def delete(self, id: int):
        return await self.vpnSessionRepository.delete(id)

    async def update(
        self, id: int, updates: VPNSessionUpdateSchema,
    ) -> VPNSession:
        db_obj = await self.vpnSessionRepository.get(id)
        if not db_obj:
            raise HTTPException(status_code=404, detail="Not found by this id")
        data = updates.model_dump(exclude_unset=True)
        for key, value in data.items():
            setattr(db_obj, key, value)
        return await self.vpnSessionRepository.update(db_obj)
