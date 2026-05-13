from fastapi import APIRouter, Depends

from src.database.db import AsyncSession, get_session
from src.database.models import UserRole, User
from src.services.comment_service import CommentService
from src.api.dependencies.require_role_dependency import require_roles

comment_router = APIRouter(
    prefix="/api",
    tags=["comments"]
)


async def get_comment_service(session: AsyncSession = Depends(get_session)):
    return CommentService(session=session)


@comment_router.post("/place/{place_id}/comment/create/", status_code=201)
async def create_comment(
    title: str,
    place_id: int,
    user: User = Depends(require_roles(UserRole.USER, UserRole.ADMIN)),
    comment_service: CommentService = Depends(get_comment_service)
):
    return await comment_service.create_comment(title=title, place_id=place_id)


@comment_router.get("/place/{place_id}/comment/", status_code=200)
async def get_comments(
    place_id: int,
    user: User = Depends(require_roles(UserRole.USER, UserRole.ADMIN)),
    comment_service: CommentService = Depends(get_comment_service)
):
    return await comment_service.get_all_comment_by_place(place_id=place_id)
    