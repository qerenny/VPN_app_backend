from vpn_backend.repositories.base_repository import BaseRepository
from vpn_backend.models.route_profile import RouteProfile

class RouteProfileRepository(BaseRepository[RouteProfile]):
    def __init__(self):
        super().__init__(RouteProfile)