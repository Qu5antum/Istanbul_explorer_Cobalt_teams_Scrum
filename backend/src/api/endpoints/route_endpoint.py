from fastapi import APIRouter, Depends
from uuid import UUID

from src.database.db import AsyncSession, get_session
from src.database.models import User, UserRole
from src.api.schemas.user_schema import UserLocationRequest
from src.api.schemas.route_schema import RouteGenerationRequest
from src.services.route_service import RouteService
from src.api.dependencies.require_role_dependency import require_roles

route_place_route = APIRouter(
    prefix="/api",
    tags=["routes"]
)

async def get_route_service(session: AsyncSession = Depends(get_session)):
    return RouteService(session=session)


@route_place_route.post("/route/generate", status_code=200)
async def generate_route(
    data: RouteGenerationRequest,
    user: User = Depends(require_roles(UserRole.USER, UserRole.ADMIN)),
    route_service: RouteService = Depends(get_route_service)
):
    return await route_service.generate_route(data=data, user=user)
    

@route_place_route.get("/route/all", status_code=200)
async def get_routes(
    user: User = Depends(require_roles(UserRole.USER, UserRole.ADMIN)),
    route_service: RouteService = Depends(get_route_service)
):
    return await route_service.get_routes(user=user)


@route_place_route.get("/route/{route_id}/route_places", status_code=200)
async def get_route_places(
    route_id: int,
    user: User = Depends(require_roles(UserRole.USER, UserRole.ADMIN)),
    route_service: RouteService = Depends(get_route_service)
):
    return await route_service.get_route_places(user=user, route_id=route_id)


@route_place_route.delete("/route/{route_id}/delete", status_code=200)
async def delete_route(
    route_id: int,
    user: User = Depends(require_roles(UserRole.USER, UserRole.ADMIN)),
    route_service: RouteService = Depends(get_route_service)
):
    return await route_service.delete_route(user=user, route_id=route_id)


@route_place_route.get("/route/{route_token}/shared", status_code=200)
async def get_route_with_token(
    route_token: UUID,
    user: User = Depends(require_roles(UserRole.USER, UserRole.ADMIN)),
    route_service: RouteService = Depends(get_route_service)
):
    return await route_service.get_route_by_link(route_token=route_token)

    