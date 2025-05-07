from pydantic import BaseModel


class UserRegistrationSchema(BaseModel):
    email: str
    password: str


class UserLoginSchema(BaseModel):
    email: str
    password: str
