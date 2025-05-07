from vpn_backend.repositories.base_repository import BaseRepository
from vpn_backend.models.route_rule import RouteRule


class RouteRuleRepository(BaseRepository[RouteRule]):
    def __init__(self):
        super().__init__(RouteRule)
