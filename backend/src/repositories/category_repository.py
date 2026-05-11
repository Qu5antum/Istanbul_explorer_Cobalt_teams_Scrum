from sqlalchemy import select

from src.database.models import Category
from .base_repository import BaseRepository


class CategoryRepository(BaseRepository):
    model = Category

    async def get_title(self, title: str):
        result = await self.session.execute(
            select(self.model).where(self.model.title == title)
        )

        return result.scalar_one_or_none()
    
    async def get_categories_with_ids(self, category_ids: list[int]):
        result = await self.session.execute(
            select(self.model).where(self.model.id.in_(category_ids))
        )

        return result.scalars().all()