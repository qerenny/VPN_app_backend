from vpn_backend.repositories.base_repository import BaseRepository
from vpn_backend.models.user import User

class UserRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__(User)