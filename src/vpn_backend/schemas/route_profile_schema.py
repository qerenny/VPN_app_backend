from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class RouteProfileCreateSchema(BaseModel):
    user_id: int
    name: str

class RouteProfileUpdateSchema(BaseModel):
    user_id: Optional[int]
    name: Optional[str]

