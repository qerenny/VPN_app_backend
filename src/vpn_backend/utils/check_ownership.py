from fastapi import Depends, HTTPException, Security
from sqlmodel.ext.asyncio.session import AsyncSession
from functools import wraps
from typing import Callable, Type, Any, Union
from sqlmodel import select
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from vpn_backend.configs.database.engine import get_db_connection
from vpn_backend.utils.auth_handler import auth_handler
from vpn_backend.models.user import User, UserRole


security = HTTPBearer()


def check_ownership(model: Type, *, get_user_field: Union[str, Callable[[Any], int]] = "user_id"):
    async def dependency(
        id: int,
        session: AsyncSession = Depends(get_db_connection),
        auth: HTTPAuthorizationCredentials = Security(security)
    ):
        auth_user_id = auth_handler.get_user(auth)

        # Получаем пользователя для проверки роли
        user_stmt = select(User).where(User.id == auth_user_id)
        user_result = await session.exec(user_stmt)
        current_user = user_result.first()

        if not current_user:
            raise HTTPException(status_code=401, detail="User not found")

        # Получаем объект (например, Payment)
        stmt = select(model).where(model.id == id)
        result = await session.exec(stmt)
        obj = result.first()

        if not obj:
            raise HTTPException(status_code=404, detail="Not found")

        # Проверка владельца
        user_id = (
            getattr(obj, get_user_field)
            if isinstance(get_user_field, str)
            else get_user_field(obj)
        )

        if user_id != auth_user_id and current_user.role != UserRole.ADMIN:
            raise HTTPException(status_code=403, detail="Forbidden")

        return auth_user_id

    return Depends(dependency)


def get_admin_user():
    async def dependency(
        session: AsyncSession = Depends(get_db_connection),
        auth: HTTPAuthorizationCredentials = Security(security),
    ):
        auth_user_id = auth_handler.get_user(auth)

        stmt = select(User).where(User.id == auth_user_id)
        result = await session.exec(stmt)
        user = result.first()

        if not user or user.role != UserRole.ADMIN:
            raise HTTPException(
                status_code=403,
                detail="Admin access required"
            )

        return auth_user_id

    return Depends(dependency)