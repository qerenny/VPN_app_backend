from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import HTTPException
from vpn_backend.models.route_rule import RouteRule
from vpn_backend.repositories.route_rule_repository import RouteRuleRepository
from vpn_backend.schemas.route_rule_schema import RouteRuleCreateSchema, RouteRuleUpdateSchema


class RouteRuleService:
    def __init__(self, session: AsyncSession):
        self.routeRuleRepository = RouteRuleRepository(session)

    async def get(self, id: int) -> RouteRule:
        return await self.routeRuleRepository.get(id)

    async def list(self) -> List[RouteRule]:
        return await self.routeRuleRepository.get_all()

    async def create(self, route_rule: RouteRuleCreateSchema) -> RouteRule:
        return await self.routeRuleRepository.create(RouteRule.model_validate(route_rule))

    async def delete(self, id: int):
        return await self.routeRuleRepository.delete(id)

    async def update(
        self, id: int, updates: RouteRuleUpdateSchema,
    ) -> RouteRule:
        db_obj = await self.routeRuleRepository.get(id)
        if not db_obj:
            raise HTTPException(status_code=404, detail="Not found by this id")
        data = updates.model_dump(exclude_unset=True)
        for key, value in data.items():
            setattr(db_obj, key, value)
        return await self.routeRuleRepository.update(db_obj)
