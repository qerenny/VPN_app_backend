from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession
from vpn_backend.models.user import User
from vpn_backend.repositories.user_repository import UserRepository
from vpn_backend.schemas.user_schema import UserRegistrationSchema, UserLoginSchema


class UserService:
    def __init__(self, session: AsyncSession):
        self.userRepository = UserRepository(session)

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
        return await self.userRepository.get_all()

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
