from sqlalchemy import select

from src.database.models import Place
from .base_repository import BaseRepository


class PlaceRepository(BaseRepository):
    model = Place

    async def get_title(self, title: str):
        result = await self.session.execute(
            select(self.model).where(self.model.title == title)
        )

        return result.scalar_one_or_none()