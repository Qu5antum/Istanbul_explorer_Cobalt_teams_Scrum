from fastapi import APIRouter, Depends

from src.database.db import AsyncSession, get_session
from src.database.models import User, UserRole
from src.services.place_service import PlaceService
from src.api.dependencies.require_role_dependency import require_roles
from src.api.schemas.place_schema import PlaceCreate


places_route = APIRouter(
    prefix="/api",
    tags=["places"]
)

async def get_place_service(session: AsyncSession = Depends(get_session)):
    return PlaceService(session=session)


@places_route.post("/admin/place/create", status_code=201)
async def create_place(
    place: PlaceCreate,
    user: User = Depends(require_roles(UserRole.ADMIN)),
    place_service: PlaceService = Depends(get_place_service)
):
    return await place_service.create_place(place=place)


@places_route.get("/admin/place/all", status_code=200)
async def get_all_places(
    place_service: PlaceService = Depends(get_place_service)
):
    return await place_service.get_all_places()


@places_route.get("/admin/place/{place_id}", status_code=200)
async def get_place_by_id(
    place_id: int,
    user: User = Depends(require_roles(UserRole.ADMIN)),
    place_service: PlaceService = Depends(get_place_service)
):
    return await place_service.get_place_by_id(place_id=place_id)


@places_route.get("/search/{title}", status_code=200)
async def search_title(
    title: str,
    user: User = Depends(require_roles(UserRole.USER, UserRole.ADMIN)),
    place_service: PlaceService = Depends(get_place_service)
):
    return await place_service.search_place_by_title(title=title)


@places_route.get("/admin/category/{category_id}")
async def get_place_by_category(
    category_id: int,
    user: User = Depends(require_roles(UserRole.USER, UserRole.ADMIN)),
    place_service: PlaceService = Depends(get_place_service)
):
    return await place_service.get_place_with_category(category_id=category_id)


@places_route.delete("/admin/delete_place", status_code=200)
async def delete_place(
    place_id: int,
    user: User = Depends(require_roles(UserRole.ADMIN)),
    place_service: PlaceService = Depends(get_place_service)
):
    return await place_service.delete_place_with_id(place_id=place_id)