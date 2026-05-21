from uuid import UUID
from sqlalchemy import select, func

from .base_repository import BaseRepository
from src.database.models import PlaceRating


class RatingRepository(BaseRepository):
    model = PlaceRating

    async def get_rating_place_with_user(self, user_id: UUID, place_id: int):
        result = await self.session.execute(
            select(self.model)
            .where(
                self.model.user_id == user_id,
                self.model.place_id == place_id
            )
        )

        return result.scalar_one_or_none()
    
    async def get_place_rating(self, place_id: int):
        result = await self.session.execute(
            select(
                func.avg(PlaceRating.rating),
                func.count(PlaceRating.id)
            )
            .where(self.model.place_id==place_id)
        )

        average_rating, total_reviews = result.one()

        return {
            "average_rating": round(float(average_rating or 0), 1),
            "total_reviews": total_reviews
        }

