from vpn_backend.repositories.base_repository import BaseRepository
from vpn_backend.models.vpn_key import VPNKey


class VPNKeyRepository(BaseRepository[VPNKey]):
    def __init__(self):
        super().__init__(VPNKey)
