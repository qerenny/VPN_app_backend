from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class RouteRuleCreateSchema(BaseModel):
    profile_id: int
    target: str
    action: str

class RouteRuleUpdateSchema(BaseModel):
    profile_id: Optional[int]
    target: Optional[str]
    action: Optional[str]

