from typing import List, Optional

from fastapi import Depends
from vpn_backend.models.user import User

from vpn_backend.repositories.user_repository import UserRepository
from vpn_backend.schemas.user_schema import UserRegistrationSchema, UserLoginSchema


class UserService:
    userRepository: UserRepository

    def __init__(
        self, userRepository: UserRepository = Depends()
    ) -> None:
        self.userRepository = userRepository

    async def registration(self, body: UserRegistrationSchema):
        return await self.userRepository.create(
            User(email=body.email, password_hash=body.password)
        )

    async def login(self, body: UserLoginSchema):
        return await self.userRepository.create(
            User(email=body.email, password_hash=body.password)
        )

    async def get(self, id: int) -> User:
        return await self.userRepository.get(id)

    async def list(self) -> List[User]:
        users = await self.userRepository.get_all()
        print(users)
        return users

    # def delete(self, author_id: int) -> None:
    #     return self.authorRepository.delete(
    #         Author(id=author_id)
    #     )

    # def update(
    #     self, author_id: int, author_body: AuthorSchema
    # ) -> Author:
    #     return self.authorRepository.update(
    #         author_id, Author(name=author_body.name)
    #     )