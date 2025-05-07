from datetime import datetime, timezone
from typing import Optional
from sqlmodel import SQLModel, Field


class VPNKey(SQLModel, table=True):
    __tablename__ = "vpn_keys"

    id: int = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="users.id")
    subscription_id: Optional[int] = Field(default=None, foreign_key="subscriptions.id")
    key_data: str = Field(description="Конфиг или ключ")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
