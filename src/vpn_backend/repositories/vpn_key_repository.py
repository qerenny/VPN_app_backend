from vpn_backend.repositories.base_repository import BaseRepository
from vpn_backend.models.vpn_key import VPNKey
from sqlmodel.ext.asyncio.session import AsyncSession


class VPNKeyRepository(BaseRepository[VPNKey]):
    def __init__(self, session: AsyncSession):
        super().__init__(VPNKey, session)