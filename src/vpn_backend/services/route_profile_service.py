from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import HTTPException
from vpn_backend.models.route_profile import RouteProfile
from vpn_backend.repositories.route_profile_repository import RouteProfileRepository
from vpn_backend.schemas.route_profile_schema import RouteProfileCreateSchema, RouteProfileUpdateSchema


class RouteProfileService:
    def __init__(self, session: AsyncSession):
        self.routeProfileRepository = RouteProfileRepository(session)

    async def get(self, id: int) -> RouteProfile:
        return await self.routeProfileRepository.get(id)

    async def list(self) -> List[RouteProfile]:
        return await self.routeProfileRepository.get_all()

    async def create(self, route_profile: RouteProfileCreateSchema) -> RouteProfile:
        return await self.routeProfileRepository.create(RouteProfile.model_validate(route_profile))

    async def delete(self, id: int):
        return await self.routeProfileRepository.delete(id)

    async def update(
        self, id: int, updates: RouteProfileUpdateSchema,
    ) -> RouteProfile:
        db_obj = await self.routeProfileRepository.get(id)
        if not db_obj:
            raise HTTPException(status_code=404, detail="Not found by this id")
        data = updates.model_dump(exclude_unset=True)
        for key, value in data.items():
            setattr(db_obj, key, value)
        return await self.routeProfileRepository.update(db_obj)
