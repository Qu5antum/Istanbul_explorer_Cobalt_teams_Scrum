from fastapi import APIRouter, Depends

from src.database.db import AsyncSession, get_session
from src.database.models import UserRole, User
from src.services.comment_service import CommentService
from src.api.dependencies.require_role_dependency import require_roles
from src.api.schemas.comment_schema import CommentCreate, CommentResponse

comment_router = APIRouter(
    prefix="/api",
    tags=["comments"]
)


async def get_comment_service(session: AsyncSession = Depends(get_session)):
    return CommentService(session=session)


@comment_router.post("/place/{place_id}/comment/create/", status_code=201)
async def create_comment(
    place_id: int,
    data: CommentCreate,
    user: User = Depends(require_roles(UserRole.USER, UserRole.ADMIN)),
    comment_service: CommentService = Depends(get_comment_service)
):
    return await comment_service.create_comment(data=data, place_id=place_id, user=user)


@comment_router.get("/place/{place_id}/comment/", response_model=list[CommentResponse], status_code=200)
async def get_comments(
    place_id: int,
    user: User = Depends(require_roles(UserRole.USER, UserRole.ADMIN)),
    comment_service: CommentService = Depends(get_comment_service)
):
    return await comment_service.get_all_comment_by_place(place_id=place_id)
    