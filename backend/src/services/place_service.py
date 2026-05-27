from typing import Any
from sqlalchemy.exc import IntegrityError

from src.database.db import AsyncSession
from src.database.models import Place
from src.api.schemas.place_schema import PlaceCreate, PlaceUpdate
from src.repositories.place_repository import PlaceRepository
from src.repositories.category_repository import CategoryRepository
from src.exception_handlers.db_exception import DatabaseException
from src.exception_handlers.place_exception import PlaceNotFoundException, PlaceAlreadyExists
from src.api.schemas.user_schema import UserLocationRequest
from src.exception_handlers.category_exception import SomeCategoryNotFound


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
            raise SomeCategoryNotFound(
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
    
    async def get_place_by_id(self, userLocation: UserLocationRequest, place_id: int) -> (Any | None):
        place = await self.place_repo.get_place_by_id_with_distance(lat=userLocation.lat, lng=userLocation.lng, place_id=place_id)

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

    # Kullanıcıya yakın olan yerleri bulma metodu
    async def get_user_nearby_places(self, userLocation: UserLocationRequest, category_id: int | None = None):
        nearby_places = await self.place_repo.get_nearby_places(lat=userLocation.lat, lng=userLocation.lng, category_id=category_id)

        return nearby_places
    
    # Konumu yenileme metodu
    async def update_place_with_id(self, place_id: int, placeUpdate: PlaceUpdate):
        try:
            place = await self.place_repo.get_place_with_category(place_id=place_id)

            if not place:
                raise PlaceNotFoundException
            
            data=placeUpdate.model_dump(exclude_unset=True)

            category_ids = data.pop(
                "category_ids",
                None
            )
            update_place = await self.place_repo.update(id=place_id, data=data)

            if category_ids is not None:
                categories = await self.category_repo.get_categories_with_ids(
                    category_ids=category_ids
                )

                if len(categories) != len(category_ids):
                    raise ValueError(
                        "Bazı kategoriler bulunamadı"
                    )
                
                place.categories = categories

            await self.session.commit()
            await self.session.refresh(place)

            return update_place
        except IntegrityError:
            raise DatabaseException("Veritaban hatası")




    


    



