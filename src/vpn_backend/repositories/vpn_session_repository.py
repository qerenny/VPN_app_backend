from vpn_backend.repositories.base_repository import BaseRepository
from vpn_backend.models.vpn_session import VPNSession

class VPNSessionRepository(BaseRepository[VPNSession]):
    def __init__(self):
        super().__init__(VPNSession)