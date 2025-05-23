from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class UserSettingsCreateSchema(BaseModel):
    user_id: int
    language: str
    theme: str
    auto_connect: bool
    dns_server: Optional[str]
    updated_at: Optional[datetime]

class UserSettingsUpdateSchema(BaseModel):
    user_id: Optional[int]
    language: Optional[str]
    theme: Optional[str]
    auto_connect: Optional[bool]
    dns_server: Optional[str]
    updated_at: Optional[datetime]

