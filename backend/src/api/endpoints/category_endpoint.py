from fastapi import APIRouter, Depends

from src.database.db import AsyncSession, get_session
from src.database.models import User, UserRole
from src.services.category_service import CategoryService
from src.api.schemas.category_schema import CategoryCreate
from src.api.dependencies.require_role_dependency import require_roles


category_route = APIRouter(
    prefix="/api",
    tags=["categories"]
)


async def get_category_service(session: AsyncSession = Depends(get_session)):
    return CategoryService(session=session)


@category_route.post("/admin/category/create", status_code=201)
async def create_category(
    category: CategoryCreate,
    user: User = Depends(require_roles(UserRole.ADMIN)),
    category_service: CategoryService = Depends(get_category_service)
):
    return await category_service.create_category(category=category)


@category_route.get("/admin/category", status_code=200)
async def get_all_categories(
    user: User = Depends(require_roles(UserRole.ADMIN)),
    category_service: CategoryService = Depends(get_category_service)
):
    return await category_service.get_categories()