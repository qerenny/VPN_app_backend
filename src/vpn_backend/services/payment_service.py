from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import HTTPException
from vpn_backend.models.payment import Payment
from vpn_backend.repositories.payment_repository import PaymentRepository
from vpn_backend.schemas.payment_schema import PaymentCreateSchema, PaymentUpdateSchema


class PaymentService:
    def __init__(self, session: AsyncSession):
        self.paymentRepository = PaymentRepository(session)

    async def get(self, id: int) -> Payment:
        return await self.paymentRepository.get(id)

    async def list(self) -> List[Payment]:
        return await self.paymentRepository.get_all()

    async def create(self, payment: PaymentCreateSchema) -> Payment:
        return await self.paymentRepository.create(Payment.model_validate(payment))

    async def delete(self, id: int):
        return await self.paymentRepository.delete(id)

    async def update(
        self, id: int, updates: PaymentUpdateSchema,
    ) -> Payment:
        db_obj = await self.paymentRepository.get(id)
        if not db_obj:
            raise HTTPException(status_code=404, detail="Not found by this id")
        data = updates.model_dump(exclude_unset=True)
        for key, value in data.items():
            setattr(db_obj, key, value)
        return await self.paymentRepository.update(db_obj)
