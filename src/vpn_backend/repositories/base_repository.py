from typing import TypeVar, Generic, Optional, Type, List
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, SQLModel

T = TypeVar("T", bound=SQLModel)


class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T], session: AsyncSession):
        self.model = model
        self.session = session

    async def get(self, id: int) -> Optional[T]:
        result = await self.session.exec(select(self.model).where(self.model.id == id))
        return result.first()

    async def get_all(self) -> List[T]:
        result = await self.session.exec(select(self.model))
        return result.all()

    async def get_all_by_id(self, user_id: int) -> List[T]:
        result = await self.session.exec(select(self.model).where(self.model.user_id == user_id))
        return result.all()

    async def create(self, obj: T) -> T:
        self.session.add(obj)
        await self.session.commit()
        await self.session.refresh(obj)
        return obj

    async def update(self, obj: T) -> T:
        self.session.add(obj)
        await self.session.commit()
        await self.session.refresh(obj)
        return obj

    async def delete(self, id: int) -> None:
        result = await self.session.exec(select(self.model).where(self.model.id == id))
        obj = result.first()
        if obj:
            await self.session.delete(obj)
            await self.session.commit()
