from vpn_backend.repositories.base_repository import BaseRepository
from vpn_backend.models.vpn_session import VPNSession
from sqlmodel.ext.asyncio.session import AsyncSession


class VPNSessionRepository(BaseRepository[VPNSession]):
    def __init__(self, session: AsyncSession):
        super().__init__(VPNSession, session)