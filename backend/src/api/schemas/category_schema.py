from pydantic import BaseModel


class CategoryCreate(BaseModel):
    title: str
    
