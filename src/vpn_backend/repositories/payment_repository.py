from vpn_backend.repositories.base_repository import BaseRepository
from vpn_backend.models.payment import Payment
from sqlmodel.ext.asyncio.session import AsyncSession


class PaymentRepository(BaseRepository[Payment]):
    def __init__(self, session: AsyncSession):
        super().__init__(Payment, session)