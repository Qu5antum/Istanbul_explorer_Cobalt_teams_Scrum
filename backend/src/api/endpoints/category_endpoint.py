from fastapi import APIRouter, Depends

from src.database.db import AsyncSession, get_session
from src.services.category_service import CategoryService
from src.api.schemas.category_schema import CategoryCreate


category_route = APIRouter(
    prefix="/api/category",
    tags=["categories"]
)


async def get_category_service(session: AsyncSession = Depends(get_session)):
    return CategoryService(session=session)


@category_route.post("/create", status_code=201)
async def create_category(
    category: CategoryCreate,
    category_service: CategoryService = Depends(get_category_service)
):
    return await category_service.create_category(category=category)