from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from decimal import Decimal

class PaymentCreateSchema(BaseModel):
    user_id: int
    subscription_id: Optional[int]
    amount: Decimal
    method: str
    status: str

class PaymentUpdateSchema(BaseModel):
    user_id: Optional[int]
    subscription_id: Optional[int]
    amount: Optional[Decimal]
    method: Optional[str]
    status: Optional[str]

