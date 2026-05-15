from fastapi import APIRouter, Depends

from src.database.db import AsyncSession, get_session
from src.services.favorite_place_service import FavoritePlaceService
from src.database.models import User, UserRole
from src.api.dependencies.require_role_dependency import require_roles


favorite_place_router = APIRouter(
    prefix="/api",
    tags=["favorite_places"]
)

async def get_favorite_place_service(session: AsyncSession = Depends(get_session)):
    return FavoritePlaceService(session=session)


@favorite_place_router.post("/place/{place_id}/favorite", status_code=201)
async def add_to_favorite(
    place_id: int,
    user: User = Depends(require_roles(UserRole.USER, UserRole.ADMIN)),
    favorite_place_service: FavoritePlaceService = Depends(get_favorite_place_service)
):
    return await favorite_place_service.add_place_to_favorite(user=user, place_id=place_id)
    

@favorite_place_router.delete("/place/{place_id}/favorite", status_code=200)
async def delete_place_from_favorite(
    place_id: int,
    user: User = Depends(require_roles(UserRole.USER, UserRole.ADMIN)),
    favorite_place_service: FavoritePlaceService = Depends(get_favorite_place_service)
):
    return await favorite_place_service.delete_favorite_place(user=user, place_id=place_id)


@favorite_place_router.get("/user/favorites", status_code=200)
async def get_user_favorites_places(
    user: User = Depends(require_roles(UserRole.USER, UserRole.ADMIN)),
    favorite_place_service: FavoritePlaceService = Depends(get_favorite_place_service)
):
    return await favorite_place_service.get_favorite_places(user=user)
