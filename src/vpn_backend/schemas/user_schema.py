from pydantic import BaseModel
from typing import Optional, List


class UserRegistrationSchema(BaseModel):
    email: str
    password: str


class UserLoginSchema(BaseModel):
    email: str
    password: str


class UserUpdateSchema(BaseModel):
    email: Optional[str]
    password: Optional[str]
