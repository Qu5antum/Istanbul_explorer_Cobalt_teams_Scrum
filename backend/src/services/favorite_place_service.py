from sqlalchemy.exc import IntegrityError

from src.database.db import AsyncSession
from src.database.models import User
from src.repositories.place_repository import PlaceRepository
from src.repositories.favorite_place_repository import FavoritePlaceRepository
from src.exception_handlers.place_exception import PlaceNotFoundException
from src.exception_handlers.db_exception import DatabaseException


class FavoritePlaceService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.place_repo = PlaceRepository(session=self.session)
        self.favorite_repo = FavoritePlaceRepository(session=self.session)

    async def add_place_to_favorite(self, user: User, place_id: int):
        place = await self.place_repo.get(id=place_id)

        if not place:
            raise PlaceNotFoundException("Konum bulunmadı")
        
        try:
            new_favorite = await self.favorite_repo.create(
                user_id=user.id,
                place_id=place_id
            )

            await self.session.commit()
            await self.session.refresh(new_favorite)
        except IntegrityError:
            raise DatabaseException("Veritabanı hatası")
        
        return {"detail": "Favoriye eklendi"}
    
    async def delete_favorite_place(self, user: User, place_id: int):
        place = await self.place_repo.get(id=place_id)

        if not place:
            raise PlaceNotFoundException("Konum bulunmadı")
        
        delete_favorite = await self.favorite_repo.delete_favorite(
            user=user,
            place_id=place_id
        )

        if not delete_favorite:
            raise DatabaseException("Veritabanı hatası")
        
        return {"detail": "Favorilerinden silindi"}
    
    async def get_favorite_places(self, user: User):
        favorite_places = await self.place_repo.get_favorite_places_with_id(
            user=user
        )

        return favorite_places
        