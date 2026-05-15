from sqlalchemy import select
from sqlalchemy.orm import selectinload

from .base_repository import BaseRepository
from src.database.models import FavoritePlace, User, Place


class FavoritePlaceRepository(BaseRepository):
    model = FavoritePlace

    async def delete_favorite(self, user: User, place_id: int):
        result = await self.session.execute(
            select(self.model)
            .where(
                self.model.user_id == user.id,
                self.model.place_id == place_id
            )
        )

        favorite_place = result.scalar_one_or_none()

        if not favorite_place:
            return None
        
        await self.session.delete(favorite_place)
        await self.session.commit()

        return favorite_place