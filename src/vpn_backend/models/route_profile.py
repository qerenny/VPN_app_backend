from datetime import datetime, timezone
from sqlmodel import SQLModel, Field


class RouteProfile(SQLModel, table=True):
    __tablename__ = "route_profiles"

    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    name: str = Field(max_length=100)
    created_at: datetime = Field(default_factory=lambda: datetime.utcnow())
