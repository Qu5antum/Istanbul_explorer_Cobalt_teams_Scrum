from sqlalchemy.exc import IntegrityError
from typing import Any

from src.database.db import AsyncSession
from src.database.models import Place
from src.api.schemas.place_schema import PlaceCreate
from src.repositories.place_repository import PlaceRepository
from src.repositories.category_repository import CategoryRepository
from src.exception_handlers.db_exception import DatabaseException
from src.exception_handlers.place_exception import PlaceNotFoundException, PlaceAlreadyExists


class PlaceService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.place_repo = PlaceRepository(session=self.session)
        self.category_repo = CategoryRepository(session=self.session)
    
    # Konum oluşturma metodu
    async def create_place(self, place: PlaceCreate):
        place_title = await self.place_repo.get_title(
            title=place.title
        )

        if place_title:
            raise PlaceAlreadyExists(
                "Böyle bir konum var zaten"
            )

        categories = await self.category_repo.get_categories_with_ids(
            category_ids=place.category_ids
        )

        if len(categories) != len(place.category_ids):
            raise ValueError(
                "Bazı kategoriler bulunamadı"
            )

        new_place = Place(
            title=place.title,
            link=place.link,
            price=place.price,
            latitude=place.latitude,
            longitude=place.longitude,
            address=place.address,
            description=place.description,
            image_path=place.image_path
        )

        new_place.categories = categories

        self.session.add(new_place)

        await self.session.commit()

        return {
            "detail": "Konum başarıyla oluşturuldu"
        }
    
    # Veritabanda olan her konuyu getir metodu
    async def get_all_places(self) -> list[dict | None]:
        places = await self.place_repo.get_all()

        return places
    
    async def get_place_by_id(self, place_id: int) -> (Any | None):
        place = await self.place_repo.get_object_by_id(id=place_id)

        return place
    
    async def search_place_by_title(self, title: str):
        place = await self.place_repo.search_title(title=title)

        if not place:
            raise PlaceNotFoundException("Konum bulunmadı")
        
        return place
    
    async def get_place_with_category(self, category_id: int):
        places = await self.place_repo.get_place_by_category_id(category_id=category_id)

        return places
    
    async def delete_place_with_id(self, place_id: int):
        delete_place = await self.place_repo.delete_place_by_id(place_id=place_id)

        if not delete_place:
            raise DatabaseException("Veritaban hatası")

        return {"detail": "Konum silindi"}

    
    


    



