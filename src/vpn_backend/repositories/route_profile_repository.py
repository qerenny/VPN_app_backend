from vpn_backend.repositories.base_repository import BaseRepository
from vpn_backend.models.route_profile import RouteProfile
from sqlmodel.ext.asyncio.session import AsyncSession


class RouteProfileRepository(BaseRepository[RouteProfile]):
    def __init__(self, session: AsyncSession):
        super().__init__(RouteProfile, session)
