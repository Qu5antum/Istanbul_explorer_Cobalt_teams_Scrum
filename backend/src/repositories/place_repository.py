from sqlalchemy import select, or_

from src.database.models import Place, Category
from .base_repository import BaseRepository


class PlaceRepository(BaseRepository):
    model = Place

    async def get_title(self, title: str):
        result = await self.session.execute(
            select(self.model).where(self.model.title == title)
        )

        return result.scalar_one_or_none()

    async def search_title(self, title: str):
        result = await self.session.execute(
            select(self.model)
            .where(
                or_(
                    self.model.title.ilike(f'%{title}'),
                    self.model.address.ilike(f'%{title}')
                )
            )
        )

        return result.scalars().all()
    
    async def get_place_by_category(self, category_id: int):
        result = await self.session.execute(
            select(self.model)
            .join(self.model.categories)
            .where(Category.id == category_id)
        )

        return result.scalars().all()
