from vpn_backend.repositories.base_repository import BaseRepository
from vpn_backend.models.route_rule import RouteRule
from sqlmodel.ext.asyncio.session import AsyncSession


class RouteRuleRepository(BaseRepository[RouteRule]):
    def __init__(self, session: AsyncSession):
        super().__init__(RouteRule, session)