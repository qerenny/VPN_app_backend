from typing import List
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from vpn_backend.configs.database.engine import get_db_connection
from vpn_backend.models.payment import Payment
from vpn_backend.services.payment_service import PaymentService
from vpn_backend.schemas.payment_schema import PaymentCreateSchema, PaymentUpdateSchema
from vpn_backend.utils.auth_handler import auth_handler

PaymentRouter = APIRouter(prefix="/payments", tags=["payment"])

def get_payment_service(session: AsyncSession = Depends(get_db_connection)) -> PaymentService:
    return PaymentService(session)

@PaymentRouter.get("/get-all", response_model=List[Payment])
async def get_all(
    service: PaymentService = Depends(get_payment_service),
):
    return await service.list()

@PaymentRouter.get("/get-one/{id}", response_model=Payment)
async def get_user(
    id: int,
    service: PaymentService = Depends(get_payment_service),
):
    return await service.get(id)

@PaymentRouter.post("/create", response_model=Payment)
async def create(
    payment: PaymentCreateSchema,
    service: PaymentService = Depends(get_payment_service),
):
    return await service.create(payment)

@PaymentRouter.delete("/delete/{id}")
async def delete(
    id: int,
    service: PaymentService = Depends(get_payment_service),
):
    return await service.delete(id)

@PaymentRouter.patch("/update/{id}", response_model=Payment)
async def update(
    id: int,
    updates: PaymentUpdateSchema,
    service: PaymentService = Depends(get_payment_service),
):
    return await service.update(id, updates)
