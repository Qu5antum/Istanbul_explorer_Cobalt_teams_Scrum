from pydantic import BaseModel


class PlaceCreate(BaseModel):
    title: str
    link: str
    price: str
    latitude: float
    longitude: float
    address: str
    description: str
    category_ids: list[int]


class PlaceOut(PlaceCreate):
    id: int

    class Config:
        from_attributes = True