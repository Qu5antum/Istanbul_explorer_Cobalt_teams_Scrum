from sqlalchemy.exc import IntegrityError

from src.database.db import AsyncSession
from src.repositories.rating_repository import RatingRepository
from src.repositories.place_repository import PlaceRepository
from src.api.schemas.rating_schema import RatingCreate
from src.database.models import User
from src.exception_handlers.db_exception import DatabaseException
from src.exception_handlers.place_exception import PlaceNotFoundException


class RatingService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.rating_repo = RatingRepository(session=self.session)
        self.place_repo = PlaceRepository(session=self.session)

    async def place_rating_create(
        self,
        place_id: int,
        user: User,
        ratingCreate: RatingCreate
    ):
        place = await self.place_repo.get(id=place_id)

        if not place:
            raise PlaceNotFoundException("Konum bulunmadı")

        rating = await self.rating_repo.get_rating_place_with_user(
            user_id=user.id,
            place_id=place_id
        )

        if rating:
            rating.rating = ratingCreate.rating

            await self.session.commit()
            await self.session.refresh(rating)

            return {
                "detail": "Değerlendirme güncellendi"
            }

        try:
            new_rating = await self.rating_repo.create(
                rating=ratingCreate.rating,
                place_id=place_id,
                user_id=user.id
            )

            await self.session.commit()
            await self.session.refresh(new_rating)

        except IntegrityError:
            raise DatabaseException("Veritaban hatası")
        
        return {"detail": "Değerlendirme başarıyla bıraktınız"}


    async def get_place_rating(self, place_id: int):
        place = await self.place_repo.get(id=place_id)

        if not place:
            raise PlaceNotFoundException("Konum bulunmadı")

        place_rating = await self.rating_repo.get_place_rating(place_id=place_id)

        return place_rating





        
        
    