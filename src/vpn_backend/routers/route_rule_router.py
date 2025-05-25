from typing import List
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from vpn_backend.configs.database.engine import get_db_connection
from vpn_backend.models.route_rule import RouteRule
from vpn_backend.services.route_rule_service import RouteRuleService
from vpn_backend.schemas.route_rule_schema import RouteRuleCreateSchema, RouteRuleUpdateSchema
from vpn_backend.utils.auth_handler import auth_handler

RouteRuleRouter = APIRouter(prefix="/route-rules", tags=["route_rule"])

def get_route_rule_service(session: AsyncSession = Depends(get_db_connection)) -> RouteRuleService:
    return RouteRuleService(session)

@RouteRuleRouter.get("/get-all", response_model=List[RouteRule])
async def get_all(
    service: RouteRuleService = Depends(get_route_rule_service),
):
    return await service.list()

@RouteRuleRouter.get("/get-one/{id}", response_model=RouteRule)
async def get_route_rule(
    id: int,
    service: RouteRuleService = Depends(get_route_rule_service),
):
    return await service.get(id)

@RouteRuleRouter.post("/create", response_model=RouteRule)
async def create(
    route_rule: RouteRuleCreateSchema,
    service: RouteRuleService = Depends(get_route_rule_service),
):
    return await service.create(route_rule)

@RouteRuleRouter.delete("/delete/{id}")
async def delete(
    id: int,
    service: RouteRuleService = Depends(get_route_rule_service),
):
    return await service.delete(id)

@RouteRuleRouter.patch("/update/{id}", response_model=RouteRule)
async def update(
    id: int,
    updates: RouteRuleUpdateSchema,
    service: RouteRuleService = Depends(get_route_rule_service),
):
    return await service.update(id, updates)
