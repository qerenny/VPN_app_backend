from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class NotificationCreateSchema(BaseModel):
    user_id: int
    title: str
    message: str
    sent_at: datetime
    read_at: Optional[datetime]

class NotificationUpdateSchema(BaseModel):
    user_id: Optional[int]
    title: Optional[str]
    message: Optional[str]
    sent_at: Optional[datetime]
    read_at: Optional[datetime]

