from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field


class VPNSession(SQLModel, table=True):
    __tablename__ = "vpn_sessions"

    id: int = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="users.id")
    key_id: int = Field(foreign_key="vpn_keys.id")
    started_at: datetime = Field(description="Время подключения")
    ended_time: Optional[datetime] = None
    bytes_sent: int = Field(default=0)
    bytes_received: int = Field(default=0)
