from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import HTTPException
from vpn_backend.models.vpn_key import VPNKey
from vpn_backend.repositories.vpn_key_repository import VPNKeyRepository
from vpn_backend.schemas.vpn_key_schema import VPNKeyCreateSchema, VPNKeyUpdateSchema


class VPNKeyService:
    def __init__(self, session: AsyncSession):
        self.vpnKeyRepository = VPNKeyRepository(session)

    async def get(self, id: int) -> VPNKey:
        return await self.vpnKeyRepository.get(id)

    async def get_all_by_id(self, user_id: int) -> List[VPNKey]:
        return await self.vpnKeyRepository.get_all_by_id(user_id)

    async def list(self) -> List[VPNKey]:
        return await self.vpnKeyRepository.get_all()

    async def create(self, vpn_key: VPNKeyCreateSchema) -> VPNKey:
        return await self.vpnKeyRepository.create(VPNKey.model_validate(vpn_key))

    async def delete(self, id: int):
        return await self.vpnKeyRepository.delete(id)

    async def update(
        self, id: int, updates: VPNKeyUpdateSchema,
    ) -> VPNKey:
        db_obj = await self.vpnKeyRepository.get(id)
        if not db_obj:
            raise HTTPException(status_code=404, detail="Not found by this id")
        data = updates.model_dump(exclude_unset=True)
        for key, value in data.items():
            setattr(db_obj, key, value)
        return await self.vpnKeyRepository.update(db_obj)
