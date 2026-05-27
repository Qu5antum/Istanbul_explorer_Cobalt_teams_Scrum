from datetime import datetime, timedelta, UTC
from typing import Any
from math import radians, sin, cos, sqrt, atan2
from sqlalchemy.exc import IntegrityError
from uuid import UUID

from src.database.db import AsyncSession
from src.database.models import User
from src.api.schemas.route_schema import RouteGenerationRequest
from src.repositories.place_repository import PlaceRepository
from src.repositories.category_repository import CategoryRepository
from src.repositories.route_repository import RouteRepository, RoutePlaceRepository
from src.exception_handlers.category_exception import SomeCategoryNotFound
from src.exception_handlers.db_exception import DatabaseException
from src.exception_handlers.route_exception import RouteAlreadyExists, RouteNotFound


CATEGORY_VISIT_DURATION = {
    "Cafe": 45,
    "Museum": 120,
    "Park": 60,
    "Restaurant": 90
}

def calculate_distance(lat1: float, lng1: float, lat2: float, lng2: float):
    R = 6371
    dlat = radians(lat2 - lat1)
    dlng = radians(lng2 - lng1)

    a = (
        sin(dlat / 2) ** 2
        +
        cos(radians(lat1))
        *
        cos(radians(lat2))
        *
        sin(dlng / 2) ** 2
    )
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c

def optimize_route(
    user_lat: float,
    user_lng: float,
    places: list[dict[str, Any]]
):
    optimized = []
    current_lat = user_lat
    current_lng = user_lng
    remaining_places = places.copy()

    while remaining_places:
        nearest_place = min(
            remaining_places,
            key=lambda item:
                calculate_distance(
                    current_lat,
                    current_lng,
                    item["place"].latitude,
                    item["place"].longitude
                )
        )

        optimized.append(nearest_place)

        current_lat = nearest_place["place"].latitude
        current_lng = nearest_place["place"].longitude

        remaining_places.remove(nearest_place)

    return optimized

def generate_timeline(
    optimized_places: list[dict[str, Any]],
    start_time: datetime = datetime.now(UTC)
):
    route_items = []
    current_time = start_time
    previous_lat = None
    previous_lng = None

    for order, place in enumerate(optimized_places, start=1):
        if previous_lat is None:
            travel_duration = 0
        else:
            distance = calculate_distance(
                previous_lat,
                previous_lng,
                place["place"].latitude,
                place["place"].longitude
            )
            travel_duration = int(distance * 5)

        current_time += timedelta(
            minutes=travel_duration
        )

        arrival_time = current_time
        category_title = place["place"].categories[0].title
        visit_duration = CATEGORY_VISIT_DURATION.get(
            category_title,
            60
        )

        departure_time = (
            arrival_time + timedelta(minutes=visit_duration)
        )

        route_items.append({
            "order": order,
            "place": place,
            "arrival_time": arrival_time,
            "departure_time": departure_time,
            "travel_duration": travel_duration,
            "visit_duration": visit_duration
        })

        current_time = departure_time
        previous_lat = place["place"].latitude
        previous_lng = place["place"].longitude

    return route_items

def filter_by_budget(
    places: list[dict[str, Any]],
    budget: int
):
    budget_filtered_places = []

    for item in places:
        place = item["place"]

        if place.price == "Free":
            budget_filtered_places.append(item)
            continue

        try:
            min_price, max_price = place.price.split('-')

            min_price = int(min_price)
            max_price = int(max_price)

            if min_price <= budget:
                budget_filtered_places.append(item)
        except(ValueError, AttributeError):
            continue
        
    return budget_filtered_places


