from pydantic import BaseModel


class PlaceCreate(BaseModel):
    title: str
    link: str
    price: str
    latitude: float
    longitude: float
    address: str
    description: str
    image_path: str
    category_ids: list[int]


class PlaceUpdate(BaseModel):
    title: str | None = None
    link: str | None = None
    price: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    address: str | None = None
    description: str | None = None
    image_path: str | None = None
    category_ids: list[int] | None = None


class PlaceOut(PlaceCreate):
    id: int

    class Config:
        from_attributes = True