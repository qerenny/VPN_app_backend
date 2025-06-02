from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import HTTPException
from vpn_backend.models.user import User
from vpn_backend.repositories.user_repository import UserRepository
from vpn_backend.schemas.user_schema import UserRegistrationSchema, UserLoginSchema, UserUpdateSchema
from vpn_backend.utils.auth_handler import auth_handler


class UserService:
    def __init__(self, session: AsyncSession):
        self.userRepository = UserRepository(session)

    async def registration(self, body: UserRegistrationSchema):
        user_candidate = await self.userRepository.get_by_email(body.email)
        if user_candidate is not None:
            raise HTTPException(status_code=400, detail='Email is taken')
        password_hash = auth_handler.get_password_hash(body.password)
        user = User(email=body.email, password_hash=password_hash, role=body.role)
        await self.userRepository.create(user)
        token = auth_handler.encode_token(user.id)
        return {"token": token}

    async def login(self, body: UserLoginSchema):
        user_found = await self.userRepository.get_by_email(body.email)
        if user_found is None:
            raise HTTPException(status_code=400, detail='Invalid email')
        verified = auth_handler.verify_password(body.password, user_found.password_hash)
        if not verified:
            raise HTTPException(status_code=401, detail='Invalid password')
        token = auth_handler.encode_token(user_found.id)
        return {'token': token}

    async def me(self, authUserId: int):
        user_found = await self.userRepository.get(authUserId)
        if user_found is None:
            raise HTTPException(status_code=400, detail='Invalid id')
        token = auth_handler.encode_token(user_found.id)
        return {'user': user_found, 'token': token}

    async def get(self, id: int) -> User:
        return await self.userRepository.get(id)

    async def list(self) -> List[User]:
        return await self.userRepository.get_all()

    async def update(
        self, updates: UserUpdateSchema, id: int,
    ) -> User:
        db_user = await self.userRepository.get(id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        user_data = updates.model_dump(exclude_unset=True)
        for key, value in user_data.items():
            if key == 'password':
                password_hash = auth_handler.get_password_hash(value)
                setattr(db_user, 'password_hash', password_hash)
            else:
                setattr(db_user, key, value)
        return await self.userRepository.update(db_user)
    
    async def delete(self, id: int) -> None:
        db_user = await self.userRepository.get(id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        await self.userRepository.delete(db_user)
        return None

