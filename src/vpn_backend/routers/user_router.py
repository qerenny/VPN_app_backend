from typing import List
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from vpn_backend.configs.database.engine import get_db_connection
from vpn_backend.services.user_service import UserService
from vpn_backend.models.user import User
from vpn_backend.schemas.user_schema import UserRegistrationSchema, UserLoginSchema, UserUpdateSchema
from vpn_backend.utils.auth_handler import auth_handler
from vpn_backend.utils.check_ownership import check_ownership, get_admin_user

UserRouter = APIRouter(prefix="/users", tags=["user"])


def get_user_service(session: AsyncSession = Depends(get_db_connection)) -> UserService:
    return UserService(session)


@UserRouter.post("/registration")
async def registration(
    body: UserRegistrationSchema,
    service: UserService = Depends(get_user_service),
):
    return await service.registration(body)


@UserRouter.post("/login")
async def login(
    body: UserLoginSchema,
    service: UserService = Depends(get_user_service),
):
    return await service.login(body)


@UserRouter.post("/me")
async def me(
    authUserId=Depends(auth_handler.get_user),
    service: UserService = Depends(get_user_service),
):
    return await service.me(authUserId)


@UserRouter.get("/get-all", response_model=List[User], description="Locked to admin users")
async def get_all(
    auth_admin_id: int = get_admin_user(),
    service: UserService = Depends(get_user_service),
):
    return await service.list()


@UserRouter.get("/get-one/{id}", response_model=User, description="Locked to user who owns the account")
async def get_user(
    id: int,
    auth_user_id: int = check_ownership(model=User, get_user_field="id"),
    service: UserService = Depends(get_user_service),
):
    return await service.get(id)


@UserRouter.patch("/update", response_model=User, description="Locked to user who owns the account")
async def update(
    id: int,
    updates: UserUpdateSchema,
    auth_user_id: int = check_ownership(model=User, get_user_field="id"),
    service: UserService = Depends(get_user_service),
):
    return await service.update(id, updates)

@UserRouter.delete("/delete/{id}", description="Locked to user who owns the account")
async def delete(
    id: int,
    auth_user_id: int = check_ownership(model=User, get_user_field="id"),
    service: UserService = Depends(get_user_service),
):
    return await service.delete(id)

