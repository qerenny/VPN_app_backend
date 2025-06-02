from typing import List
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from vpn_backend.configs.database.engine import get_db_connection
from vpn_backend.models.payment import Payment
from vpn_backend.services.payment_service import PaymentService
from vpn_backend.schemas.payment_schema import PaymentCreateSchema, PaymentUpdateSchema
from vpn_backend.utils.auth_handler import auth_handler
from vpn_backend.utils.check_ownership import check_ownership, get_admin_user

PaymentRouter = APIRouter(prefix="/payments", tags=["payment"])

def get_payment_service(session: AsyncSession = Depends(get_db_connection)) -> PaymentService:
    return PaymentService(session)

@PaymentRouter.get("/get-all", response_model=List[Payment], description="Locked to admin users")
async def get_all(
    auth_admin_id: int = get_admin_user(),
    service: PaymentService = Depends(get_payment_service),
):
    return await service.list()

@PaymentRouter.get("/get-one/{id}", response_model=Payment, description="Locked to user who owns the payment")
async def get(
    id: int,
    auth_user_id: int = check_ownership(model=Payment, get_user_field="user_id"),
    service: PaymentService = Depends(get_payment_service),
):
    return await service.get(id)

@PaymentRouter.post("/create", response_model=Payment, description="Locked to admin users")
async def create(
    payment: PaymentCreateSchema,
    auth_admin_id: int = get_admin_user(),
    service: PaymentService = Depends(get_payment_service),
):
    return await service.create(payment)

@PaymentRouter.delete("/delete/{id}", description="Locked to admin users")
async def delete(
    id: int,
    auth_admin_id: int = get_admin_user(),
    service: PaymentService = Depends(get_payment_service),
):
    return await service.delete(id)

@PaymentRouter.patch("/update/{id}", response_model=Payment, description="Locked to admin users")
async def update(
    id: int,
    updates: PaymentUpdateSchema,
    auth_admin_id: int = get_admin_user(),
    service: PaymentService = Depends(get_payment_service),
):
    return await service.update(id, updates)
