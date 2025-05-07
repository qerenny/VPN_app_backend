from vpn_backend.repositories.base_repository import BaseRepository
from vpn_backend.models.payment import Payment


class PaymentRepository(BaseRepository[Payment]):
    def __init__(self):
        super().__init__(Payment)
