from sqlalchemy import select, or_
from sqlalchemy.orm import selectinload

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
                    self.model.title.ilike(f'%{title}%'),
                    self.model.address.ilike(f'%{title}%')
                )
            )
        )

        return result.scalars().all()
    
    async def get_place_by_category_id(self, category_id: int):
        result = await self.session.execute(
            select(self.model)
            .options(selectinload(self.model.categories))
            .join(self.model.categories)
            .where(Category.id == category_id)
        )

        return result.scalars().all()
    
    async def delete_place_by_id(self, place_id: int):
        place = await self.session.get(self.model, place_id)

        if not place:
            return None
        
        await self.session.delete(place)
        await self.session.commit()
        
        return place
