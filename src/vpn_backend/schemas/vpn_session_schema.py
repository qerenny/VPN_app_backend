from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class VPNSessionCreateSchema(BaseModel):
    user_id: Optional[int]
    key_id: int
    started_at: datetime
    ended_time: Optional[datetime]
    bytes_sent: int
    bytes_received: int

class VPNSessionUpdateSchema(BaseModel):
    user_id: Optional[int]
    key_id: Optional[int]
    started_at: Optional[datetime]
    ended_time: Optional[datetime]
    bytes_sent: Optional[int]
    bytes_received: Optional[int]

