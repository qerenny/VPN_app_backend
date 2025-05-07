from datetime import datetime, timezone
from typing import Optional
from sqlmodel import SQLModel, Field


class Notification(SQLModel, table=True):
    __tablename__ = "notifications"

    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    title: str = Field(max_length=100)
    message: str
    sent_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    read_at: Optional[datetime] = None
