from fastapi import APIRouter, Depends

from src.database.db import AsyncSession, get_session
from src.api.schemas.rating_schema import RatingCreate
from src.database.models import User, UserRole
from src.api.dependencies.require_role_dependency import require_roles
from src.services.rating_service import RatingService


rating_route = APIRouter(
    prefix="/api",
    tags=["ratings"]
)


async def get_rating_service(session: AsyncSession = Depends(get_session)):
    return RatingService(session=session)


@rating_route.post("/place/{place_id}/rate", status_code=201)
async def place_rate(
    place_id: int,
    ratingCreate: RatingCreate,
    user: User = Depends(require_roles(UserRole.USER, UserRole.ADMIN)),
    rating_service: RatingService = Depends(get_rating_service)
):
    return await rating_service.place_rating_create(place_id=place_id, user=user, ratingCreate=ratingCreate)


@rating_route.get("/place/{place_id}/rating", status_code=200)
async def place_rating(
    place_id: int,
    user: User = Depends(require_roles(UserRole.USER, UserRole.ADMIN)),
    rating_service: RatingService = Depends(get_rating_service)
):
    return await rating_service.get_place_rating(place_id=place_id)