class RouteService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.category_repo = CategoryRepository(session=self.session)
        self.place_repo = PlaceRepository(session=self.session)
        self.route_repo = RouteRepository(session=self.session)
        self.route_place_repo = RoutePlaceRepository(session=self.session)

    async def generate_route(
        self, 
        user: User,
        data: RouteGenerationRequest
    ) -> dict[str, Any]:
        route = await self.route_repo.get_route_by_title(title=data.route_title)
        
        if route:
            raise RouteAlreadyExists("Boyle bir rota zaten var")
        
        categories = await self.category_repo.get_categories_with_ids(category_ids=data.category_ids)

        if len(data.category_ids) != len(categories):
            raise SomeCategoryNotFound("Bazı kategoriler bulunamadı")
        
        places = await self.place_repo.get_places_with_category_ids(
            lat=data.userLocation.lat, 
            lng=data.userLocation.lng, 
            category_ids=data.category_ids
        )

        candidate_places = places  

        if data.budget:
            budget_filtered_places = filter_by_budget(
                places=candidate_places,
                budget=data.budget
            )

            candidate_places = budget_filtered_places

        optimized_places = optimize_route(
                user_lat=data.userLocation.lat,
                user_lng=data.userLocation.lng,
                places=candidate_places
            )
            
        route_items = generate_timeline(
            optimized_places=optimized_places,
            start_time=data.start_time
        )

        try:
            new_route = await self.route_repo.create(
                user_id=user.id,
                title=data.route_title,
                total_distance=round(sum(
                    item["place"]["distance"]
                    for item in route_items
                ), 2),
                estimated_duration=sum(
                    item["travel_duration"] + item["visit_duration"]
                    for item in route_items
                )
            )

            await self.session.flush()

            for item in route_items:
                new_route_place = await self.route_place_repo.create(
                    route_id=new_route.id,
                    place_id=item["place"]["place"].id,
                    order_number=item["order"],
                    title=item["place"]["place"].title,
                    arrival_time=item["arrival_time"],
                    departure_time=item["departure_time"],
                    travel_duration=item["travel_duration"],
                    visit_duration=item["visit_duration"]
                )
            
            await self.session.commit()
        except IntegrityError:
            raise DatabaseException("Veritaban hatası")

        return {
            "route_id": new_route.id,
            "title": new_route.title,
            "places": [
                {
                    "order": item["order"],
                    "title": item["place"]["place"].title,
                    "arrival_time": item["arrival_time"],
                    "departure_time": item["departure_time"]
                }
                for item in route_items
            ]
        }
    
    async def get_routes(self, user: User):
        routes = await self.route_repo.get_routes_with_places(user_id=user.id)

        return routes
    
    async def get_route_places(self, user: User, route_id: int):
        route = await self.route_repo.get(id=route_id)

        if not route:
            raise RouteNotFound("Rota bulunmadı")
            
        route_places = await self.route_place_repo.get_route_places_with_route_id(
            user_id=user.id,
            route_id=route_id
        )

        return route_places
    
    async def delete_route(self, user: User, route_id: int):
        route_to_delete = await self.route_repo.delete_route_by_id(
            user_id=user.id,
            route_id=route_id
        )

        if route_to_delete is None:
            raise RouteNotFound("Rota bulunmadı")
        
        return {"detail": "Rota başarıyla silindi"}


    async def get_route_by_link(self, route_token: UUID):
        route = await self.route_repo.get_route_with_token(route_token=route_token)

        if not route:
            raise RouteNotFound("Rota bulunmadı")
        
        place_ids = [route_place.place_id for route_place in route.route_places]
        
        places = await self.place_repo.get_places_with_ids(place_ids=place_ids)

        places_map = {
            place.id: place
            for place in places
        }

        formatted_places = []

        for route_place in sorted(
            route.route_places,
            key=lambda x: x.order_number
        ):
            formatted_places.append({
                "id": route_place.id,
                "order_number": route_place.order_number,
                "arrival_time": route_place.arrival_time,
                "departure_time": route_place.departure_time,
                "travel_duration": route_place.travel_duration,
                "visit_duration": route_place.visit_duration,
                "place": places_map.get(route_place.place_id)
            })

        return {
            "id": route.id,
            "title": route.title,
            "total_distance": route.total_distance,
            "estimated_duration": route.estimated_duration,
            "is_public": route.is_public,
            "share_token": route.share_token,
            "places": formatted_places
        }