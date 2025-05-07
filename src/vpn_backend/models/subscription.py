from datetime import datetime, date, timezone
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class Subscription(SQLModel, table=True):
    __tablename__ = "subscriptions"

    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", nullable=False)
    plan_name: Optional[str] = Field(default=None, max_length=100)
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
