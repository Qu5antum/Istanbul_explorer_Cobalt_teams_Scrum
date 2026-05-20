from sqlalchemy import select, or_, and_, func
from sqlalchemy.orm import selectinload

from src.database.models import Place, Category, User, FavoritePlace
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
    
    async def get_place_with_category(self, place_id: int):
        result = await self.session.execute(
            select(self.model)
            .options(selectinload(self.model.categories))
            .where(self.model.id == place_id)
        )

        return result.scalar_one_or_none()
    
    async def delete_place_by_id(self, place_id: int):
        place = await self.session.get(self.model, place_id)

        if not place:
            return None
        
        await self.session.delete(place)
        await self.session.commit()
        
        return place
    
    async def get_favorite_places_with_id(self, user: User):
        result = await self.session.execute(
            select(self.model)
            .join(FavoritePlace)
            .where(FavoritePlace.user_id == user.id)
        )

        return result.scalars().all()
    

    async def get_nearby_places(
        self,
        lat: float,
        lng: float,
        radius: float = 0.05,
        category_id: int = None
    ):
        distance = (
            6371 *
            func.acos(
                func.cos(func.radians(lat))
                *
                func.cos(func.radians(self.model.latitude))
                *
                func.cos(
                    func.radians(self.model.longitude)
                    -
                    func.radians(lng)
                )
                +
                func.sin(func.radians(lat))
                *
                func.sin(func.radians(self.model.latitude))
            )
        ).label("distance")
        
        query = (
            select(
                self.model,
                distance
            )
            .where(
                and_(
                    self.model.latitude.between(
                        lat - radius,
                        lat + radius
                    ),
                    self.model.longitude.between(
                        lng - radius,
                        lng + radius
                    )
                )
            )
            .order_by(distance.asc())
        )
        if category_id:
            query = (
                query
                .options(
                    selectinload(self.model.categories)
                )
                .join(self.model.categories)
                .where(Category.id == category_id)
            )
        result = await self.session.execute(query)
        rows = result.all()
        return [
            {
                **place.__dict__,
                "distance": round(distance_value, 2)
            }
            for place, distance_value in rows
        ]
    
    async def get_place_by_id_with_distance(
        self,
        lat: float,
        lng: float,
        place_id: int
    ):
        distance = (
            6371 *
            func.acos(
                func.cos(func.radians(lat))
                *
                func.cos(func.radians(self.model.latitude))
                *
                func.cos(
                    func.radians(self.model.longitude)
                    -
                    func.radians(lng)
                )
                +
                func.sin(func.radians(lat))
                *
                func.sin(func.radians(self.model.latitude))
            )
        ).label("distance")

        query = (
            select(
                self.model,
                distance
            )
            .where(self.model.id == place_id)
        )

        result = await self.session.execute(query)

        row = result.first()

        if not row:
            return None

        place, distance_value = row

        return {
            "id": place.id,
            "title": place.title,
            "description": place.description,
            "address": place.address,
            "price": place.price,
            "latitude": place.latitude,
            "longitude": place.longitude,
            "image_path": place.image_path,
            "link": place.link,
            "created_at": place.created_at,
            "distance": round(distance_value, 2)
        }