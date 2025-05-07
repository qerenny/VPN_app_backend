from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field


class UserSettings(SQLModel, table=True):
    __tablename__ = "user_settings"

    user_id: int = Field(primary_key=True, foreign_key="users.id")
    language: str = Field(default="en", max_length=10)
    theme: str = Field(default="black", max_length=10)
    auto_connect: bool = Field(default=False)
    dns_server: Optional[str] = Field(default=None, max_length=100)
    updated_at: Optional[datetime] = None
