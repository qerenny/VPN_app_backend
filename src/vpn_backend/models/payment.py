from datetime import datetime, timezone
from decimal import Decimal
from typing import Optional
from sqlmodel import SQLModel, Field


class Payment(SQLModel, table=True):
    __tablename__ = "payments"

    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    subscription_id: Optional[int] = Field(default=None, foreign_key="subscriptions.id")
    amount: Decimal
    method: str = Field(max_length=50)
    status: str = Field(default="unpaid", max_length=20)
    created_at: datetime = Field(default_factory=lambda: datetime.utcnow())
