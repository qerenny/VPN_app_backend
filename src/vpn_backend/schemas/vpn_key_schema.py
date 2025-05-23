from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class VPNKeyCreateSchema(BaseModel):
    user_id: Optional[int]
    subscription_id: Optional[int]
    key_data: str
    created_at: datetime

class VPNKeyUpdateSchema(BaseModel):
    user_id: Optional[int]
    subscription_id: Optional[int]
    key_data: Optional[str]
    created_at: Optional[datetime]

