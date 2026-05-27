from sqlalchemy import select
from sqlalchemy.orm import selectinload
from uuid import UUID

from .base_repository import BaseRepository
from src.database.models import Route, RoutePlace


class RouteRepository(BaseRepository):
    model = Route

    async def get_route_by_title(self, title: str):
        result = await self.session.execute(
            select(self.model)
            .where(self.model.title == title)
        )
        
        return result.scalar_one_or_none()
    
    async def get_routes_with_places(self, user_id: UUID):
        result = await self.session.execute(
            select(self.model)
            .where(self.model.user_id == user_id)
        )

        return result.scalars().all()
    
    async def delete_route_by_id(self, user_id: UUID, route_id: int):
        result = await self.session.execute(
            select(self.model)
            .where(
                self.model.id == route_id,
                self.model.user_id == user_id
            )
        )

        route = result.scalar_one_or_none()

        if not route:
            return None

        await self.session.delete(route)
        await self.session.commit()

        return route
    
    async def get_route_with_token(self, route_token: UUID):
        result = await self.session.execute(
            select(self.model)
            .options(selectinload(self.model.route_places))
            .where(self.model.share_token == route_token)
        )

        return result.scalar_one_or_none()


class RoutePlaceRepository(BaseRepository):
    model = RoutePlace

    async def get_route_places_with_route_id(self, user_id: UUID, route_id: int):
        result = await self.session.execute(
            select(self.model)
            .join(self.model.route)
            .options(selectinload(self.model.place))
            .where(
                Route.id == route_id,
                Route.user_id == user_id
            )
        )

        return result.scalars().all()