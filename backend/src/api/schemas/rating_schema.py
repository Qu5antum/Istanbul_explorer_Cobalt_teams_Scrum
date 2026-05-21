from pydantic import BaseModel, Field


class RatingCreate(BaseModel):
    rating: int = Field(ge=1, le=5) 