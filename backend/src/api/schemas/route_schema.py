from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

from .user_schema import UserLocationRequest


class RouteGenerationRequest(BaseModel):
    route_title: str
    start_time: datetime
    budget: Optional[int] = Field(None, ge=100, le=1000000)
    userLocation: UserLocationRequest
    category_ids: list[int]