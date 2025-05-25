from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class SubscriptionCreateSchema(BaseModel):
    user_id: int
    plan_name: str
    started_at: datetime
    ended_at:datetime

class SubscriptionUpdateSchema(BaseModel):
    user_id: Optional[int]
    plan_name: Optional[str]
    started_at: Optional[datetime]
    ended_at: Optional[datetime]

