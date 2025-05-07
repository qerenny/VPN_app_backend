from sqlmodel import SQLModel, Field


class RouteRule(SQLModel, table=True):
    __tablename__ = "route_rules"

    id: int = Field(default=None, primary_key=True)
    profile_id: int = Field(foreign_key="route_profiles.id")
    target: str = Field(max_length=255)
    action: str = Field(max_length=100)
